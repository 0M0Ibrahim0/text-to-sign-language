from fbx import *

def MergLayers(pAnimLayer1, pAnimLayer2, pNode1, pNode2):
    MergChannels(pNode1, pNode2, pAnimLayer1, pAnimLayer2)

    for lModelCount in range(pNode1.GetChildCount()):
        MergLayers(pAnimLayer1, pAnimLayer2, pNode1.GetChild(lModelCount), pNode2.GetChild(lModelCount))

def MergChannels(pNode1, pNode2, pAnimLayer1, pAnimLayer2):
    lAnimCurve1 = None
    lAnimCurve2 = None

    KFCURVENODE_T_X = "X"
    KFCURVENODE_T_Y = "Y"
    KFCURVENODE_T_Z = "Z"

    KFCURVENODE_R_X = "X"
    KFCURVENODE_R_Y = "Y"
    KFCURVENODE_R_Z = "Z"
    KFCURVENODE_R_W = "W"

    KFCURVENODE_S_X = "X"
    KFCURVENODE_S_Y = "Y"
    KFCURVENODE_S_Z = "Z"

    # Merge general curves.
    lAnimCurve1 = pNode1.LclTranslation.GetCurve(pAnimLayer1, KFCURVENODE_T_X)
    lAnimCurve2 = pNode2.LclTranslation.GetCurve(pAnimLayer2, KFCURVENODE_T_X)
    if lAnimCurve2:
        MergCurve(lAnimCurve1, lAnimCurve2)
    lAnimCurve1 = pNode1.LclTranslation.GetCurve(pAnimLayer1, KFCURVENODE_T_Y)
    lAnimCurve2 = pNode2.LclTranslation.GetCurve(pAnimLayer2, KFCURVENODE_T_Y)
    if lAnimCurve2:
        MergCurve(lAnimCurve1, lAnimCurve2)
    lAnimCurve1 = pNode1.LclTranslation.GetCurve(pAnimLayer1, KFCURVENODE_T_Z)
    lAnimCurve2 = pNode2.LclTranslation.GetCurve(pAnimLayer2, KFCURVENODE_T_Z)
    if lAnimCurve2:
        MergCurve(lAnimCurve1, lAnimCurve2)

    lAnimCurve1 = pNode1.LclRotation.GetCurve(pAnimLayer1, KFCURVENODE_R_X)
    lAnimCurve2 = pNode2.LclRotation.GetCurve(pAnimLayer2, KFCURVENODE_R_X)
    if lAnimCurve2:
        MergCurve(lAnimCurve1, lAnimCurve2)
    lAnimCurve1 = pNode1.LclRotation.GetCurve(pAnimLayer1, KFCURVENODE_R_Y)
    lAnimCurve2 = pNode2.LclRotation.GetCurve(pAnimLayer2, KFCURVENODE_R_Y)
    if lAnimCurve2:
        MergCurve(lAnimCurve1, lAnimCurve2)
    lAnimCurve1 = pNode1.LclRotation.GetCurve(pAnimLayer1, KFCURVENODE_R_Z)
    lAnimCurve2 = pNode2.LclRotation.GetCurve(pAnimLayer2, KFCURVENODE_R_Z)
    if lAnimCurve2:
        MergCurve(lAnimCurve1, lAnimCurve2)
    lAnimCurve1 = pNode1.LclRotation.GetCurve(pAnimLayer1, KFCURVENODE_R_W)
    lAnimCurve2 = pNode2.LclRotation.GetCurve(pAnimLayer2, KFCURVENODE_R_W)
    if lAnimCurve2:
        MergCurve(lAnimCurve1, lAnimCurve2)

    lAnimCurve1 = pNode1.LclScaling.GetCurve(pAnimLayer1, KFCURVENODE_S_X)
    lAnimCurve2 = pNode2.LclScaling.GetCurve(pAnimLayer2, KFCURVENODE_S_X)
    if lAnimCurve2:
        MergCurve(lAnimCurve1, lAnimCurve2)
    lAnimCurve1 = pNode1.LclScaling.GetCurve(pAnimLayer1, KFCURVENODE_S_Y)
    lAnimCurve2 = pNode2.LclScaling.GetCurve(pAnimLayer2, KFCURVENODE_S_Y)
    if lAnimCurve2:
        MergCurve(lAnimCurve1, lAnimCurve2)
    lAnimCurve1 = pNode1.LclScaling.GetCurve(pAnimLayer1, KFCURVENODE_S_Z)
    lAnimCurve2 = pNode2.LclScaling.GetCurve(pAnimLayer2, KFCURVENODE_S_Z)
    if lAnimCurve2:
        MergCurve(lAnimCurve1, lAnimCurve2)

    # Merge curves specific to a light or marker.
    lNodeAttribute1 = pNode1.GetNodeAttribute()
    lNodeAttribute2 = pNode2.GetNodeAttribute()

    KFCURVENODE_COLOR_RED = "X"
    KFCURVENODE_COLOR_GREEN = "Y"
    KFCURVENODE_COLOR_BLUE = "Z"

    if lNodeAttribute2:
        lAnimCurve1 = lNodeAttribute1.Color.GetCurve(pAnimLayer1, KFCURVENODE_COLOR_RED)
        lAnimCurve2 = lNodeAttribute2.Color.GetCurve(pAnimLayer2, KFCURVENODE_COLOR_RED)
        if lAnimCurve2:
            MergCurve(lAnimCurve1, lAnimCurve2)
        lAnimCurve1 = lNodeAttribute1.Color.GetCurve(pAnimLayer1, KFCURVENODE_COLOR_GREEN)
        lAnimCurve2 = lNodeAttribute2.Color.GetCurve(pAnimLayer2, KFCURVENODE_COLOR_GREEN)
        if lAnimCurve2:
            MergCurve(lAnimCurve1, lAnimCurve2)
        lAnimCurve1 = lNodeAttribute1.Color.GetCurve(pAnimLayer1, KFCURVENODE_COLOR_BLUE)
        lAnimCurve2 = lNodeAttribute2.Color.GetCurve(pAnimLayer2, KFCURVENODE_COLOR_BLUE)
        if lAnimCurve2:
            MergCurve(lAnimCurve1, lAnimCurve2)

        # Merge curves specific to a light.
        light1 = pNode1.GetLight()
        light2 = pNode2.GetLight()
        if light2:
            lAnimCurve1 = light1.Intensity.GetCurve(pAnimLayer1)
            lAnimCurve2 = light2.Intensity.GetCurve(pAnimLayer2)
            if lAnimCurve2:
                MergCurve(lAnimCurve1, lAnimCurve2)

            lAnimCurve1 = light1.OuterAngle.GetCurve(pAnimLayer1)
            lAnimCurve2 = light2.OuterAngle.GetCurve(pAnimLayer2)
            if lAnimCurve2:
                MergCurve(lAnimCurve1, lAnimCurve2)

            lAnimCurve1 = light1.Fog.GetCurve(pAnimLayer1)
            lAnimCurve2 = light2.Fog.GetCurve(pAnimLayer2)
            if lAnimCurve2:
                MergCurve(lAnimCurve1, lAnimCurve2)

        # Merge curves specific to a camera.
        camera1 = pNode1.GetCamera()
        camera2 = pNode2.GetCamera()
        if camera2:
            lAnimCurve1 = camera1.FieldOfView.GetCurve(pAnimLayer1)
            lAnimCurve2 = camera2.FieldOfView.GetCurve(pAnimLayer2)
            if lAnimCurve2:
                MergCurve(lAnimCurve1, lAnimCurve2)

            lAnimCurve1 = camera1.FieldOfViewX.GetCurve(pAnimLayer1)
            lAnimCurve2 = camera2.FieldOfViewX.GetCurve(pAnimLayer2)
            if lAnimCurve2:
                MergCurve(lAnimCurve1, lAnimCurve2)

            lAnimCurve1 = camera1.FieldOfViewY.GetCurve(pAnimLayer1)
            lAnimCurve2 = camera2.FieldOfViewY.GetCurve(pAnimLayer2)
            if lAnimCurve2:
                MergCurve(lAnimCurve1, lAnimCurve2)

            lAnimCurve1 = camera1.OpticalCenterX.GetCurve(pAnimLayer1)
            lAnimCurve2 = camera2.OpticalCenterX.GetCurve(pAnimLayer2)
            if lAnimCurve2:
                MergCurve(lAnimCurve1, lAnimCurve2)

            lAnimCurve1 = camera1.OpticalCenterY.GetCurve(pAnimLayer1)
            lAnimCurve2 = camera2.OpticalCenterY.GetCurve(pAnimLayer2)
            if lAnimCurve2:
                MergCurve(lAnimCurve1, lAnimCurve2)

            lAnimCurve1 = camera1.Roll.GetCurve(pAnimLayer1)
            lAnimCurve2 = camera2.Roll.GetCurve(pAnimLayer2)
            if lAnimCurve2:
                MergCurve(lAnimCurve1, lAnimCurve2)

        # Merge curves specific to a geometry.
        '''if lNodeAttribute.GetAttributeType() == FbxNodeAttribute.eMesh or \
                lNodeAttribute.GetAttributeType() == FbxNodeAttribute.eNurbs or \
                lNodeAttribute.GetAttributeType() == FbxNodeAttribute.ePatch:
            lGeometry = lNodeAttribute

            lBlendShapeDeformerCount = lGeometry.GetDeformerCount(FbxDeformer.eBlendShape)
            for lBlendShapeIndex in range(lBlendShapeDeformerCount):
                lBlendShape = lGeometry.GetDeformer(lBlendShapeIndex, FbxDeformer.eBlendShape)
                lBlendShapeChannelCount = lBlendShape.GetBlendShapeChannelCount()
                for lChannelIndex in range(lBlendShapeChannelCount):
                    lChannel = lBlendShape.GetBlendShapeChannel(lChannelIndex)
                    lAnimCurve1 = lGeometry.GetShapeChannel(lBlendShapeIndex, lChannelIndex, pAnimLayer1, True)
                    lAnimCurve2 = lGeometry.GetShapeChannel(lBlendShapeIndex, lChannelIndex, pAnimLayer2, True)
                    if lAnimCurve2:
                        MergCurve(lAnimCurve1, lAnimCurve2)'''

def MergCurve(pCurve1, pCurve2):

    if pCurve1 == None:
        pCurve1 = pCurve2
    lKeyCount = pCurve2.KeyGetCount()
    lastKeyTime = 0
    if pCurve1:
        lastKeyTime = pCurve1.KeyGetTime(pCurve1.KeyGetCount() - 1)
    pCurve1.KeyModifyBegin()
    for lCount in range(lKeyCount):
        lKeyValue = pCurve2.KeyGetValue(lCount)
        lKeyTime = pCurve2.KeyGetTime(lCount)
        lKeyIndex = pCurve1.KeyAdd(lastKeyTime + lKeyTime)[0]
        pCurve1.KeySetValue(lKeyIndex, lKeyValue)
        pCurve1.KeySetInterpolation(lKeyIndex, pCurve2.KeyGetInterpolation(lCount))
    pCurve1.KeyModifyEnd()
