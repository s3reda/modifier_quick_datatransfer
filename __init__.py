bl_info = {
    "name": "Modifier Quick Data Transfer",
    "author": "sereda",
    "version": (0, 0, 2),
    "blender": (4, 1, 0),
    "location": "Object mode Context menu.",
    "description": "",
    "warning": "",
    "doc_url": "",
    "category": "Modifier",
}

import bpy
from . import ops
from . import ui


_classes = [ops.data_transfer.MODQDATATRANSFER_OT_MOD_data_transfer, ]

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)
    ui.register()


def unregister():
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)
    ui.unregister()