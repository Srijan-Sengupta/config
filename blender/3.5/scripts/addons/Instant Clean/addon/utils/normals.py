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


def normals(context, objects, bmeshes):
    stats = {
        'Flipped': False,
        'Sharp Edges': False,
        'Weighted Normals': False,
    }

    pg = bpy.context.scene.instantclean_normals
    if pg.recalculate:
        stats['Flipped'] = 0
        face_normals = []
        for bm in bmeshes: face_normals.append([f.normal.copy() for f in bm.faces])
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.normals_make_consistent(inside=pg.recalculate_orientation == 'INSIDE')

        for bm, fns in zip(bmeshes, face_normals):
            stats['Flipped'] += sum(1 for f, n in zip(bm.faces, fns) if f.normal != n)

    if pg.auto_smooth:
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.faces_shade_smooth()
        for obj in objects:
            obj.data.use_auto_smooth = True
            obj.data.auto_smooth_angle = pg.auto_smooth_ang

    if pg.weighted_normals:
        stats['Weighted Normals'] = 0
        for obj in objects:
            try:
                for m in obj.modifiers.values():
                    if m.type == 'WEIGHTED_NORMAL':
                        raise Exception
                    
            except Exception: continue

            mod = obj.modifiers.new(name='Weighted Normals', type='WEIGHTED_NORMAL')
            mod.keep_sharp = True
            stats['Weighted Normals'] += 1
    
    if pg.clear_custom_split_normals:
        bpy.ops.mesh.select_all(action='SELECT')
        for obj in objects:
            bpy.context.view_layer.objects.active = obj
            bpy.ops.mesh.customdata_custom_splitnormals_clear()

    if pg.clear_sharp_edges:
        stats['Sharp Edges'] = 0
        for bm in bmeshes:
            for e in bm.edges:
                if e.smooth: continue
                e.smooth = True
                stats['Sharp Edges'] += 1

    return stats