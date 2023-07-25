# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi

@Mod.Binding(name="WealthBellMod", version="0.0.1")
class WealthBellMod(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def WealthBellModServerInit(self):
        serverApi.RegisterSystem("WealthBellMod","WealthBellModServerSystem","WealthBellMod.WealthBellModServerSystem.WealthBellModServerSystem")
        print("服务注册成功")

    @Mod.DestroyServer()
    def WealthBellModServerDestroy(self):
        print("服务销毁成功")

    @Mod.InitClient()
    def WealthBellModClientInit(self):
        clientApi.RegisterSystem("WealthBellMod","WealthBellModClientSystem","WealthBellMod.WealthBellModClientSystem.WealthBellModClientSystem")
        print("客户注册成功")

    @Mod.DestroyClient()
    def WealthBellModClientDestroy(self):
        print("客户销毁成功")
