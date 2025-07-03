from direct.showbase.ShowBase import ShowBase
import defensepaths as defensepaths
import spacegameclasses as spacegameclasses



class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)


        self.Universe = spacegameclasses.Universe(self.loader, "./Assets/universe/Universe/Universe.x", self.render, 'Universe', "./Assets/universe/Universe/starfield-in-blue.jpg", (0, 0, 0), 15000)
        self.Planet1 = spacegameclasses.Planet(self.loader, "./Assets/planets/protoPlanet.x", self.render, 'Planet1', "./Assets/planets/planetOne.jpg", (150, 5000, 67), 350)
        self.Planet2 = spacegameclasses.Planet(self.loader, "./Assets/planets/protoPlanet.x", self.render, 'Planet2', "./Assets/planets/planetTwo.jpg", (3150, 7830, 492), 700)
        self.Planet3 = spacegameclasses.Planet(self.loader, "./Assets/planets/protoPlanet.x", self.render, 'Planet3', "./Assets/planets/planetThree.jpg", (11111, 7644, 9974), 3256)
        self.Planet4 = spacegameclasses.Planet(self.loader, "./Assets/planets/protoPlanet.x", self.render, 'Planet4', "./Assets/planets/planetFour.jpg", (5892, 123, 3945), 2718)
        self.Planet5 = spacegameclasses.Planet(self.loader, "./Assets/planets/protoPlanet.x", self.render, 'Planet5', "./Assets/planets/planetFive.jpg", (132, 8765, 393), 470)
        self.Planet6 = spacegameclasses.Planet(self.loader, "./Assets/planets/protoPlanet.x", self.render, 'Planet6', "./Assets/planets/planetSix.jpg", (111, 1111, 111), 111)
        self.SpaceStation1 = spacegameclasses.SpaceStation(self.loader, "./Assets/space station/SpaceStation1B/spaceStation.x", self.render, 'SpaceStation', "./Assets/space station/SpaceStation1B/SpaceStation1_Dif2.png", (2654, 2222, 4111), 75)
        self.playerShip = spacegameclasses.PlayerShip(self.loader, "./Assets/spaceships/Dumbledore/Dumbledore.x", self.render, 'PlayerShip', "./Assets/spaceships/Dumbledore/spacejet_C.png", (10, 10, 10), 5)
        self.drone = spacegameclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, 'Drone', "./Assets/DroneDefender/octotoad1_auv.png", (0, 0, 0), 5 )

    def DrawBaseBallSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        unitVec = defensepaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 250 + centralObject.modelNode.getPos()
        spacegameclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 5)
    def DrawCloudDefense(self, centralObject, droneName):
        unitVec = defensepaths.Cloud()
        unitVec.normalize()
        position = unitVec * 500 + centralObject.modelNode.getPos()
        spacegameclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)
    # def CircleDefenseX(self, centralObject, droneName):
    #     unitVec = defensepaths.CircleDefense(unitVec)
    #     unitVec.normalize()
    #     position = unitVec * 500 + centralObject.modelNode.getPos()
    #     spacegameclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)




        fullCycle = 60

        for j in range(fullCycle):
            spacegameclasses.Drone.droneCount += 1
            nickName = "Drone" + str(spacegameclasses.Drone.droneCount)
            
            self.DrawCloudDefense(self.Planet1, nickName)
            self.DrawBaseBallSeams(self.SpaceStation1, nickName, j, fullCycle, 2)
            













        # adds universe model and texture

        # self.Universe = self.loader.loadModel("./Assets/universe/Universe/Universe.x")
        # self.Universe.reparentTo(self.render)
        # self.Universe.setScale(15000)
        # texUni = self.loader.loadTexture("./Assets/universe/Universe/starfield-in-blue.jpg")
        # self.Universe.setTexture(texUni, 1)

        # adds planet model and texture



        # #planet1
        # self.Planet1 = self.loader.loadModel("./Assets/planets/protoPlanet.x")
        # self.Planet1.reparentTo(self.render)
        # self.Planet1.setPos(150, 5000, 67)
        # self.Planet1.setScale(350)
        # texPlanOne = self.loader.loadTexture("./Assets/planets/planetOne.jpg")
        # self.Planet1.setTexture(texPlanOne, 1)
        # #planet2
        # self.Planet2 = self.loader.loadModel("./Assets/planets/protoPlanet.x")
        # self.Planet2.reparentTo(self.render)
        # self.Planet2.setPos(3150, 7830, 492)
        # self.Planet2.setScale(700)
        # texPlanTwo = self.loader.loadTexture("./Assets/planets/planetTwo.jpg")
        # self.Planet2.setTexture(texPlanTwo, 1)
        # #planet3
        # self.Planet3 = self.loader.loadModel("./Assets/planets/protoPlanet.x")
        # self.Planet3.reparentTo(self.render)
        # self.Planet3.setPos(11111, 7644, 9974)
        # self.Planet3.setScale(3256)
        # texPlanThree = self.loader.loadTexture("./Assets/planets/planetThree.jpg")
        # self.Planet3.setTexture(texPlanThree, 1)
        # #planet4
        # self.Planet4 = self.loader.loadModel("./Assets/planets/protoPlanet.x")
        # self.Planet4.reparentTo(self.render)
        # self.Planet4.setPos(5892, 123, 3945)
        # self.Planet4.setScale(2718)
        # texPlanFour = self.loader.loadTexture("./Assets/planets/planetFour.jpg")
        # self.Planet4.setTexture(texPlanFour, 1)
        # #planet5
        # self.Planet5 = self.loader.loadModel("./Assets/planets/protoPlanet.x")
        # self.Planet5.reparentTo(self.render)
        # self.Planet5.setPos(132, 8765, 393)
        # self.Planet5.setScale(470)
        # texPlanFive = self.loader.loadTexture("./Assets/planets/planetFive.jpg")
        # self.Planet5.setTexture(texPlanFive, 1)
        # #planet6
        # self.Planet6 = self.loader.loadModel("./Assets/planets/protoPlanet.x")
        # self.Planet6.reparentTo(self.render)
        # self.Planet6.setPos(111, 1111, 111)
        # self.Planet6.setScale(111)
        # texPlanSix = self.loader.loadTexture("./Assets/planets/planetSix.jpg")
        # self.Planet6.setTexture(texPlanSix, 1)      
        
        # #spaceshuttle
        # self.playerShip = self.loader.loadModel("./Assets/spaceships/Dumbledore/Dumbledore.x")
        # self.playerShip.reparentTo(self.render)
        # self.playerShip.setPos(10, 10, 10)
        # self.playerShip.setScale(5)
        # texplayerShip = self.loader.loadTexture("./Assets/spaceships/Dumbledore/spacejet_C.png")
        # self.playerShip.setTexture(texplayerShip, 1)

        # #spacestation
        # self.spaceStation = self.loader.loadModel("./Assets/space station/SpaceStation1B/spaceStation.x")
        # self.spaceStation.reparentTo(self.render)
        # self.spaceStation.setPos(500, 250, 75)
        # self.spaceStation.setScale(75)
        # texspaceStation = self.loader.loadTexture("./Assets/space station/SpaceStation1B/SpaceStation1_Dif2.png")
        # self.spaceStation.setTexture(texspaceStation, 1)


    
app = MyApp()
app.run()    
