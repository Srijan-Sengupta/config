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



from .categories_pg import INSTANTCLEAN_PG_Categories
from .misc_pg import INSTANTCLEAN_PG_Misc
from .repair_pg import INSTANTCLEAN_PG_Repair_Settings
from .manifold_pg import INSTANTCLEAN_PG_ManifoldSettings
from .dissolve_pg import INSTANTCLEAN_PG_Dissolve_Settings
from .topology_pg import INSTANTCLEAN_PG_Topology_Settings
from .normals_pg import INSTANTCLEAN_PG_Normals_Settings
from .objectdata_pg import INSTANTCLEAN_PG_Objectdata_Settings


pgs_classes = {
    'instantclean_categories': INSTANTCLEAN_PG_Categories,
    'instantclean_misc': INSTANTCLEAN_PG_Misc,
    'instantclean_repair': INSTANTCLEAN_PG_Repair_Settings,
    'instantclean_manifold': INSTANTCLEAN_PG_ManifoldSettings,
    'instantclean_dissolve': INSTANTCLEAN_PG_Dissolve_Settings,
    'instantclean_topology': INSTANTCLEAN_PG_Topology_Settings,
    'instantclean_normals': INSTANTCLEAN_PG_Normals_Settings,
    'instantclean_objectdata': INSTANTCLEAN_PG_Objectdata_Settings
}

import bpy


def register():
    for pg, cls in pgs_classes.items():
        bpy.utils.register_class(cls)
        setattr(bpy.types.Scene, pg, bpy.props.PointerProperty(type=cls))
        

def unregister():
    for pg, cls in pgs_classes.items():
        delattr(bpy.types.Scene, pg)
        bpy.utils.unregister_class(cls)
