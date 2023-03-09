from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
robotArm.moveRight() 
robotArm.grab()
i = 0
while i < 9:
    robotArm.moveRight()
i = i + 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()