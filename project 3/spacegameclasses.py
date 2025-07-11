from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task

class Universe(ShowBase):

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)


class Planet(ShowBase):

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class Drone(ShowBase):
    droneCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)


class SpaceStation(ShowBase):

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class PlayerShip(ShowBase):

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):

        self.taskManager = Task
        
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

    def Thrust(self, keyDown):

        if keyDown:
            self.taskManager.add(self.ApplyThrust, 'foward-thrust')
        else:
            self.taskManager.remove('foward-thrust')

    def ApplyThrust(self):

        rate = 5

        trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()

        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)

        return Task.cont
    
    def SetKeyBindings(self):

        self.accept('space', self.Thrust, [1])
        self.accept('space-up', self.Thrust, [0])

        self.accept('a', self.LeftTurn, [1])
        self.accept('a-up', self.LeftTurn, [0])

        self.accept('d', self.RightTurn, [1])
        self.accept('d-up', self.RightTurn, [0])

        self.accept('w', self.LookUp, [1])
        self.accept('w-up', self.LookUp, [0])

        self.accept('s', self.LookDown, [1])
        self.accept('s-up', self.LookDown, [0])

        self.accept('q', self.RollLeft, [1])
        self.accept('q-up', self.RollLeft, [0])
        
        self.accept('e', self.RollRight, [1])
        self.accept('e-up', self.RollRight, [0])
    
    def LeftTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLeftTurn, 'left-turn')
        else:
            self.taskManager.remove('left-turn')
    
    def ApplyLeftTurn(self, Task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont

    def RightTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRightTurn, 'right-turn')
        else:
            self.taskManager.remove('right-turn')

    def ApplyRightTurn(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
    
    def LookUp(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLookUp, 'look-up')
        else:
            self.taskManager.remove('look-up')

    def ApplyLookUp(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont

    def LookDown(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLookDown, 'look-down')
        else:
            self.taskManager.remove('look-down')

    def ApplyLookDown(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
    
    def RollLeft(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRollLeft, 'roll-left')
        else:
            self.taskManager.remove('roll-left')

    def ApplyRollLeft(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
    
    def RollRight(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRollRight, 'roll-right')
        else:
            self.taskManager.remove('roll-right')

    def ApplyRollRight(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont





