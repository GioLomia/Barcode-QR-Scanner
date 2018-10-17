# P01-Final Project.

## Motivation.
I am building this programm because I am facinated by computer vision and recognition software. I think it provides a good challenge and
offers a great learning experiance.

## Purpose.
My programm takes the live feed from the computer camera or a direct image or a barcode number and recognises barcode in it. After recognizing the barcode it reads it and opens
the product page in a web browser.

## Initial Design Plan.
I will create a class called Scanner. Its purpouse is to scan different types of data 
(such as image, string of numbers, live video feed) and find a barcode in it.
![alt files](https://github.com/spring-2018-csc-226/p01-final-project-lomiag_final_project/blob/master/CRC_card_Scanner.png "CRC card Scanner")
![alt files](https://github.com/spring-2018-csc-226/p01-final-project-lomiag_final_project/blob/master/CRC_card_GUI.png "CRC card GUI")
## Files

scanner.py-the scanner class.

test_suite.py-the test suite for the project. 

Final_Project.py-the compilation of all the files that brings everything together.

bar_detector.py-Supporting collection of functions used for Scanner class

a08_upc_start-the upc assignment that I used and expend uppon. 

barcode_o1.png-test image. 

QR_code_example.jpg-QR test image

CRC card Scanner-CRC card for the scanner class. 

CRC card GUI-CRC card for the GUI class. 

beep sound.wav-beeping sound 

README.md-readme file 

## Summary

I have been working on this project for dozens of hours. At first I wanted to only create one class called scanner, however thoughout development I realized that a user interface would be extremely useful. The biggest chalange was figuring out how to scan live video feed nad detecting a barcode in it, however after some time I was able to figure it out. Throughout development the fitures of the programm kept stocking up. I did not intend the programm to be able to read QR codes, or make a beeping sound after detecting a barcode however I thought it would make my project much better so decided to add it. 

I have encountered great many challenges during this project simply because I have never worked with computer vision before, however figuring out those problems was very satisfying.

## Video

https://youtu.be/_rwGjLD0HbA

## Instructions 

This app is very easy to use. When the app starts the user will see a screen infront of them that has an entry box and 5 buttons:"Number", "Image", "Live", "Close", "Help". Each of those buttons does the following.
"Number"- Before pressing it the user must put in a barcode number that needs to searched, then click it, after which the programm will find the product in the library.

"Image"- Allows the user to select an image from their computer and finds the barcode in it and opens its product page.

"Live"- Starts a webcam, the user can put a barcode in front of it and the page will be opened, after which the webcam will turn of, the camera can be turn off manually by pressing "q" on the keyboard, and closing the windows window that pops up afterwards.

"Close"- Closes the aplication.

"Help"- Provides helpful text to the user.

## Reflection

I have worked on my final project for a while now. Throughout my time working on it has brought me a lot of enjoynment. I had a lot of fun trying to figure out how to use computer vison and combine it with barcode recognition. It has being a challenging experience that enriched my knowledge of software development. I am planning on extend on my program in the future and perfect it.

## References

OpenCV library - https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html

playsound library - https://pypi.org/project/playsound/1.2.0/

pyzbar library - https://pypi.org/project/pyzbar/

PIL library - https://pillow.readthedocs.io/en/5.1.x/

Webcam capturing Stack overflow - https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv?rq=1

