import bpy

class MODQDATATRANSFER_OT_MOD_data_transfer(bpy.types.Operator):
    bl_idname = "modqdatatransfer.mod_data_transfer"
    bl_label = "Set Quick Data Transfer To Selected From Active"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.active_object and len(bpy.context.selected_objects) > 1
        # return context.area.type == 'VIEW_3D' and context.active_object and len(bpy.context.selected_objects)>1
    
    def execute(self, context):
    
        def set_data_transfer_modifier(obj, target):
            mod = obj.modifiers.new('','DATA_TRANSFER')
            mod.object = target
            mod.use_loop_data = True
            mod.data_types_loops = {'CUSTOM_NORMAL'}
            mod.loop_mapping = 'POLYINTERP_NEAREST'
        
        def get_selection():
            active_object = bpy.context.active_object
            selected_objects = bpy.context.selected_objects.copy()
            selected_objects.remove(active_object)
            return active_object, selected_objects

        def apply_modifier_to_selected(selection, target):
            for obj in selection:
                if obj.type != 'MESH':
                    continue
                set_data_transfer_modifier(obj, target)
                
        apply_modifier_to_selected(get_selection()[1], get_selection()[0])
        return {'FINISHED'}
            
