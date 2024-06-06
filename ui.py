import bpy
from .ops import data_transfer
    
def menu(self, context): #This is more advanced setup - it's a main menu which is attached to Blender's menus.
    layout = self.layout
    layout.menu("VIEW3D_MT_object_modqdatatransfer_menu", text='Data Transfer',)

class MODQDATATRANSFER_MT_menu(bpy.types.Menu): #This is a submenu which is attached to menu. Must be registered though.
    bl_idname = "VIEW3D_MT_object_modqdatatransfer_menu"
    bl_label = "Quick Data Transfer"
    
    def draw(self, context):
        layout = self.layout
        layout.operator(data_transfer.MODQDATATRANSFER_OT_MOD_data_transfer.bl_idname, )
        # You can add more items to the submenu if needed

def register():
    bpy.utils.register_class(MODQDATATRANSFER_MT_menu)
    bpy.types.VIEW3D_MT_object_context_menu.append(menu) # Appending our menu to the other menu.


def unregister():
    bpy.utils.unregister_class(MODQDATATRANSFER_MT_menu)
    bpy.types.VIEW3D_MT_object_context_menu.remove(menu)