######################################################################
# Author: Giorgi Lomia
# Username: lomiag
# #
# Assignment: A08: UPC Bar Codes
#
# Purpose: Determine how to do some basic operations on lists
#
######################################################################
# Acknowledgements:
#
# None: Original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle

def is_valid_input(barcode):
    """
    Checks if the user input is valid
    :param barcode: User input bar code
    :return: True or False
    """
    if  len(barcode) == 11 and barcode.isnumeric()==True and int(barcode) >= 0:  # Check for if the barcode is valid
        return True
    return False

def is_valid_modulo(barcode):
    """
    Check if the barcode is an appropriate barcode and follows the modulo rule and generates the barcode number
    :param barcode: User barcode
    :return: Correct barcode number
    """
                                                                                # Modulo number used to check the barcode
    odd_num_pos=[]                                                              # List of odd sequence digits
    z = 0                                                                       # Variable that selects the appendable items
    for i in range(2):
        while z < 11:
            odd_num_pos.append(int(barcode[z]))
            z+= 2
        z = 1
    even_num_pos=odd_num_pos[6:]
    del odd_num_pos[6:]
    modulo_num = str(10-((sum((odd_num_pos)*3)+sum(even_num_pos))%10))
    return barcode+modulo_num


def translate(barcode_num):
    """
    Translates the barcode into binary for farther use in drawing the barcode
    :param barcode_num: barcode to translate
    :return: binary version of barcode
    """
    translator = {                                                         #List for the left side
        "0":"0001101",
        "1":"0011001",
        "2":"0010011",
        "3":"0111101",
        "4":"0100011",
        "5":"0110001",
        "6":"0101111",
        "7":"0111011",
        "8":"0110111",
        "9":"0001011"}
    translator_reverse={                                                   #List for the Rigth side
        "0":"1110010",
        "1":"1100110",
        "2":"1101100",
        "3":"1000010",
        "4":"1011100",
        "5":"1001110",
        "6":"1010000",
        "7":"1000100",
        "8":"1001000",
        "9":"1110100"}
    binary = ""
###########################################################################
    coder=barcode_num[:6]                           #left side binary translation
    for i in range(len(coder)):                     #Runs through the left half of barcode
        binary+=translator[coder[i]]                #Translates it into binary
########################################################################### Splits the barcode in left and right side
    coder=barcode_num[6:]                           #right side binary translation
    for i in range(len(coder)):                     #Runs through the right half of barcode
        binary+=translator_reverse[coder[i]]        #Translates it into binary
    return binary

def drawer(code,turtle,guard=False):
    """
    Draws bar lines for any number of 1 and 0 combination
    :param code: The binary version of the barcode
    :param turtle: Turtle that does the drawing
    :param guard: Default = False Can be set to True which increases the bar length
    :return: None
    """
    pen_size=2
    if guard==False:                                                    #In case of guard needed to be drawn
        size=100
    else:
        size=115
    turtle.pensize(pen_size)
    for i in code:                                                      #The process of drawing a barcode
        turtle.lt(90)
        if i == "0":                                                    #Skips a step
            turtle.penup()
        else:                                                           #Draws a line
            turtle.pendown()
        for z in range(2):                                              #Single line drawing
            turtle.right(180)
            turtle.fd(size)
        turtle.penup()                                                  #Returns to the same position
        turtle.right(90)
        turtle.forward(pen_size)                                        #Increments Forward

def draw_full_barcode(tort,barcode):
    tort.hideturtle()
    tort.speed(0)                                                           #Begining stage of Barcode
    tort.penup()
    tort.goto(-100,100)
    drawer("101",tort,True)                                                 #First Guard
    drawer(translate(is_valid_modulo(barcode))[:7],tort,True)               #First Number
    drawer(translate(is_valid_modulo(barcode))[7:42],tort,False)            #Left Side
    drawer("01010",tort,True)                                               #Middle Splitter
    drawer(translate(is_valid_modulo(barcode))[42:76],tort,False)           #Right Side
    drawer(translate(is_valid_modulo(barcode))[76:],tort,True)              #Modulo number
    drawer("101",tort,True)                                                 #Last Guard


def main():
    input_code = input("Enter a 11 digit code [0-9]: ")                         #Asks User for input

    while not is_valid_input(input_code):                                       #Continues asking until valid input
        input_code = input("Invalid number. Enter a 11 digit code [0-9]: ")
    full_code=is_valid_modulo(input_code)
    tort=turtle.Turtle()
    screen=turtle.Screen()
    draw_full_barcode(tort,input_code)                                          #Draws Full functional barcode
    tort.goto(-120,-25)
    tort.write(full_code[0]+"       "+full_code[1:6]+"   "+full_code[6:11]+"       "+full_code[11],font=("Calibri",17,"bold"))#Writes the number
    screen.exitonclick()

if __name__ == "__main__":
    main()
