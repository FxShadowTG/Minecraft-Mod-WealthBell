# -*- coding: utf-8 -*-

from mod.common.mod import Mod


@Mod.Binding(name="Script_NeteaseModY7ZRQU2F", version="0.0.1")
class Script_NeteaseModY7ZRQU2F(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModY7ZRQU2FServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModY7ZRQU2FServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModY7ZRQU2FClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModY7ZRQU2FClientDestroy(self):
        pass
