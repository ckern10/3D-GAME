from CollideObjectBase import SphereCollideObject
from panda3d.core import Loader, NodePath, Vec3
from direct.task.Task import TaskManager
from typing import Callable
from direct.task import Task
from direct.interval.LerpInterval import LerpFunc
from direct.particles.ParticleEffect import ParticleEffect
import re
from direct.gui.OnscreenImage import OnscreenImage
from CollideObjectBase import *
import spacegameclasses as spacegameclasses
from panda3d.core import CollisionHandlerEvent, CollisionTraverser

class PlayerShip(SphereCollideObject):

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float, whateverVariable, whateverAccept, whateverRender, traverser):

        super(PlayerShip, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 1)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.loader = loader

        self.taskMgr = whateverVariable

        self.accept = whateverAccept

        self.render = whateverRender

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

        self.reloadTime = .25
        self.missileDistance = 4000
        self.missileBay = 1

        self.taskMgr.add(self.CheckIntervals, 'checkMissiles', 34)

        self.cntExplode = 0
        self.explodeIntervals = {}

        self.traverser = CollisionTraverser
        
        self.handler = CollisionHandlerEvent()

        self.handler.addInPattern('into')
        self.accept('into', self.HandleInto)

        # self.handler.addInPattern('into')
        # self.accept('into', self.HandleInto)

    
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

        self.accept('r', self.Fire)

    def Thrust(self, keyDown):
        
        if keyDown:
            self.taskMgr.add(self.ApplyThrust, 'foward-thrust')
        else:
            self.taskMgr.remove('foward-thrust')

    def ApplyThrust(self, task):

        rate = 5

        trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()

        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)

        return task.cont
    
    def LeftTurn(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.ApplyLeftTurn, 'left-turn')
        else:
            self.taskMgr.remove('left-turn')
    
    def ApplyLeftTurn(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return task.cont

    def RightTurn(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.ApplyRightTurn, 'right-turn')
        else:
            self.taskMgr.remove('right-turn')

    def ApplyRightTurn(self, task):
        rate = -.5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return task.cont
    
    def LookUp(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.ApplyLookUp, 'look-up')
        else:
            self.taskMgr.remove('look-up')

    def ApplyLookUp(self, task):
        rate = .5
        self.modelNode.setP(self.modelNode.getP() + rate)
        return task.cont

    def LookDown(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.ApplyLookDown, 'look-down')
        else:
            self.taskMgr.remove('look-down')

    def ApplyLookDown(self, task):
        rate = -.5
        self.modelNode.setP(self.modelNode.getP() + rate)
        return task.cont
    
    def RollLeft(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.ApplyRollLeft, 'roll-left')
        else:
            self.taskMgr.remove('roll-left')

    def ApplyRollLeft(self, task):
        rate = -1
        self.modelNode.setR(self.modelNode.getR() + rate)
        return task.cont
    
    def RollRight(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.ApplyRollRight, 'roll-right')
        else:
            self.taskMgr.remove('roll-right')

    def ApplyRollRight(self, task):
        rate = 1
        self.modelNode.setR(self.modelNode.getR() + rate)
        return task.cont

    def Fire(self):
        if self.missileBay:
            travRate = self.missileDistance
            aim = self.render.getRelativeVector(self.modelNode, Vec3.forward())
            aim.normalize()

            fireSolution = aim * travRate
            inFront = aim * 150
            travVec = fireSolution + self.modelNode.getPos()
            self.missileBay -= 1
            tag = 'Missile' + str(spacegameclasses.Missile.missileCount)

            posVec = self.modelNode.getPos() + inFront
            currentMissile = spacegameclasses.Missile(self.loader, './Assets/Phaser/phaser.egg', self.render, tag, posVec, 4.0)
            #self.traverser.addCollider(currentMissile, self.handler)
            spacegameclasses.Missile.Intervals[tag] = currentMissile.modelNode.posInterval(2.0, travVec, startPos = posVec, fluid = 1)

            spacegameclasses.Missile.Intervals[tag].start()

        else:
            if not self.taskMgr.hasTaskNamed('reload'):
                print('Initializing Reload...')
                self.taskMgr.doMethodLater(0, self.Reload, 'reload')
        
        return Task.cont


    def Reload(self, task):
        if task.time > self.reloadTime:
            self.missileBay += 1
        if self.missileBay > 1:
            self.missileBay = 1
            print("Reload Complete.")
            return Task.done
        elif task.time < self.reloadTime:
            print ('Reload Proceeding...')
            return Task.cont
        
    def CheckIntervals(self, task):
        for i in spacegameclasses.Missile.Intervals:

            if not spacegameclasses.Missile.Intervals[i].isPlaying():

                spacegameclasses.Missile.cNodes[i].detachNode()
                spacegameclasses.Missile.fireModels[i].detachNode()

                del spacegameclasses.Missile.Intervals[i]
                del spacegameclasses.Missile.fireModels[i]
                del spacegameclasses.Missile.cNodes[i]
                del spacegameclasses.Missile.collisionSolids[i]

                print(i + ' has reached the end of its fire solution.')

                break
    
        return Task.cont

    def HandleInto(self, entry):
        fromNode = entry.getFromNodePath().getNode()
        print("fromNode: " + fromNode)
        intoNode = entry.getIntoNodePath().getName()
        print("intoNode: " + intoNode)

        intoPosition = Vec3(entry.getSurfacePoint(self.render))

        tempVar = fromNode.split('_')
        print('tempVar: ' + str(tempVar))
        shooter = tempVar[0]
        print('Shooter: ' + str(shooter))
        tempVar = intoNode.split('-')
        print('TempVar1: ' + str(tempVar))
        tempVar = intoNode.split('_')
        print('TempVar2: ' + str(tempVar))
        victim = tempVar[0]
        print('Victim: ' + str(victim))

        pattern = r'[0-9]'
        strippedString = re.sub(pattern, '', victim)

        if (strippedString == 'Drone' or strippedString == 'Planet' or strippedString == 'Space Station'):
            print(victim, 'hit at', intoPosition)
            self.DestroyObject(victim, intoPosition)

        print(shooter + 'is DONE.')
        spacegameclasses.Missile.Intervals[shooter].finish()

    def DestroyObject(self, hitID, hitPosition):
        nodeID = self.render.find(hitID)
        nodeID.detachNode()

        self.explodeNode.setPos(hitPosition)
        self.Explode()

    def Explode(self):
        self.cntExplode += 1
        tag = 'particles-' + str(self.cntExplode)

        self.explodeIntervals[tag] = LerpFunc(self.ExplodeLight, duration = 4.0)
        self.explodeIntervals[tag].start()

    def ExplodeLight(self, t):
        if t == 1.0 and self.explodeEffect:
            self.explodeEffect.disable()
        
        elif t == 0:
            self.explodeEffect.start(self.explodeNode)

    def SetParticles(self):
        base.enableParticles()
        self.explodeEffect = ParticleEffect()
        self.explodeEffect.loadConfig('./Assets/ParticleEffects/Explosions/basic_xpld_efx.ptf')
        self.explodeEffect.setScale(20)
        self.explodeNode = self.render.attachNewNode('ExplosionEffects')


    # def EnableHUD(self):
    #     self.Hud = OnscreenImage(image = '.Assets/Hud/Reticle3b.png', pos = Vec3(0, 0, 0), scale = 0.1)
    #     self.Hud.setTransparency(TransparencyAttrib.MAlpha)
    #     self.Hud.show()

    
