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
from bpy.props import (BoolProperty, FloatProperty)


class INSTANTCLEAN_PG_Dissolve_Settings(bpy.types.PropertyGroup):
    max_angle: FloatProperty(
        name='Max Angle',
        default=0.0875,
        subtype='ANGLE',
        description='Maximum angle at which geometry will be dissolved'
    )

    boundaries: BoolProperty(
        name='Boundaries',
        description='Edges which are connected to one face only'
    )

    protect_sharp : BoolProperty(
        name='Sharp',
        default=True,
        description='Excludes edges marked as sharp from the dissolve'
    )

    protect_seam : BoolProperty(
        name='Seam',
        default=True,
        description='Excludes edges marked as seam from the dissolve'
    )

    protect_uv : BoolProperty(
        name='UV',
        default=True,
        description='Excludes edges which are boundary of UV islands from the dissolve'
    )

    protect_materials : BoolProperty(
        name='Materials',
        default=True,
        description='Excludes edges which delimit two different assigned materials from the dissolve'
    )