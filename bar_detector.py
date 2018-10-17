######################################################################
# Author: Giorgi Lomia
# Username: lomiag
# #
# Assignment: Project 1
#
#Collection of functions used for barcode reading operations
######################################################################
from PIL import Image
from cv2 import *
import webbrowser
import playsound
from pyzbar.pyzbar import decode

def beep():
    playsound._playsoundWin("beep sound.wav")

def bar_decoder(file):
    """
    This function decodes the barcode from an image and returns a string with the number on it
    :param file: The image that needs to be read and decoded
    :return: A barcode number
    """
    #Decodes the barcode
    code=decode(Image.open(file))
    #Incese the scanner cannot read the image.
    if code != []:
        #Turns the byte type barcode into string
        the_code=code[0][0].decode()
    else:
        return None
    return the_code


import cv2
def check(file):
    """
    The function that checks if the frame has a barcode in it
    :param file: the file that needs to be checked
    :return: True or False
    """
    #Decoder
    code=decode((file))
    if code == []:
        #No Barcode
        return False
    #Yes Barcode
    return True
def webcam_capture(camera):
    """
    Function that takes video feed from the webcamera and checks frames for the presence of a barcode.
    as soon as a barcode is detected it takes a snapshot of the image and stores it as a file.
    :param camera: Camera that does the video taking
    :return:
    """
    #Live video feed

    while True:
        #Reading the video feed
        shape,frame=camera.read()
        if not shape:
            break
        #Normal Window
        color_scheme=cv2.cvtColor(frame, cv2.WINDOW_NORMAL)
        #What we see
        cv2.imshow('frame',color_scheme)
        #Live barcode detection
        detection=check(frame)
        #Barcode detected
        if detection==True:
            #Saving an image with the barcode
            beep()
            cv2.imwrite("Product.png",frame)
            #Stop Video Feed
            break
        #Manual Stop
        elif cv2.waitKey(1) & 0xFF == ord ("q"):
            break
    camera.release()
    cv2.destroyAllWindows()

def capture(camera,show=False):
    """
    Takes a picture of whatever webcam is filming. Mainly there for taking images with webcam.
    :param camera: Camera to be used
    :return:
    """
    sub, img = camera.read()


    if sub:    # frame captured without any errors
        #If the user wants to see the image they take
        if show == True:
            namedWindow("Product Barcode",cv2.WINDOW_NORMAL)
            imshow("Product Barcode",img)
        waitKey(0)
        destroyWindow("Product Barcode")
        name ="Product.png"
        imwrite(name,img) #save image


def web_browse(code):
    """
    Opens the product page in a web browser
    :param code: The barcode
    """
    webbrowser.open('https://www.barcodelookup.com/'+code)




