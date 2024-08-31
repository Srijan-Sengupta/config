import bpy
scene = bpy.context.scene

scene.render.fps = 25
scene.render.fps_base = 1.0
scene.render.pixel_aspect_x = 16.0
scene.render.pixel_aspect_y = 11.0
scene.render.resolution_percentage = 100
scene.render.resolution_x = 7680
scene.render.resolution_y = 4320
