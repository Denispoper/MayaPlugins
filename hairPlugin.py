import maya.cmds as mc
from maya import mel

class PolypaintToGuidelinesTool(object):

    def __init__(self):
        object.__init__(self)
        self.showWindow()

    if mc.window('PolypaintToGuidelines', exists=True):
        mc.deleteUI('PolypaintToGuidelines')

    def showWindow(self):
        myWindow = mc.window('PolypaintToGuidelines', width=300, height=100)
        mc.columnLayout()
        mc.button(label='Polypaint to curves', width=300, command=self.strokesToCurves)
        mc.separator()
        mc.button(label='Select Curves', width=300, command=self.selectCurves)
        mc.separator()
        mc.button(label='Clean up', width=300, command=self.cleanUp)
        mc.separator()
        mc.button(label='Activate live selection', width=300)
        mc.showWindow('PolypaintToGuidelines')

    def selectCurves(self, *args, **kwargs):
        curves1 = mc.ls('curve?')
        curves2 = mc.ls('curve??')
        curves = curves1 + curves2
        mc.group(curves)
        #return curves

    def strokesToCurves(self, *args, **kwargs):
        strokes1 = mc.ls('strokeDefaultBrush?')
        strokes2 = mc.ls('strokeDefaultBrush??')
        strokes = strokes1 + strokes2
        mc.select(strokes)
        mel.eval('PaintEffectsToCurve')

    def grouping(self, *args, **kwargs):
        curves = selectCurves()
        mc.group(curves)

    def cleanUp(self, *args, **kwargs):

        trash = ['strokeDefaultBrush*',
                'strokeShapeDefaultBrush*', 
                'curveDefaultBrush*',
                #'curveFromMeshCoM*',        
                #'DefaultBrush*'
        ]

        for element in trash:
            mc.delete(element)

    def polyPaintToCurves(self, *args, **kwargs):
        grouping()
        cleanUp()