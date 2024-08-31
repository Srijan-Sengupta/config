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
import re


def objectdata(context, objects, bmeshes):
    stats = {
        'Double Materials': False,
        'Material Slots': False,
        'Vertex Groups': False,
    }

    pg = context.scene.instantclean_objectdata
    if pg.empty_vertex_groups:
        stats['Vertex Groups'] = 0
        for obj, bm in zip(objects, bmeshes):
            for vg in obj.vertex_groups.values():
                used = False
                for vert in bm.verts:
                    try: v = vg.weight(vert.index)
                    except: continue
                    if v == 0: continue
                    used = True
                    break

                if not used:
                    context.view_layer.objects.active = obj
                    bpy.ops.object.vertex_group_set_active(group=vg.name)
                    bpy.ops.object.vertex_group_remove()
                    stats['Vertex Groups'] += 1

    bpy.ops.object.mode_set(mode='OBJECT')
                
    if pg.material_slots:
        stats['Material Slots'] = 0  
        for obj in objects:
            context.view_layer.objects.active = obj
            prev_matslots = len(obj.material_slots)
            if pg.material_slots_clear == 'UNUSED':
                bpy.ops.object.material_slot_remove_unused()
            elif pg.material_slots_clear == 'ALL':
                for i, ms in enumerate(obj.material_slots):
                    obj.active_material_index = i
                    bpy.ops.object.material_slot_remove()

            stats['Material Slots'] += prev_matslots - len(obj.material_slots)

    if pg.double_materials:
        stats['Double Materials'] = 0
        pattern = re.compile(r'[.]\d+$')
        materials = set()
        unique_mats = {}
        double_mats = {}
        for obj in objects:
            for m in obj.data.materials:
                if not m: continue
                materials.add(m)

        for mat in materials:
            matches = re.findall(pattern, mat.name)
            if matches:
                mat_stem = mat.name.removesuffix(matches[0])
                if mat_stem in unique_mats.keys(): double_mats[mat.name] = mat_stem
                else:
                    orig_mat = bpy.data.materials.get(mat_stem)
                    if orig_mat:
                        unique_mats[mat_stem] = orig_mat
                        double_mats[mat.name] = mat_stem

                    else: unique_mats[mat_stem] = mat

            else:
                unique_mats[mat.name] = mat

        for obj in objects:
            context.view_layer.objects.active = obj
            double_ms = set()
            for ms in obj.material_slots:
                orig_mat_name = double_mats.get(ms.name)
                if not orig_mat_name: continue
                if not any(orig_mat_name == m.name for m in obj.material_slots):
                    ms.material = unique_mats[orig_mat_name]
                else:
                    double_ms.add(ms.name)

            for ms_name in double_ms:
                idx = [i for i, m in enumerate(obj.material_slots) if ms_name == m.name][0]
                obj.active_material_index = idx
                bpy.ops.object.material_slot_remove()
                stats['Double Materials'] += 1

        if pg.double_materials_remove_data:
            for key in double_mats.keys():
                mat = bpy.data.materials.get(key)
                if mat: bpy.data.materials.remove(mat)

    bpy.ops.object.mode_set(mode='EDIT')

    return stats