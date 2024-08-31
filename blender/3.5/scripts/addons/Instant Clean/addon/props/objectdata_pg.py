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
from bpy.props import (BoolProperty, EnumProperty)


class INSTANTCLEAN_PG_Objectdata_Settings(bpy.types.PropertyGroup):
    material_slots: BoolProperty(
        name='Material Slots',
        default=True,
        description='Removes all material slots whose materials are not assigned to the mesh'
    )

    material_slots_clear: EnumProperty(
        name='Clear Method',
        items=[
            ('UNUSED', 'Unused Only', 'Clear unused material slots only', '', 0),
            ('ALL', 'All', 'Clear all material slots', '', 1),
        ],
        description='Material slots clearing method'
    )

    double_materials: BoolProperty(
        name='Material Doubles',
        default=True,
        description='Merges all materials starting with the same name into one, respectively'
    )

    double_materials_remove_data: BoolProperty(
        name='Remove Data',
        default=False,
        description='Remove material doubles from the file destructively'
    )

    empty_vertex_groups: BoolProperty(
        name='Empty Groups',
        default=True,
        description='Removes all vertex groups which have no vertices assigned to it'
    )