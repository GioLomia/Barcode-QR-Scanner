from bar_detector import *
import scanner
import sys
def testit(did_pass):
    """  Prints the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def scanner_test():
    testit(bar_decoder("barcode_01.jpg")=="0051500241639")
    testit(check(Image.open("barcode_01.jpg"))==True)

    s=scanner.Scanner(value_to_unpack="12345678901")
    s.mode="NUMBER"
    testit(s.decode()=="123456789012")

    s.value_to_unpack="12039485712"
    testit(s.decode()=="120394857124")

    s=scanner.Scanner(value_to_unpack="barcode_01.jpg")
    s.mode="IMAGE"
    testit(s.decode()=="0051500241639")

    s=scanner.Scanner(value_to_unpack="barcode_01.jpg")
    s.mode="IMAGE"
    s.browser="ON"
    s.decode()
    testit(s.web_browse()=="https://www.barcodelookup.com/0051500241639")
    s.browser="OFF"
    testit(s.web_browse()=="0051500241639")

    s.value_to_unpack = "QR_code_example.jpg"
    s.decode()
    s.qr_mode="ON"
    s.browser="ON"
    testit(s.web_browse()=="https://internationalbarcodes.com/")
    s.browser="OFF"
    testit(s.web_browse()=="https://internationalbarcodes.com/")

scanner_test()


