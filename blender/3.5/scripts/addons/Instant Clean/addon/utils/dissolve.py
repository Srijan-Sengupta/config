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


def dissolve(context, objects, bmeshes):
    stats = {
        'Vertices': 0,
        'Edges': 0,
        'Faces': 0
    }

    pg = context.scene.instantclean_dissolve
    protect_mask = [True, pg.protect_materials, pg.protect_seam, pg.protect_sharp, pg.protect_uv]
    protect = ['NORMAL', 'MATERIAL', 'SEAM', 'SHARP', 'UV']
    delimiter = [d for i, d in enumerate(protect) if protect_mask[i]]
    
    bpy.ops.mesh.select_all(action='SELECT')
    for o in objects:
        prev_count = o.data.count_selected_items()
        stats['Vertices'] += prev_count[0]
        stats['Edges'] += prev_count[1]
        stats['Faces'] += prev_count[2]

    bpy.ops.mesh.dissolve_limited(angle_limit=pg.max_angle, use_dissolve_boundaries=pg.boundaries, delimit=set(delimiter))

    for o in objects:
        after_count = o.data.count_selected_items()
        stats['Vertices'] -= after_count[0]
        stats['Edges'] -= after_count[1]
        stats['Faces'] -= after_count[2]

    return stats