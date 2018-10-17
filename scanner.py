######################################################################
# Author: Giorgi Lomia
# Username: lomiag
# #
# Assignment: Project 1
#
#Class defenitiion of the Scanner and GUI classes
######################################################################
from a08_upc_start import *
from bar_detector import *
import tkinter
import tkinter.filedialog as filer
class Scanner:
    """
    This is a barcode scanner class that works as a scanner of different data types.
    """
    all_mods=["NUMBER","IMAGE","LIVE"]
    browse_mode=["ON","OFF"]
    def __init__(self,value_to_unpack="",on_off="ON",browser_mode_on_off="ON",qr_on_off="OFF",):


        self.mode = ""
        self.on_off = on_off
        self.value_to_unpack=str(value_to_unpack)
        self.barcode = ""
        self.browser = browser_mode_on_off
        self.qr_mode = qr_on_off

    def decode(self):
        """
        Decodes in different modes
        :return:
        """
        #If the scanner is ON
        #Number mode
        if self.mode=="NUMBER":
            #makes the barcode parameter of the class equal to the input plus the modulo
            return self.barcode
        #Image mode
        elif self.mode=="IMAGE":
            #Asks user for the image file to read until the file is actually in the library
                #catches the errors
            self.barcode=bar_decoder(self.value_to_unpack)
            if self.barcode.isalpha():
                self.qr_mode="ON"
           #Returns the barcode.
            return self.barcode
        #Live video feed mode
        elif self.mode=="LIVE":
            #Capturing video from the webcam and taking a photo in the right moment. For referance check the bar_detector.py
            webcam_capture(VideoCapture(0))
            try:
                #barcode from the image decoded
                self.barcode=bar_decoder("Product.png")
                os.remove("Product.png")
            except:
                self.barcode=""
            return self.barcode

    def decode_anything(self):
        """
        full final decoding
        :return: None
        """
        self.decode()
        if self.barcode != None:
            if self.barcode.isnumeric():
                self.qr_mode="OFF"
            else:
                self.qr_mode="ON"
            webbrowser.open(self.web_browse())

    def web_browse(self):
        """
        Opens the product page in a web browser
        :return: barcode
        """
        #If we are reading a regular barcode
        if self.qr_mode == "OFF" and self.browser=="ON":
            #If the scanner is on
            #Open the product page
            return 'https://www.barcodelookup.com/'+self.barcode
        else:
            #Print the code on the screen
            return self.barcode


class GUI:
    def __init__(self,master,scanner):
        """
        Definition of all the attributes of the GUI class
        :param master: The window that needs to be used
        :param scanner: The scanner that needs to be used
        """
    ##################Screen##################
        self.master = master
        self.scanner=scanner

        self.label = tkinter.Label(master, text="Barcode Number")
        self.label.pack()

        self.master.minsize(width=700, height=500)
        self.master.maxsize(width=1550, height=1100)
        self.master.title("Barcode Detective")
    ##################Interface###############
        #Number entry box
        self.number_box=tkinter.Entry()
        self.number_box.pack()
        #Number mode button
        self.number_button=tkinter.Button(self.master, text="Number", command=self.get_number)
        self.number_button.pack(padx=30,pady=10)
        #Image mode button
        self.image_button=tkinter.Button(self.master, text="Image", command=self.get_image)
        self.image_button.pack(padx=30,pady=10)
        #Live mode button
        self.live_button=tkinter.Button(self.master, text="Live", command=self.get_live)
        self.live_button.pack(padx=30,pady=10)
        #Close button
        self.close_button=tkinter.Button(self.master, text="Close", command=exit)
        self.close_button.pack(padx=30,pady=10)
        #Helper button
        self.help_button=tkinter.Button(self.master, text="Help", command=self.helper)
        self.help_button.pack(side="bottom")
        #Helping Text
        self.text_helper=tkinter.StringVar()
        self.words=tkinter.Label(master,textvariable=self.text_helper)
        self.words.pack()

    def get_number(self):
        """
        The function necessary for the number decoding
        :return: None
        """
        self.scanner.mode="NUMBER"
        self.scanner.barcode=self.number_box.get()
        self.text_helper.set("")
        checker=self.scanner.barcode[:11]
        if is_valid_input(self.scanner.barcode[:11]):
            if is_valid_modulo(checker)==self.scanner.barcode:
                self.scanner.decode_anything()
            else:
                self.text_helper.set("This Is an Invalid Barcode, Please Enter Again.")
        else:
            self.text_helper.set("Input Too Short, Please Enter Again")

    def get_image(self):
        """
        The function necessary for the image decoding
        :return: None
        """
        self.scanner.mode="IMAGE"
        self.text_helper.set("")
        try:
            self.scanner.value_to_unpack=filer.askopenfilename()
            self.scanner.decode_anything()
        except:
            self.text_helper.set("Invalid File, Please Select an Image to open")
    def get_live(self):
        """
        The function necessary for the live video decoding
        :return: None
        """
        self.scanner.mode="LIVE"
        self.scanner.decode_anything()

    def helper(self):
        """
        A helping hand for the user.
        :return: None
        """
        self.text_helper.set("""
                     Barcode Detective is a scanner application, It has 3 modules of operation.
                The scanner scans barcodes translates them to EAN system in order to easily find it.
                It can also translate QR codes into web links and open them.
                
                1) Number mode - Opens a page for a number you put in into the entry box, if it is a valid barcode.
                    *Type in a 12 digit number from the barcode you want to find.
               
                2)Image mode - Allows you to select an image from your computer if it has a barcode. It opens a webpage.
                    *Select an Image from your computer.
               
                3)Live mode - Starts up a webcamera and allows live scanning of barcodes and opens webpage for the product.
                    *Put a barcode in front of your camera, if want to quit the webcam mode press 'q'.""")

