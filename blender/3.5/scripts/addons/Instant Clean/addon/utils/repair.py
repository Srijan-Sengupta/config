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


def repair(context, objects, bmeshes):
    stats = {
        'Loose Verts': False,
        'Loose Edges': False,
        'Loose Faces': False,
        'Doubles': False,
        'Zero Faces': False,
        'Dispensables': False,
        'Non-Manifold Faces': False,
        'Non-Manifold Verts': False,
        'Filled Holes': False,
    }

    pg = context.scene.instantclean_repair
    if pg.doubles:
        for o in objects: stats['Doubles'] += o.data.count_selected_items()[0]
        bpy.ops.mesh.remove_doubles(threshold=pg.doubles_dst)
        for o in objects: stats['Doubles'] -= o.data.count_selected_items()[0]

    if pg.loose:
        for o in objects:
            count = o.data.count_selected_items()
            stats['Loose Verts'] += count[0]
            stats['Loose Edges'] += count[1]
            stats['Loose Faces'] += count[2]

        bpy.ops.mesh.delete_loose(use_verts=pg.loose_verts, use_edges=pg.loose_edges, use_faces=pg.loose_faces)
        bpy.ops.mesh.select_all(action='SELECT')
        for o in objects:
            count = o.data.count_selected_items()
            stats['Loose Verts'] -= count[0]
            stats['Loose Edges'] -= count[1]
            stats['Loose Faces'] -= count[2]

    if pg.zero_faces:
        for o in objects: stats['Zero Faces'] += o.data.count_selected_items()[2]
        bpy.ops.mesh.dissolve_degenerate(threshold=pg.zero_faces_area)
        for o in objects: stats['Zero Faces'] -= o.data.count_selected_items()[2]

    if pg.dispensables:
        for o, bm in zip(objects, bmeshes):
            stats['Dispensables'] += o.data.count_selected_items()[0]
            bmesh.ops.dissolve_verts(bm, verts=[v for v in bm.verts if len(v.link_edges) == 2 and v.calc_edge_angle(0) < pg.dispensables_ang])
            
        for o in objects: stats['Dispensables'] -= o.data.count_selected_items()[0]

    return stats