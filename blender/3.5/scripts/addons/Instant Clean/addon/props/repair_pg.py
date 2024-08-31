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


def update(self, context):
    bpy.ops.ed.undo_push(message='Changed Setting')


class INSTANTCLEAN_PG_Repair_Settings(bpy.types.PropertyGroup):
    loose: BoolProperty(
        name='Loose',
        default=True,
        description='Unconnected Geometry',
        update=update
    )

    loose_verts: BoolProperty(
        name='Loose Verts',
        default=True,
        description='Vertices which are not part of an edge'
    )

    loose_edges: BoolProperty(
        name='Loose Edges',
        default=True,
        description='Edges which are not part of an face'
    )

    loose_faces: BoolProperty(
        name='Loose Faces',
        default=True,
        description='Faces which are not connected to other faces'
    )

    doubles: BoolProperty(
        name='Doubles',
        default=True,
        description='Vertices with the same position',
        update=update
    )

    doubles_dst: FloatProperty(
        name='Max Distance',
        default=0.0001,
        subtype='DISTANCE',
        description='Maximum Distance between positions to be considered as same'
    )

    zero_faces: BoolProperty(
        name='Zero Faces',
        default=True,
        description='Faces with an area of zero'
    )

    zero_faces_area: FloatProperty(
        name='Max Area',
        default=0.0001,
        subtype='DISTANCE',
        description='Maximum area of an face to be considered as zero'
    )

    dispensables: BoolProperty(
        name='Dispensables',
        default=True,
        description='Vertices which are connecting two edges by an angle of zero'
    )

    dispensables_ang: FloatProperty(
        name='Max Angle',
        default=0.0875,
        subtype='ANGLE',
        description='Maximum angle between two edges to be considered as zero'
    )