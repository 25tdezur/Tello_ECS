from djitellopy import tello
from time import sleep

ginger = tello.Tello()
ginger.connect()
print(ginger.get_battery())
ginger.takeoff()

# Starting point
ginger.move_up(95)
ginger.move_forward(500)
sleep(1)

# Changing direction to the "Must fly zone"
ginger.rotate_clockwise(270)
ginger.move_forward(325)
sleep(1)


ginger.rotate_clockwise(270)
ginger.move_forward(300)
ginger.rotate_clockwise(270)

# end of flying
sleep(1)

ginger.land()
