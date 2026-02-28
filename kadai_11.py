from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('kadai #9  house')

mc.setBlocks(-90, param.Y_SEA + 1, -90,   -2, param.AXIS_TOP,    -2,    param.AIR)

def setPyramid(mc=mc, x=0, z=0, size=3, y=param.Y_SEA + 1, blockTypeId=param.GOLD_BLOCK):
    while size > 0:
        mc.setBlocks(x, y, z, x + size - 1, y, z + size - 1, blockTypeId)
        x += 1
        z += 1
        size -= 2
        y += 1
        sleep(0.01)

#setLoof
mc.postToChat('set Loof')
rx=-84, ry=19, rz=-84, rs=79
setPyramid(x=rx, z=-rz, y=param.Y_SEA + ry, size=rs, blockTypeId=param.IRON_BLOCK)
setPyramid(x=rx+1, z=-rz+1, y=param.Y_SEA + ry, size=rs-2, blockTypeId=param.SHROOMLIGHT)
setPyramid(x=rx+2, z=-rz+2, y=param.Y_SEA + ry, size=rs-4, blockTypeId=param.AIR)

#setFloor
mc.postToChat('set Floor')
sleep(0.01)
mc.postToChat('set 1st Floor')
fsx=81,fsy=1,fsz=81,ffx=9,ffy=10,ffz=9
mc.setBlocks(-fsx, param.Y_SEA + fsy, -fsz,   -ffx,  param.Y_SEA+ffy,      -ffz,     param.IRON_BLOCK)
mc.setBlocks(-fsx+2, param.Y_SEA + fsy+1, -fsz+2,   -ffx-2, param.Y_SEA+ffy-1,      -ffz-2,    param.AIR)
sleep(0.01)

mc.postToChat('set 2nd Floor')
mc.setBlocks(-fsx, param.Y_SEA + fsy+10, -fsz,   -ffx, param.Y_SEA+ffy+10,    -ffz,     param.IRON_BLOCK)
mc.setBlocks(-fsx+2, param.Y_SEA + fsy+11, -fsz+2,   -ffx-2, param.Y_SEA+ffy+9,    -ffz-2,    param.AIR)
sleep(0.01)

mc.postToChat('set 3rd Floor')
mc.setBlocks(-fsx+9, param.Y_SEA + fsy+20, -fsz+9,   -ffx-9, param.Y_SEA+ffy+20,    -ffz-9,    param.IRON_BLOCK)
mc.setBlocks(-fsx+11, param.Y_SEA + fsy+21, -fsz+11,   -ffx-11, param.Y_SEA+ffy+19,    -ffz-11,    param.AIR)
sleep(0.01)

mc.postToChat('set 4th Floor')
mc.setBlocks(-fsx+18, param.Y_SEA + fsy+30, -fsz+18,   -ffx-18, param.Y_SEA+ffy+30,    -ffz-18,    param.IRON_BLOCK)
mc.setBlocks(-fsx+20, param.Y_SEA + fsy+31, -fsz+20,   -ffx-20, param.Y_SEA+ffy+29,    -ffz-20,    param.AIR)
sleep(0.01)

mc.postToChat('set 5th Floor')
mc.setBlocks(-fsx+27, param.Y_SEA + fsy+40, -fsz+27,   -ffx-27, param.Y_SEA+ffy+40,    -ffz-27,    param.IRON_BLOCK)
mc.setBlocks(-fsx+29, param.Y_SEA + fsy+41, -fsz+29,   -ffx-29, param.Y_SEA+ffy+39,    -ffz-29,    param.AIR)
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
        
def setStepX(mc=mc, x=0, z=0, y=param.Y_SEA + 1, size=3, high=3, inclination=1, Changex=-1,  blockTypeId=param.IRON_BLOCK):
    # inclination = 1/n or n
    # ChangeX = 1 or -1
    while high > 0:
        ny = inclination
        nx = 1 // inclination
        mc.setBlocks(x, y, z, x, y, z + size, blockTypeId)
        x += nx ** Changex
        high -= ny
        y += ny
        sleep(0.01)

def setStepZ(mc=mc, x=0, z=0, y=param.Y_SEA + 1, size=3, high=3, inclination=1, Changez=-1,  blockTypeId=param.IRON_BLOCK):
    # inclination = 1/n or n
    # ChangeZ = 1 or -1
    while high > 0:
        ny = inclination
        nz = 1 // inclination
        mc.setBlocks(x, y, z, x + size, y, z, blockTypeId)
        z += nz ** Changez
        high -= ny
        y += ny
        sleep(0.01)

def setRoom(mc=mc, x=0, z=0, y=param.Y_SEA + 1, sizex = 1,sizey = 1,sizez = 1, blockTypeId=param.IRON_BLOCK):
    mc.setBlocks(x, y, z, x - sizex, y + sizey, z - sizez, blockTypeId)
    mc.setBlocks(x - 1, y + 1, z - 1, x - sizex + 1, y + sizey - 1, z - sizez + 1, param.AIR)
    sleep(0.01)

