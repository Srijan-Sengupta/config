# Instant Clean  Copyright (C) 2023  Ruben Messerschmidt

# Instant Clean is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Instant Clean is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



import bpy
import bmesh


def manifold(context, objects, bmeshes):
    stats = {
        'Non-Manifold Faces': False,
        'Non-Manifold Verts': False,
        'Wire Geometry': False,
        'Filled Holes': False,
        'Flattened Faces': False,
        'Undistorted Faces': False,
    }

    pg = context.scene.instantclean_manifold
    if pg.non_manifold_faces:
        bpy.ops.mesh.select_all(action='SELECT')
        for o in objects: stats['Non-Manifold Faces'] += o.data.count_selected_items()[2]
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
        bpy.ops.mesh.select_interior_faces()
        bpy.ops.mesh.delete(type='FACE')
        bpy.ops.mesh.select_all(action='SELECT')
        for o in objects: stats['Non-Manifold Faces'] -= o.data.count_selected_items()[2]

    if pg.non_manifold_verts:
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
        bpy.ops.mesh.select_non_manifold(extend=False, use_wire=False, use_boundary=False, use_multi_face=False, use_non_contiguous=False, use_verts=True)
        stats['Non-Manifold Verts'] = 0
        for bm in bmeshes:
            nm_verts = [v for v in bm.verts if v.select and all(e.link_faces for e in v.link_edges)]
            if not nm_verts: continue
            stats['Non-Manifold Verts'] += len(nm_verts)
            for nm_v in nm_verts:
                merge_co = nm_v.co
                parts = []
                prev_edge = nm_v.link_edges[0]
                parts.append(set((prev_edge,)))
                while(sum([len(p) for p in parts]) != len(nm_v.link_edges)):
                    linked_edge = [e for e in nm_v.link_edges if e not in parts[-1] and any(f in prev_edge.link_faces for f in e.link_faces)]
                    if linked_edge:
                        linked_edge = linked_edge[0]
                        parts[-1].add(linked_edge)

                    else:
                        prev_edge = [e for e in nm_v.link_edges if e not in parts[-1]][0]
                        parts.append(set((prev_edge,)))


                for p in parts:
                    bpy.ops.mesh.select_all(action='DESELECT')
                    res = bmesh.ops.bisect_edges(bm, edges=list(p), cuts=1)
                    new_verts = [i for i in res['geom_split'] if type(i) is bmesh.types.BMVert]
                    len_nv = len(new_verts) - 1
                    for i in range(len_nv):
                        bmesh.ops.pointmerge(bm, verts=[new_verts[0], new_verts[i+1]], merge_co=merge_co)

                bmesh.ops.delete(bm, geom=[e.other_vert(new_verts[0]) for e in new_verts[0].link_edges if not e.link_faces])

    if pg.wire_geo:
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
        bpy.ops.mesh.select_non_manifold(extend=False, use_wire=True, use_boundary=False, use_multi_face=False, use_non_contiguous=False, use_verts=False)
        for o in objects:
            stats['Wire Geometry'] += o.data.count_selected_items()[1]

        bpy.ops.mesh.delete(type='EDGE')

    if pg.fill_holes:
        bpy.ops.mesh.select_all(action='SELECT')
        for o in objects: stats['Filled Holes'] = -o.data.count_selected_items()[2]
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
        bpy.ops.mesh.select_non_manifold(extend=False, use_wire=False, use_boundary=True, use_multi_face=False, use_non_contiguous=False, use_verts=False)
        bpy.ops.mesh.fill_holes(sides=pg.fill_holes_max_sides)
        bpy.ops.mesh.select_all(action='SELECT')
        for o in objects: stats['Filled Holes'] += o.data.count_selected_items()[2]

    if pg.flatten:
        bpy.ops.mesh.select_all(action='SELECT')
        prev_normals = []
        for bm in bmeshes:
            prev_normals.append([f.normal.copy() for f in bm.faces if f.select])

        bpy.ops.mesh.face_make_planar(factor=pg.flatten_factor, repeat=pg.flatten_iterations)
        for bm, pns in zip(bmeshes, prev_normals):
            stats['Flattened Faces'] += sum(1 for f, n in zip(bm.faces, pns) if f.select and f.normal != n)

    if pg.undistort:
        stats['Undistorted Faces'] = 0
        bpy.ops.mesh.select_all(action='SELECT')
        for bm in bmeshes:
            for f in [f for f in bm.faces if f.select]:
                f_no = f.normal
                for l in f.loops:
                    l_no = l.calc_normal()
                    if l_no.dot(f_no) < 0: l_no = l_no * -1
                    if f_no.angle(l_no, 1000) > pg.undistort_ang:
                        f.select_set(False)
                        stats['Undistorted Faces'] += 1
                        break

        bpy.ops.mesh.select_all(action='INVERT')
        bpy.ops.mesh.quads_convert_to_tris()
                        
    return stats