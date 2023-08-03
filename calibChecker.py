#IMPORTS
import sys
import cv2 as cv

sys.path.insert(0, "../../library")
import racecar_core
import racecar_utils as rc_utils

import utilChecker
#GLOBAL VARIABLES
rc = racecar_core.create_racecar()

#FUNCTIONS

def start():
    print("<< Sensor Checker >>")

def update():
    color_image = rc.camera.get_color_image()
    lidarScan = rc.lidar.get_samples()

    utilChecker = utilChecker.utilShower()

    print(utilChecker.camChecker(color_image))
    print(utilChecker.lidarChecker(lidarScan))

#BEGINS EXECUTION
if __name__ == "__main__":
    rc.set_start_update(start, update, None)
    rc.go()