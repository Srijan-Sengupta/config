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
from bpy.props import (BoolProperty, FloatProperty, EnumProperty)


class INSTANTCLEAN_PG_Normals_Settings(bpy.types.PropertyGroup):
    recalculate: BoolProperty(
        name='Recalculate',
        default=True,
        description='Recalculate the normal of each face'
    )

    recalculate_orientation: EnumProperty(
            name='Orientation',
            items=[
                ('OUTSIDE', 'Outside', '', '', 0),
                ('INSIDE', 'Inside', '', '', 1)
            ],
            description='Recalculation orientation'
        )

    auto_smooth: BoolProperty(
        name='Auto Smooth',
        default=True,
        description='Smoothes normals based of the angle'
    )

    auto_smooth_ang: FloatProperty(
        name='Max Angle',
        default=0.785398,
        subtype='ANGLE',
        description='Maximal angle between face normals that will be considered as smooth'
    )

    weighted_normals: BoolProperty(
        name='Weighted Normals',
        default=False
    )

    clear_custom_split_normals: BoolProperty(
        name='Custom Split Normals',
        default=True,
        description='Clears custom split normals if any available'
    )

    clear_sharp_edges: BoolProperty(
        name='Sharp Edges',
        default=True,
        description='Clears sharp edges i.a. resulting from custom split normals'
    )
    