#setRoom
mc.postToChat('set Room')
mc.postToChat('set Room on first floor')
setRoom(x=-10, z=-10, y=param.Y_SEA + 1, sizex=9,  sizey=9, sizez=5,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-20, z=-10, y=param.Y_SEA + 1, sizex=55, sizey=9, sizez=5,  blockTypeId=param.SMOOTH_QUARTZ)
setRoom(x=-76, z=-10, y=param.Y_SEA + 1, sizex=4,  sizey=9, sizez=5,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-10, z=-21, y=param.Y_SEA + 1, sizex=14, sizey=9, sizez=20, blockTypeId=param.SMOOTH_QUARTZ)
sleep(0.01)
setRoom(x=-25, z=-21, y=param.Y_SEA + 1, sizex=9,  sizey=9, sizez=9,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-35, z=-21, y=param.Y_SEA + 1, sizex=9,  sizey=9, sizez=9,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-45, z=-21, y=param.Y_SEA + 1, sizex=14, sizey=9, sizez=14, blockTypeId=param.IRON_BLOCK)
setRoom(x=-60, z=-21, y=param.Y_SEA + 1, sizex=20, sizey=9, sizez=20, blockTypeId=param.SMOOTH_QUARTZ)
sleep(0.01)
setRoom(x=-25, z=-31, y=param.Y_SEA + 1, sizex=9,  sizey=9, sizez=10, blockTypeId=param.SMOOTH_QUARTZ)
setRoom(x=-35, z=-31, y=param.Y_SEA + 1, sizex=9,  sizey=9, sizez=10, blockTypeId=param.SMOOTH_QUARTZ)
setRoom(x=-45, z=-36, y=param.Y_SEA + 1, sizex=14, sizey=9, sizez=5,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-10, z=-47, y=param.Y_SEA + 1, sizex=15, sizey=9, sizez=27, blockTypeId=param.SMOOTH_QUARTZ)
sleep(0.01)
setRoom(x=-10, z=-75, y=param.Y_SEA + 1, sizex=15, sizey=9, sizez=5,  blockTypeId=param.SMOOTH_QUARTZ)
setRoom(x=-26, z=-47, y=param.Y_SEA + 1, sizex=20, sizey=9, sizez=33, blockTypeId=param.SMOOTH_QUARTZ)
setRoom(x=-47, z=-47, y=param.Y_SEA + 1, sizex=33, sizey=9, sizez=6,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-47, z=-54, y=param.Y_SEA + 1, sizex=33, sizey=9, sizez=6,  blockTypeId=param.IRON_BLOCK)
sleep(0.01)
setRoom(x=-47, z=-61, y=param.Y_SEA + 1, sizex=33, sizey=9, sizez=6,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-47, z=-68, y=param.Y_SEA + 1, sizex=33, sizey=9, sizez=6,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-47, z=-74, y=param.Y_SEA + 1, sizex=22, sizey=9, sizez=6,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-70, z=-74, y=param.Y_SEA + 1, sizex=10, sizey=9, sizez=6,  blockTypeId=param.SMOOTH_QUARTZ)
sleep(0.01)
mc.setBlocks(-72, param.Y_SEA + 2, -76, -79, param.Y_SEA + 7, -79, param.DIAMOND_BLOCK)
sleep(0.01)
mc.postToChat('set Room on second floor')
setRoom(x=-10, z=-66, y=param.Y_SEA + 11, sizex=20, sizey=9, sizez=14, blockTypeId=param.SMOOTH_QUARTZ)
setRoom(x=-10, z=-10, y=param.Y_SEA + 11, sizex=29, sizey=9, sizez=27, blockTypeId=param.IRON_BLOCK)
setRoom(x=-10, z=-38, y=param.Y_SEA + 11, sizex=29, sizey=9, sizez=27, blockTypeId=param.IRON_BLOCK)
setRoom(x=-10, z=-10, y=param.Y_SEA + 11, sizex=34, sizey=9, sizez=27, blockTypeId=param.IRON_BLOCK)
sleep(0.01)
setRoom(x=-45, z=-10, y=param.Y_SEA + 11, sizex=33, sizey=9, sizez=27, blockTypeId=param.IRON_BLOCK)
setRoom(x=-40, z=-38, y=param.Y_SEA + 11, sizex=40, sizey=9, sizez=42, blockTypeId=param.SMOOTH_QUARTZ)
setRoom(x=-31, z=-70, y=param.Y_SEA + 11, sizex=8,  sizey=9, sizez=10, blockTypeId=param.IRON_BLOCK)
sleep(0.01)
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

sleep(0.01)

mc.postToChat('You can get into this house')
