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
from bpy.props import (BoolProperty, IntProperty, FloatProperty)


def update(self, context):
    bpy.ops.ed.undo_push(message='Changed Setting')


class INSTANTCLEAN_PG_ManifoldSettings(bpy.types.PropertyGroup):
    non_manifold_faces: BoolProperty(
        name='Non-Manifold Faces',
        default=True,
        description='Faces with edges which are connected to more than two faces or are inside the mesh (e.g. interior faces)'
    )

    non_manifold_verts: BoolProperty(
        name='Non-Manifold Vertices',
        default=True,
        description='Splits vertices which are connecting two parts of a mesh in a zero size point'
    )

    wire_geo: BoolProperty(
        name='Wire Geometry',
        default=True,
        description='Geometry not consisting of any faces'
    )

    fill_holes: BoolProperty(
        name='Fill Holes',
        default=False,
        description='Fill up holes in the mesh',
    )

    fill_holes_max_sides: IntProperty(
        name='Max Sides',
        default=4,
        description='Fill only holes with up to this amount of sides',
    )

    flatten: BoolProperty(
        name='Flatten Faces',
        default=False,
        description='Flatten faces which vertices are not in the same plane by moving them to match an average plane'
    )

    flatten_iterations: IntProperty(
        name='Iterations',
        default=3,
        description='Repeat the flatten process this many times'
    )

    flatten_factor: FloatProperty(
        name='Factor',
        default=1.0,
        description='Determines how strong vertices will be moved to make all faces as flat as possible'
    )

    undistort: BoolProperty(
        name='Undistort Faces',
        default=False,
        description='Triangulate non-planar faces to create as many planar faces as possible'
    )

    undistort_ang: FloatProperty(
        name='Max Angle',
        subtype='ANGLE',
        default=0.087266,
        description='Only faces that are more distorted than this amount will be triangulated'
    )

    
