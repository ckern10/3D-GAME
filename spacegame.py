from direct.showbase.ShowBase import ShowBase
import defensepaths as defensepaths
import spacegameclasses as spacegameclasses
import direct.task as Task
from panda3d.core import CollisionTraverser, CollisionHandlerPusher
import player as player


class MyApp(ShowBase):

    def __init__(self):

        ShowBase.__init__(self)

        self.SetScene()
        self.SetCamera()
        self.cTrav = CollisionTraverser()
        self.cTrav.traverse(self.render)
        self.pusher = CollisionHandlerPusher()
        self.pusher.addCollider(self.playerShip.collisionNode, self.playerShip.modelNode)
        self.cTrav.addCollider(self.playerShip.collisionNode, self.pusher)

        self.cTrav.showCollisions(self.render)

    def SetScene(self):

        self.Universe = spacegameclasses.Universe(self.loader, "./Assets/universe/Universe/Universe.x", self.render, 'Universe', "./Assets/universe/Universe/starfield-in-blue.jpg", (0, 0, 0), 15000)
        self.Planet4 = spacegameclasses.Planet(self.loader, "./Assets/planets/protoPlanet.x", self.render, 'Planet4', "./Assets/planets/planetFour.jpg", (5892, 123, 3945), 2718)
        self.Planet5 = spacegameclasses.Planet(self.loader, "./Assets/planets/protoPlanet.x", self.render, 'Planet5', "./Assets/planets/planetFive.jpg", (132, 8765, 393), 470)
        self.Planet6 = spacegameclasses.Planet(self.loader, "./Assets/planets/protoPlanet.x", self.render, 'Planet6', "./Assets/planets/planetSix.jpg", (111, 1111, 111), 111)
        self.SpaceStation1 = spacegameclasses.SpaceStation(self.loader, "./Assets/space station/SpaceStation1B/spaceStation.x", self.render, 'SpaceStation', "./Assets/space station/SpaceStation1B/SpaceStation1_Dif2.png", (2654, 2222, 4111), 75)

        self.Planet1 = spacegameclasses.Planet(self.loader, "./Assets/planets/protoPlanet.x", self.render, 'Planet1', "./Assets/planets/planetOne.jpg", (150, 5000, 67), 350)
        self.Planet2 = spacegameclasses.Planet(self.loader, "./Assets/planets/protoPlanet.x", self.render, 'Planet2', "./Assets/planets/planetTwo.jpg", (3150, 7830, 492), 700)
        self.Planet3 = spacegameclasses.Planet(self.loader, "./Assets/planets/protoPlanet.x", self.render, 'Planet3', "./Assets/planets/planetThree.jpg", (-971, -764, -9974), 3256)
        self.playerShip = player.PlayerShip(self.loader, "./Assets/spaceships/Dumbledore/Dumbledore.x", self.render, 'PlayerShip', "./Assets/spaceships/Dumbledore/spacejet_C.png", (10, 10, 10), 5, self.taskMgr, self.accept, self.render, CollisionTraverser)


        fullCycle = 60

        for j in range(fullCycle):
            spacegameclasses.Drone.droneCount += 1
            nickName = "Drone" + str(spacegameclasses.Drone.droneCount)

            self.DrawCloudDefense(self.Planet1, nickName)
            # self.DrawBaseBallSeams(self.Planet2, nickName, j, fullCycle, 2)
            self.DrawCircleDefenseX(self.Planet3, nickName)
            self.DrawCircleDefenseY(self.Planet3, nickName)
            self.DrawCircleDefenseZ(self.Planet3, nickName)

    def SetCamera(self):

        self.disableMouse()
        self.playerShip.SetKeyBindings()
        self.camera.reparentTo(self.playerShip.modelNode)
        self.camera.setFluidPos(0, 1, 0)

    # def DrawBaseBallSeams(self, centralObject, droneName, step, numSeams, radius = 1, l):
    #     unitVec = defensepaths.BaseballSeams(step, numSeams, B = 0.4)
    #     unitVec.normalize()
    #     position = unitVec * radius * 250 + centralObject.modelNode.getPos()
    #     spacegameclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 5)

    def DrawCloudDefense(self, centralObject, droneName):
        unitVec = defensepaths.Cloud()
        unitVec.normalize()
        position = unitVec * 500 + centralObject.modelNode.getPos()
        spacegameclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)

    def DrawCircleDefenseX(self, centralObject, droneName):
        unitVec = defensepaths.CircleDefenseX(self)
        unitVec.normalize()
        position = unitVec + centralObject.modelNode.getPos()
        spacegameclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 5)

    def DrawCircleDefenseY(self, centralObject, droneName):
        unitVec = defensepaths.CircleDefenseY(self)
        unitVec.normalize()
        position = unitVec + centralObject.modelNode.getPos()
        spacegameclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 5)

    def DrawCircleDefenseZ(self, centralObject, droneName):
        unitVec = defensepaths.CircleDefenseZ(self)
        unitVec.normalize()
        position = unitVec + centralObject.modelNode.getPos()
        spacegameclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 5)

    
app = MyApp()
app.run()    
