from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task
from CollideObjectBase import *
from panda3d.core import CollisionHandlerEvent
from direct.interval.LerpInterval import LerpFunc
from direct.particles.ParticleEffect import ParticleEffect
import re
from direct.gui.OnscreenImage import OnscreenImage

class Universe(InverseSphereCollideObject):

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Universe, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 0.9)

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)


        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)


class Planet(SphereCollideObject):

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Planet, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 1.25)

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)


        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class Drone(SphereCollideObject):
    droneCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Drone, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 1.25)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)


        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        

class SpaceStation(CapsuleCollidableObject):

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(SpaceStation, self).__init__(loader, modelPath, parentNode, nodeName, 1, -1, 5, 1, -1, -5, 10)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)


        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class Missile(SphereCollideObject):

    fireModels = {}
    cNodes = {}
    collisionSolids = {}
    Intervals = {}
    missileCount = 0

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float = 1.0):
        super(Missile, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 3.0)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setPos(posVec)
        self.modelNode.setName(nodeName)

        Missile.missileCount += 1
        Missile.fireModels[nodeName] = self.modelNode
        Missile.cNodes[nodeName] = self.collisionNode

        Missile.collisionSolids[nodeName] = self.collisionNode.node().getSolid(0)
        Missile.cNodes[nodeName].show()

        print("Fire torpedo #" + str(Missile.missileCount))

# class Missile(SphereCollideObject):

#     fireModels = {}
#     cNodes = {}
#     collisionSolids = {}
#     Intervals = {}
#     missileCount = 0

#     def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float = 1.0):
#         super(Missile, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 3.0)
#         self.modelNode.setScale(scaleVec)
#         self.modelNode.setPos(posVec)

#         Missile.missileCount += 1
#         Missile.fireModels[nodeName] = self.modelNode
#         Missile.cNodes[nodeName] = self.collisionNode

#         Missile.collisionSolids[nodeName] = self.collisionNode.node().getSolid(0)
#         Missile.cNodes[nodeName].show()

#         print("Fire torpedo #" + str(Missile.missileCount))


#     def Fire(self): #: Loader):
#         self.loader = Loader
#         if self.missileBay:
#             travRate = self.missileDistance
#             aim = self.render.getRelativeVector(self.modelNode, Vec3.forward())
#             aim.normalize()

#             fireSolution = aim * travRate
#             inFront = aim * 150
#             travVec = fireSolution + self.modelNode.getPos()
#             self.missileBay -= 1
#             tag = 'Missile' + str(Missile.missileCount)

#             posVec = self.modelNode.getPos() + inFront
#             currentMissile = Missile(self.loader, './Assets/Phaser/phaser.egg', self.render, tag, posVec, 4.0)

#             Missile.Intervals[tag] = currentMissile.modelNode.posInterval(2.0, travVec, startPos = posVec, fluid = 1)

#             Missile.Intervals[tag].start()
#         else:
#             if not self.taskMgr.hasTaskNamed('reload'):
#                 print('Initializing Reload...')
#                 self.taskMgr.doMethodLater(0, self.Reload, 'reload')
#                 return Task.cont
        
#     def Reload(self, task):
#         if task.time > self.reloadTime:
#             self.missileBay += 1
#         if self.missileBay > 1:
#             self.missileBay = 1
#             print("Reload Complete.")
#             return Task.done
#         elif task.time < self.reloadTime:
#             print ('Reload Proceeding...')
#             return Task.cont
        
#     def CheckIntervals(self, task):
#         for i in Missile.Intervals:

#             if not Missile.Intervals[i].isPlayer():
#                 Missile.cNodes[i].detachNode()
#                 Missile.fireModels[i].detachNode()
#                 del Missile.Intervals[i]
#                 del Missile.fireModels[i]
#                 del Missile.cNodes[i]
#                 del Missile.collisionSolids[i]

#                 print(i + ' has reached the end of its fire solution.')

#                 break
#             return Task.cont
        
    # def EnableHUD(self):
    #     self.Hud = OnscreenImage(image = '.Assets/Hud/Reticle3b.png', pos = Vec3(0, 0, 0), scale = 0.1)
    #     self.Hud.setTransparency(TransparencyAttrib.MAlpha)
    #     self.Hud.show()
                
    

    

    




