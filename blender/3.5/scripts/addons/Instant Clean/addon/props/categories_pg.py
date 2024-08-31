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
from bpy.props import BoolProperty


class INSTANTCLEAN_PG_Categories(bpy.types.PropertyGroup):
    repair: BoolProperty(
        name='Repair',
        default=True,
        description='Toggle Repair operations'
    )

    manifold: BoolProperty(
        name='Manifold',
        default=True,
        description='Toggle Manifold operations'
    )

    dissolve: BoolProperty(
        name='Dissolve',
        default=True,
        description='Toggle Dissolve operations'
    )

    topology: BoolProperty(
        name='Topology',
        default=True,
        description='Toggle Topology operations'
    )

    normals: BoolProperty(
        name='Normals',
        default=True,
        description='Toggle Normals operations'
    )

    objectdata: BoolProperty(
        name='Objectdata',
        default=True,
        description='Toggle Objectdata operations'
    )
