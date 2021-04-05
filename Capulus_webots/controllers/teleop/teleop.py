"""control_4_llantas controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Keyboard

# create the Robot instance.
robot = Robot()
keyboard=Keyboard()
# get the time step of the current world.
timestep = 64
keyboard.enable(timestep)

wheels=[]
wheelsNames=['wheel1','wheel2','wheel3','wheel4']

for i in range(4):
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)



ds=[]
dsNames=['ds_left','ds_right']

for i in range(2):
    ds.append(robot.getDevice(dsNames[i]))
    ds[i].enable(timestep)


avoidObstacleCounter=0


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    leftSpeed=0.0
    rightSpeed=0.0
    
    key=keyboard.getKey()
    print(key)
    if key ==87:
        leftSpeed=1.0
        rightSpeed=1.0
    elif key == 83:
        leftSpeed=-1.0
        rightSpeed=-1.0
    elif key==65:
        leftSpeed=-1.0
        rightSpeed=1.0
    elif key == 68:
        leftSpeed=1.0
        rightSpeed=-1.0

        
            
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
