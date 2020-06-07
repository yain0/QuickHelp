bl_info = {
    "name": "QuickHelp",
    "description": "",
    "author": "",
    "version": (0, 0, 2),
    "blender": (2, 70, 0),
    "location": "3D View > Tools",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "",
    "tracker_url": "",
    "category": "Development"
}

import bpy
import os
import csv
import urllib.request
import json
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Operator,
                       PropertyGroup,
                       )



# ------------------------------------------------------------------------
#    Scene Properties
# ------------------------------------------------------------------------

class MySettings(PropertyGroup):

    my_bool = BoolProperty(
        name="Enable or Disable",
        description="A bool property",
        default = False
        )

    my_int = IntProperty(
        name = "Int Value",
        description="A integer property",
        default = 23,
        min = 10,
        max = 100
        )

    my_float = FloatProperty(
        name = "Float Value",
        description = "A float property",
        default = 23.7,
        min = 0.01,
        max = 30.0
        )
    my_string3 = StringProperty(
        name="",
        description=":",
        default="",
        maxlen=1024,
        )

    my_string = StringProperty(
        name="Ввести описание",
        description=":",
        default="",
        maxlen=1024,
        )
    my_string2 = StringProperty(
        name="Горячие клавиши",
        description=":",
        default="",
        maxlen=1024,
        )

    my_enum = EnumProperty(
        name="Dropdown:",
        description="Apply Data to attribute.",
        items=[ ('OP1', "Option 1", ""),
                ('OP2', "Option 2", ""),
                ('OP3', "Option 3", ""),
               ]
        )

# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------
class WM_OT_Manual(bpy.types.Operator):
    bl_idname = "wm.manual"
    bl_label = "Руководство"
    def load_lines(path):
        with open(path, encoding="utf8") as file:
            for line in file:
                yield line.rstrip('\n')
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        # print the values to the console
        f = open('D:/manual.txt','r', encoding="utf8")
        k = f.readline(10000)
        bpy.context.scene.my_tool.my_string3 = k
        return {'FINISHED'}

class WM_OT_HelloWorld(bpy.types.Operator):
    bl_idname = "wm.hello_world"
    bl_label = "Получить подсказку"
    
    def load_lines(path):
        with open(path, encoding="utf8") as file:
            for line in file:
                yield line.rstrip('\n')
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        name = os.path.basename(r'C:\Users\yanai\PycharmProjects\Parser1\comands.txt')
        print(name)
        # print the values to the console
        print("Hello World")
        lines = os.path.basename(r'C:\Users\yanai\PycharmProjects\Parser1')
        #f = open('C:/Users/yanai/PycharmProjects/Parser1/comands.txt','r', encoding="utf8")
        #with open('C:/Users/yanai/PycharmProjects/Parser1/comands.txt', 'r', encoding='utf-8') as fin:
         ##   for line in fin:
          #      line.strip()
          #      bpy.context.scene.my_tool.my_string3 += line
          #      if bpy.context.scene.my_tool.my_string == line:
           #         bpy.context.scene.my_tool.my_string2 = line
        #f = open('C:/Users/yanai/PycharmProjects/Parser1/comands.txt','r', encoding="utf8")
        #f2 = open('C:/Users/yanai/PycharmProjects/Parser1/pars.csv','r', encoding="utf8")
        #with open('C:/Users/yanai/PycharmProjects/Parser1/pars.csv', newline='') as csvfile:
        #    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
         #   for row in spamreader:
         #       bpy.context.scene.my_tool.my_string3 == row
        response = urllib.request.urlopen('http://localhost/dashboard/comands.txt').read().decode('utf-8')
        #output = response.decode('utf-8')
        #response = urllib.urlopen(currURL)
        #json_obj = json.load(urllib.request.urlopen('http://localhost/dashboard/comands.txt').read().decode('UTF-8'))
        #lines = response.readlines()
        #bpy.context.scene.my_tool.my_string3 = response
        temp = response.splitlines()
        #bpy.context.scene.my_tool.my_string3 = temp
        k=0
        for line in temp:
            #bpy.context.scene.my_tool.my_string3 = line
            k+=1
            if bpy.context.scene.my_tool.my_string == line:
                bpy.context.scene.my_tool.my_string2 = temp[k-2]
        return {'FINISHED'}


# ------------------------------------------------------------------------
#    Menus
# ------------------------------------------------------------------------

class OBJECT_MT_CustomMenu(bpy.types.Menu):
    bl_idname = "object.custom_menu"
    bl_label = "Select"

    def draw(self, context):
        layout = self.layout

        # Built-in example operators
        layout.operator("object.select_all", text="Select/Deselect All").action = 'TOGGLE'
        layout.operator("object.select_all", text="Inverse").action = 'INVERT'
        layout.operator("object.select_random", text="Random")

# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------

class OBJECT_PT_CustomPanel(Panel):
    bl_idname = "object.custom_panel"
    bl_label = "QuickHelp"
    bl_space_type = "VIEW_3D"   
    bl_region_type = "TOOLS"    
    bl_category = "Tools"
    bl_context = "objectmode"   

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        layout.operator("wm.manual")
        layout.prop(mytool, "my_string3")
        layout.prop(mytool, "my_string")
        layout.operator("wm.hello_world")
        layout.prop(mytool, "my_string2")
        layout.separator()

# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------
def testing():
    text = rpy.context.scene.my_tool.my_string2
    messages.append(Message(text))
    # a = "['камера']"
    a = dfn[dfn.desc == text].name
    b = list(zip(a, a.index))
    print(list(zip(a, a.index)))
    return render_template('testing.html',b=b)


def register():
    bpy.utils.register_module(__name__)
    bpy.types.Scene.my_tool = PointerProperty(type=MySettings)

def unregister():
    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.my_tool

if __name__ == "__main__":
    register()