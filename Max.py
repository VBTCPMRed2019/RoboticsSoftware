from finch import Finch
from keyboard import is_pressed as press
from time import sleep
from random import uniform, randint



Max = Finch()

#This while statement checks for whether or not the finch's accelerators
#have moved in such a way that represents flipping over
while Max.acceleration()[2] > -0.7:
    #If the W key is pressed on a keyboard, both wheels accelerate forware
    if press('w'):
        Max.led(0,255,0)
        Max.wheels(1.5,1.5)
    #If the A key is pressed the left wheel accelerates backwards and the right wheel accelerates forwards
    #In order to turn left continuously until a new key is pressed
    elif press('a'):
        Max.led(0,0,255)
        Max.wheels(-1.5,1.5)
    #The S key makes it so both finch wheels accelerate backwards, going backwards
    elif press('s'):
        Max.led(255,0,0)
        Max.wheels(-1.5, -1.5)
    #If the D key is pressed the right wheel accelerates backwards and the left wheel accelerates forwards
    #In order to turn right continuously until a new key is pressed
    elif press('d'):
        Max.led(255,255,0)
        Max.wheels(1.5,-1.5)
    #Pressing Q on the keyboard will stop whatever movement action is currently in place for the finch
    elif press('q'):
        Max.led(255,255,255)
        Max.wheels(0,0)
    #Pressing X on the keyboard will close the finch application, thereby turning off the ability to recieve inputs
    elif press('x'):
        Max.close()
    #Pressing 1 on the keyboard will have the finch do a specific set of turns and moves to create a square shape, then stop
    elif press('1'):
        Max.wheels(1,1)
        sleep(1)
        Max.wheels(0,1)
        sleep(.5)
        Max.wheels(1,1)
        sleep(1)
        Max.wheels(0,1)
        sleep(.5)
        Max.wheels(1,1)
        sleep(1)
        Max.wheels(0,1)
        sleep(.5)
        Max.wheels(1,1)
        sleep(1)
        Max.wheels(0,1)
        sleep(.5)
        Max.wheels(1,1)
        Max.wheels(0,0)
    #Pressing 2 will have the finch move in a circular motion for a short period of time
    elif press('2'):
        for i in range(2880):
            Max.wheels(1,1)
            sleep(1/1440)
            Max.wheels(0,1)
            sleep(1/1440)
        Max.wheels(0,0)
    #Pressing R on the keyboard will generate a random motion for the finch, as well as a random nose color
    elif press('r'):
        Max.wheels(randint(-1,1),randint(-1,1))
        Max.led(randint(0,255),randint(0,255),randint(0,255))
