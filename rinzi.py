from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)

def setStepX(mc=mc, x=0, z=0, y=param.Y_SEA + 1, sizez=3, steps=3, inclination=1, Changex=-1, Changez=1, blockTypeId=param.IRON_BLOCK):
    # inclination = 1/n or n
    # ChangeX = 1 or -1
    if inclination > 1:
        high = steps * inclination
        sizez -= 1
        size = sizez * Changez
        while high > 0:
            ny = inclination
            nx = 1 // inclination
            mc.setBlocks(x, y, z, x, y - inclination, z + size, blockTypeId)
            x += Changex
            high -= ny
            y += ny

    if inclination < 1:
        high = steps
        sizez -= 1
        size = sizez * Changez
        while high > 0:
            ny = inclination
            nx = 1 // inclination
            mc.setBlocks(x, y, z, x + (nx * Changex), y, z + size, blockTypeId)
            x += (Changex * nx)
            high -= 1
            y += 1

    if inclination == 1:
        def setStep(mc=mc, x=0, z=0, y=param.Y_SEA + 1, size=3, high=3,  blockTypeId=param.IRON_BLOCK):
            size -= 1
            mc.setBlocks(x, y + high - 1, z, (x - high) + 1, y + high, z + size, param.AIR)
            mc.setBlocks(x, (y + high) - 2, z, (x - high) + 2, (y + high) - 1, z + size, param.AIR)
            while high > 0:
                mc.setBlocks(x, y, z, x, y - 1, z + size, blockTypeId)
                x -= 1
                high -= 1
                y += 1
        high = steps
        size = sizez * Changez
        setStep(x, z, y, size, high,  blockTypeId)
    
    sleep(0.01)


setStepX(mc=mc, x=45, z=-15, y=param.Y_SEA + 1, sizez=5, steps=5, inclination= (1 / 2), Changex=1, Changez=1, blockTypeId=param.IRON_BLOCK)

def setStepZ(mc=mc, x=0, z=0, y=param.Y_SEA + 1, sizex=3, steps=3, inclination=1, Changex=-1, Changez=1, blockTypeId=param.IRON_BLOCK):
    # inclination = 1/n or n
    # Changez = 1 or -1
    if inclination > 1:
        high = steps * inclination
        sizex -= 1
        size = sizex * Changex
        while high > 0:
            ny = inclination
            nz = 1 // inclination
            mc.setBlocks(x, y, z, x + size, y - inclination, z, blockTypeId)
            z += Changez
            high -= ny
            y += ny

    if inclination < 1:
        high = steps
        sizex -= 1
        size = sizex * Changez
        while high > 0:
            ny = inclination
            nz = 1 // inclination
            mc.setBlocks(x, y, z + size, x, y, z + (nz * Changex), blockTypeId)
            z += (Changez * nz)
            high -= 1
            y += 1

    if inclination == 1:
        def setStep(mc=mc, x=0, z=0, y=param.Y_SEA + 1, size=3, high=3,  blockTypeId=param.IRON_BLOCK):
            size -= 1
            mc.setBlocks(x, y + high - 1, z, x + size, y + high, (z - high) + 1, param.AIR)
            mc.setBlocks(x, (y + high) - 2, z, x + size, (y + high) - 1, (z - high) + 2, param.AIR)
            while high > 0:
                mc.setBlocks(x, y, z, x + size, y - 1, z, blockTypeId)
                z -= 1
                high -= 1
                y += 1
        high = steps
        size = sizex * Changex
        setStep(x, z, y, size, high,  blockTypeId)
    
    sleep(0.01)
