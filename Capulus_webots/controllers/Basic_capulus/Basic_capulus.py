"""control_4_llantas controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Keyboard

# create the Robot instance.
robot = Robot()
keyboard=Keyboard()
# get the time step of the current world.
timestep = 32

keyboard.enable(timestep)

wheels=[]
wheelsNames=['LEFT_MOTOR','RIGHT_MOTOR', 'LEFT_LINEAR', 'RIGHT_LINEAR','wheel_l1','wheel_l2','wheel_l3','wheel_l4','wheel_l5','wheel_r1','wheel_r2','wheel_r3','wheel_r4','wheel_r5']

for i in range(14):
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)




avoidObstacleCounter=0


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    leftSpeed=0.0
    rightSpeed=0.0
    leftTrack=0.0
    rightTrack=0.0
    key=keyboard.getKey()
    print(key)
    if key ==87:
        leftSpeed=1.0

    elif key == 83:
        leftSpeed=-1.0

    elif key==65:

        rightSpeed=1.0
    elif key == 68:

        rightSpeed=-1.0
    elif key==81:

        leftTrack=2.0
        rightTrack=-2.0
    elif key == 69:
        leftTrack=-2.0
        rightTrack=2.0

        
            
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(-leftTrack/20)
    wheels[3].setVelocity(rightTrack/20)
    wheels[4].setVelocity(leftTrack)
    wheels[5].setVelocity(leftTrack)
    wheels[6].setVelocity(leftTrack)
    wheels[7].setVelocity(leftTrack)
    wheels[8].setVelocity(leftTrack)
    wheels[9].setVelocity(rightTrack)
    wheels[10].setVelocity(rightTrack)
    wheels[11].setVelocity(rightTrack)
    wheels[12].setVelocity(rightTrack)
    wheels[13].setVelocity(rightTrack)
   
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
