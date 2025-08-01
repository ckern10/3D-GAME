import math, random
from panda3d.core import *

def Cloud(radius = 1):

    x = 2 * random.random() - 1
    y = 2 * random.random() - 1
    z = 2 * random.random() - 1

    unitVec = Vec3(x, y, z)
    unitVec.normalize()

    return unitVec * radius

# def BaseballSeams(step, numSeams, B, F = 1):

#     time = step / float(numSeams) * 2 * math.pi

#     F4 = 0

#     R = 1

#     xxx = math.cos(time) - B * math.cos(3 * time)
#     yyy = math.sin(time) + B * math.sin(3 * time)
#     zzz = F * math.cos(2 * time) + F4 * math.cos(4 * time)

#     rrr = math.sqrt(xxx ** 2 + yyy ** 2 + zzz ** 2)

#     x = R * xxx / rrr
#     y = R * yyy / rrr
#     z = R * zzz / rrr

#     return Vec3(x, y, z)

def CircleDefenseX(test):

    test.parent = test.loader.loadModel("./Assets/DroneDefender/DroneDefender.obj")

    x = 0

    for i in range(105):
        theta = x
        test.placeholder2 = test.render.attachNewNode('Placeholder2')
        test.placeholder2.setPos(150.0 * math.cos(theta), 150.0 * math.sin(theta), 0)
        test.parent.instanceTo(test.placeholder2)
        x = x + 0.06

    return Vec3(x)

def CircleDefenseY(test):

    test.parent = test.loader.loadModel("./Assets/DroneDefender/DroneDefender.obj")

    y = 0

    for i in range(105):
        theta = y
        test.placeholder2 = test.render.attachNewNode('Placeholder2')
        test.placeholder2.setPos(0, 150.0 * math.sin(theta), 150.0 * math.cos(theta))
        test.parent.instanceTo(test.placeholder2)
        y = y + 0.06

    return Vec3(y)

def CircleDefenseZ(test):

    test.parent = test.loader.loadModel("./Assets/DroneDefender/DroneDefender.obj")

    z = 0

    for i in range(105):
        theta = z
        test.placeholder2 = test.render.attachNewNode('Placeholder2')
        test.placeholder2.setPos(150.0 * math.cos(theta), 0, 150.0 * math.sin(theta))
        test.parent.instanceTo(test.placeholder2)
        z = z + 0.06

    return Vec3(z)
