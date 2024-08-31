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


class INSTANTCLEAN_PG_Topology_Settings(bpy.types.PropertyGroup):
    type: EnumProperty(
        name='Type',
        items=[
            ('TRIS', 'Tris', '', 'MOD_TRIANGULATE', 0),
            ('QUADS', 'Quads', '', 'MOD_OPACITY', 1),
        ],
        default='TRIS',
        description='Type of topology which the mesh will be converted to'
    )

    # Methods
    quad_method: EnumProperty(
        name='Quad Method',
        items=[
            ('BEAUTY', 'Beauty', '', '', 0),
            ('FIXED', 'Fixed', '', '', 1),
            ('FIXED_ALTERNATE', 'Fixed Alternate', '', '', 2),
            ('SHORTEST_DIAGONAL', 'Shortest Diagonal', '', '', 3),
            ('LONGEST_DIAGONAL', 'Loneges Diagonal', '', '', 4),

        ],
        description='Method which will be used for the quad to triangle computation'
    )

    quad_max_face_ang: FloatProperty(
        name='Max Face Angle',
        subtype='ANGLE',
        default=0.698123,
        description='Dissolve only edges with lower angles to create quads'
    )

    quad_max_shape_ang: FloatProperty(
        name='Max Shape Angle',
        subtype='ANGLE',
        default=0.698123,
        description='Only try to convert to a quad if the overall shape change is lower than this angle'
    )

    ngon_method: EnumProperty(
        name='NGon Method',
        items=[
            ('BEAUTY', 'Beauty', '', '', 0),
            ('CLIP', 'Clip', '', '', 1),
        ],
        description='Method which will be used for the ngon to triangle computation'
    )

    # Compare
    compare_sharp: BoolProperty(
        name='Sharp',
        default=True,
        description='Excludes edges marked as sharp from the convertion'
    )

    compare_seam: BoolProperty(
        name='Seam',
        default=True,
        description='Excludes edges marked as seam from the convertion'
    )

    compare_vcol: BoolProperty(
        name='VCol',
        default=True,
        description='Leaves vertex colors unchanged after convertion'
    )

    compare_uv: BoolProperty(
        name='UV',
        default=True,
        description='Leaves uv\'s unchanged after convertion'
    )
    
    compare_material: BoolProperty(
        name='Material',
        default=True,
        description='Excludes edges which delimit two different assigned materials from the convertion'
    )
