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


def sub_layout(layout: bpy.types.UILayout, space: float):
    row = layout.row(align=True)
    row.separator(factor=space)
    return row.column()


def sub_panel_header(layout: bpy.types.UILayout, category, text_only: bool):
        split = layout.split(align=True)
        col = split.column()
        row = col.row(align=True)
        row.ui_units_x = 6
        row.separator()
        if text_only:
            row.label(text=category.capitalize())
        else:
            row.prop(bpy.context.scene.instantclean_categories, category, toggle=True)
            row.operator('instantclean.clean', text='', icon='TRIA_RIGHT').action = category

def results_layout(layout: bpy.types.UILayout, stats):
    box = layout.box()
    split = box.split()
    col = split.column()
    col.enabled = False
    vals = split.column()
    for name, value in stats.items():
        if type(value) == type(False):
            continue
        col.label(text=name)
        row = vals.row()
        row.alignment = 'CENTER'
        row.separator(factor=1)
        row.label(text=str(value))

def popup_results(layout: bpy.types.UILayout, stats):
    sub = sub_layout(layout, 2)
    split = sub.split()
    col = split.column()
    col.enabled = False
    vals = split.column()
    for name, value in stats.items():
        if type(value) == type(False):
            continue
        col.label(text=name)
        row = vals.row()
        row.alignment = 'CENTER'
        row.separator(factor=1)
        row.label(text=str(value))
