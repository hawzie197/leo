# Author: Michael Hawes
# Project Leo
# image.py

import cv2
import twilio
import send_message as sm
import haven_on_demand



def get_image():

    """Global Variables"""
    ramp_frames = 1 # Number of frames to throw away
    camera = cv2.VideoCapture(0) # initialize camera // 0 index is the computer cam

    # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = camera.read()
    return im
    while True:
        for i in range(ramp_frames):
            temp = get_image()

    print("Taking image...")
    # Take the actual image we want to keep
    camera_capture = get_image()
    file = "image.jpg"
    cv2.imwrite(file, camera_capture) # write the photo to file
    return file
    del(camera)# release camera



def send_image(file):
    """Sends a photo over text"""
    sm.send_photo(file)




def find_companies_in_image(file):
    """recognizes company logos within a photo"""
    return havenondemand.getCompanyInImage(file)
