# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi
from math import floor
ServerSystem = serverApi.GetServerSystemCls()
factory = serverApi.GetEngineCompFactory()
      
class WealthBellModServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        self.ListenEvent()
        print("加载监听ing")
        print("加载监听ok")
        self.compCreateBlockUseEventWhiteList = factory.CreateBlockUseEventWhiteList(self.levelId)
        self.compCreateBlockUseEventWhiteList.AddBlockItemListenForUseEvent("minecraft:bell:*")

    def ListenEvent(self):
        #获取levelId
        self.levelId = serverApi.GetLevelId()
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerBlockUseEvent', self, self.OnServerBlockUseEvent)
    
    def OnServerBlockUseEvent(self,args):
        if args["blockName"] != "minecraft:bell":
            return

        posX = args["x"]
        posY = args["y"]
        posZ = args["z"]
        playerId = args["playerId"]

        compCreateDimension = factory.CreateDimension(playerId)
        dimension = compCreateDimension.GetEntityDimensionId()

        compCreatePos = factory.CreatePos(playerId)
        playerIdPos = compCreatePos.GetFootPos()

        playerIdPosX = round(floor((playerIdPos[0])),0)
        playerIdPosY = round(floor((playerIdPos[1])),0)
        playerIdPosZ = round(floor((playerIdPos[2])),0)

        newPlayerPos = (playerIdPosX,playerIdPosY-1,playerIdPosZ)

        compCreateBlockInfo = factory.CreateBlockInfo(self.levelId)
        blockDict = compCreateBlockInfo.GetBlockNew(newPlayerPos, dimension)

        itemDict = {
            'itemName': blockDict['name'],
            'count': 1,
            'auxValue': blockDict['aux'],
        }

        compCreatePlayer = factory.CreatePlayer(playerId)
        is_sneaking = compCreatePlayer.isSneaking()

        if is_sneaking == True:
            itemDict['count'] = 5
            compCreateCommand = factory.CreateCommand(self.levelId)
            compCreateCommand.SetCommand("/playsound note.chime @s",playerId)
            compCreateCommand.SetCommand("/playsound note.chime @s 0",playerId)
            compCreateCommand.SetCommand("/playsound note.chime @s 1",playerId)
            compCreateCommand.SetCommand("/playsound note.chime @s 2",playerId)
            compCreateCommand.SetCommand("/playsound note.chime @s 3",playerId)

        self.CreateEngineItemEntity(itemDict, dimension, (posX,posY,posZ))

    def UnListenEvent(self):
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerBlockUseEvent', self, self.OnServerBlockUseEvent)

    def Destroy(self):
        self.UnListenEvent()
