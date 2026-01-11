#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
left_drive_smart = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
right_drive_smart = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
#   Project:      5 PATH
#   Author:       PRATIK NOOKALA
#   Created:
#   Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *
# BRAIN
brain = Brain()
# CONTROLLER
controller = Controller()
# MOTORS
left_motor  = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)

def drive_mm(distance_mm, speed=50):

    wheel_diameter_mm = 101.6
    wheel_circumference = 3.1416 * wheel_diameter_mm
    degrees = (distance_mm / wheel_circumference) * 360

    left_motor.spin_for(FORWARD, degrees, DEGREES, speed, PERCENT)
    right_motor.spin_for(FORWARD, degrees, DEGREES, speed, PERCENT)

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("Auto running")
    start_time = brain.timer.time()  
    global screen_precision
    drivetrain.set_drive_velocity(100, PERCENT)
    intake_motor.set_velocity(100, PERCENT)
    conveyor_motor.set_velocity(100, PERCENT)
    drivetrain.turn_for(RIGHT, 60, DEGREES)
    drivetrain.drive_for(FORWARD, 950, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 50, MM)
    drivetrain.drive_for(REVERSE, 565, MM)
    conveyor_motor.spin(FORWARD)
    wait(3, SECONDS)
    conveyor_motor.stop()
    drivetrain.drive_for(FORWARD, 650, MM)
    conveyor_motor.set_velocity(10, PERCENT)
    conveyor_motor.spin(FORWARD)
    intake_motor.spin(FORWARD)
    wait(5.5, SECONDS)
    conveyor_motor.stop()
    intake_motor.stop()
    drivetrain.drive_for(REVERSE, 650, MM)
    conveyor_motor.set_velocity(100, PERCENT)
    conveyor_motor.spin(FORWARD)
    wait(4, SECONDS)
    conveyor_motor.stop()
   
    def time_left():
        return brain.timer.time() - start_time < 15
    
    if not time_left():
        stop_all_motors()
        return
    
    set_drive_velocity(100)
    intake_motor.set_velocity(100, PERCENT)
    conveyor_motor.set_velocity(100, PERCENT)
    
