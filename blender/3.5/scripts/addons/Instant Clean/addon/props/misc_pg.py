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


class INSTANTCLEAN_PG_Misc(bpy.types.PropertyGroup):
    results: BoolProperty(
        name=''
    )

    selected_only: BoolProperty(
        name='Selection Only',
        default=False,
        description='Execute all operations only for the current selection'
    )