from FbxCommon import *
from MergAnimation import *

def GenerateAnimation(seq):
    SdkManager, Scene = InitializeSdkObjects()
    Result = LoadScene(SdkManager, Scene, "Animation/" + str(seq[0]%41) + ".FBX")
    AnimStack = Scene.GetSrcObject(FbxCriteria.ObjectType(FbxAnimStack.ClassId), 0)
    AnimLayer = AnimStack.GetSrcObject(FbxCriteria.ObjectType(FbxAnimLayer.ClassId), 0)
    for i in range(1, len(seq)):
        SdkManageri, Scenei = InitializeSdkObjects()
        Resulti = LoadScene(SdkManageri, Scenei, "Animation/" + str(seq[i]%41) + ".FBX")
        AnimStacki = Scenei.GetSrcObject(FbxCriteria.ObjectType(FbxAnimStack.ClassId), 0)
        AnimLayeri = AnimStacki.GetSrcObject(FbxCriteria.ObjectType(FbxAnimLayer.ClassId), 0)
        MergLayers(AnimLayer, AnimLayeri, Scene.GetRootNode(), Scenei.GetRootNode())
    newStack = FbxAnimStack.Create(Scene, "Output Sequence")
    newStack.AddMember(AnimLayer)
    Scene.RemoveMember(AnimStack)
    SaveScene(SdkManager, Scene, "Output.FBX")