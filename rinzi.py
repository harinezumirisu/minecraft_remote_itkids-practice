from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)

def setRoom(mc=mc, x=0, z=0, y=param.Y_SEA + 1, sizex = 1,sizey = 1,sizez = 1, blockTypeId=param.IRON_BLOCK):
    mc.setBlocks(x, y, z, x - sizex, y + sizey, z - sizez, blockTypeId)
    mc.setBlocks(x - 1, y + 1, z - 1, x - sizex + 1, y + sizey - 1, z - sizez + 1, param.AIR)
    sleep(0.01)

def setStep(mc=mc, x=0, z=0, y=param.Y_SEA + 1, size=3, high=3,  blockTypeId=param.IRON_BLOCK):
    # inclination = 1/n or n
    # ChangeX = 1 or -1
    size -= 1
    mc.setBlocks(x, y + high - 1, z, (x - high) + 1, y + high, z + size, param.AIR)
    mc.setBlocks(x, (y + high) - 2, z, (x - high) + 2, (y + high) - 1, z + size, param.AIR)
    while high > 0:
        mc.setBlocks(x, y, z, x, y, z + size, blockTypeId)
        x -= 1
        high -= 1
        y += 1
        sleep(0.01)

#setRoom
mc.postToChat('set Room')
mc.postToChat('set Room on third floor')
setRoom(x=-19, z=-57, y=param.Y_SEA + 21, sizex=20,  sizey=9, sizez=14, blockTypeId=param.SMOOTH_QUARTZ)
sleep(0.01)

#setFlooring
mc.postToChat('set Flooring')
mc.setBlocks(-79, param.Y_SEA + 1, -79,   -11, param.Y_SEA+1,    -11,    param.SHROOMLIGHT)
sleep(0.01)
mc.setBlocks(-79, param.Y_SEA + 11, -79,   -11, param.Y_SEA+11,    -11,    param.SHROOMLIGHT)
sleep(0.01)
mc.setBlocks(-79, param.Y_SEA + 21, -79,   -11, param.Y_SEA+21,    -11,    param.SHROOMLIGHT)
sleep(0.01)
mc.setBlocks(-71, param.Y_SEA + 31, -71,   -19, param.Y_SEA+31,    -19,    param.SHROOMLIGHT)
sleep(0.01)
mc.setBlocks(-62, param.Y_SEA + 41, -62,   -28, param.Y_SEA+41,    -28,    param.SHROOMLIGHT)
sleep(0.01)

#setStep
mc.postToChat('set steps')
setStep(x=-16, z=-79,y=param.Y_SEA +2, size=4, high=10, blockTypeId=param.SHROOMLIGHT)
sleep(0.01)
setStep(x=-20, z=-70,y=param.Y_SEA +11, size=4, high=10, blockTypeId=param.SHROOMLIGHT)
sleep(0.01)
setStep(x=-29, z=-61,y=param.Y_SEA +21, size=4, high=10, blockTypeId=param.SHROOMLIGHT)
sleep(0.01)
setStep(x=-38, z=-52,y=param.Y_SEA +31, size=4, high=10, blockTypeId=param.SHROOMLIGHT)
sleep(0.01)

mc.setBlocks(-9, param.Y_SEA + 2, -9,   -11, param.Y_SEA + 4,    -11,    param.AIR)

a = 9 ** -1

mc.setBlocks(a, param.Y_SEA + 2, -9,   -9, param.Y_SEA + 2,    -9,    param.GOLD_BLOCK)

sleep(0.01)

mc.postToChat('You can get into this house')
