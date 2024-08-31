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



from .main_panel import INSTANTCLEAN_PT_Main_Panel
from .repair_panel import INSTANTCLEAN_PT_Repair_Panel
from .manifold_panel import INSTANTCLEAN_PT_ManifoldPanel
from .dissolve_panel import INSTANTCLEAN_PT_Dissolve_Panel
from .topology_panel import INSTANTCLEAN_PT_Topology_Panel
from .normals_panel import INSTANTCLEAN_PT_Normals_Panel
from .objectdata_panel import INSTANTCLEAN_PT_Objectdata_Panel
from . import super_panel
from .super_panel import Super_Panel


classes = [
    INSTANTCLEAN_PT_Main_Panel,
    INSTANTCLEAN_PT_Repair_Panel,
    INSTANTCLEAN_PT_ManifoldPanel,
    INSTANTCLEAN_PT_Dissolve_Panel,
    INSTANTCLEAN_PT_Topology_Panel,
    INSTANTCLEAN_PT_Normals_Panel,
    INSTANTCLEAN_PT_Objectdata_Panel,
]

import bpy


def update_merge(merge):
    super_panel.set_merge(merge)
    unregister()
    register()


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)