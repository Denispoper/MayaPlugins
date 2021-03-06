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
        mc.button(label='Polypaint to curves', width=300, height=20, command=self.strokesToCurves)
        mc.separator()
        mc.button(label='Group Curves', width=300, height=20, command=self.grouping)
        mc.separator()
        mc.button(label='Clean up', width=300, height=20, command=self.cleanUp)
        mc.separator()
        mc.text(label='Select the sculp', align='center')
        mc.button(label='Activate live selection', width=300, height=20, command=self.activateLiveSelection)
        mc.showWindow('PolypaintToGuidelines')

    def selectCurves(self, *args, **kwargs):
        curves1 = mc.ls('curve?')
        curves2 = mc.ls('curve??')
        curves = curves1 + curves2
        return curves

    def strokesToCurves(self, *args, **kwargs):
        strokes1 = mc.ls('strokeDefaultBrush?')
        strokes2 = mc.ls('strokeDefaultBrush??')
        strokes = strokes1 + strokes2
        mc.select(strokes)
        mel.eval('PaintEffectsToCurve')

    def grouping(self, *args, **kwargs):
        curves = self.selectCurves()
        mc.group(curves, name='curveSet#')

    def cleanUp(self, *args, **kwargs):

        trash = ['strokeDefaultBrush*',
                'strokeShapeDefaultBrush*', 
                'curveDefaultBrush*',
                #'curveFromMeshCoM*',        
                #'DefaultBrush*'
        ]

        for element in trash:
            mc.delete(element)

    def activateLiveSelection(self, *args, **kwargs):
        mel.eval('statusLineSetMakeLive')
        curves = self.selectCurves()
        mc.select(curves)
        mel.eval('SelectCurveCVsFirst')