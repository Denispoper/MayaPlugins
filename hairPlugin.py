import maya.cmds as mc
import test

def ui():
    if mc.window('Test', exists=True):
        mc.deleteUI('Test')
    
    myWindow = mc.window('Test')

    mc.columnLayout()
    mc.text(label = 'klafsdkfd')
    mc.button(command=test.selectCurves())
    mc.showWindow('Test')
    