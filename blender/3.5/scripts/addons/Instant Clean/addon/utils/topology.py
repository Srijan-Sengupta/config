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


def topology(context, objects, bmeshes):
    stats = {}

    pg = context.scene.instantclean_topology
    if pg.type == 'TRIS':
        bpy.ops.mesh.select_face_by_sides(number=3, type='EQUAL', extend=False)
        prev_count = 0
        for obj in objects: prev_count += obj.data.count_selected_items()[2]
        
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.quads_convert_to_tris(quad_method=pg.quad_method, ngon_method=pg.ngon_method)

        stats['Increased %'] = round(100 * (1 - (prev_count / sum(len(bm.faces) for bm in bmeshes))), 2)
        stats['Tris %'] = 100.0

    elif pg.type == 'QUADS':
        bpy.ops.mesh.select_face_by_sides(number=4, type='EQUAL', extend=False)
        prev_count = 0
        for obj in objects: prev_count += obj.data.count_selected_items()[2]
        prev_percentage = (prev_count / sum(len(bm.faces) for bm in bmeshes))

        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.tris_convert_to_quads(
            face_threshold=pg.quad_max_face_ang,
            shape_threshold=pg.quad_max_shape_ang,
            uvs=pg.compare_uv,
            vcols=pg.compare_vcol,
            seam=pg.compare_seam,
            sharp=pg.compare_sharp,
            materials=pg.compare_material
        )

        bpy.ops.mesh.select_face_by_sides(number=4, type='EQUAL', extend=False)
        after_count = 0
        for obj in objects: after_count += obj.data.count_selected_items()[2]

        after_percentage = (after_count / sum(len(bm.faces) for bm in bmeshes))
        stats['Increased %'] = round(100 * ((after_percentage) - prev_percentage), 2)
        stats['Quads %'] = round(100 * after_percentage, 2)

    return stats