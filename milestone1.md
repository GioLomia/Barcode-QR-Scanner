# Feedback

Awesome idea, really pushing yourself into new territory. Go for it!

Your Scanner class looks good. I have a few questions. What library are you using for the feed data? I see a CV class collaboration; is that part of OpenCV or some other library? 

What does data_read() do? Not sure what "Reads a data type" means. Meaning it pulls an image into memory? How does it return a bar code? Is there a CV library you're leveraging to do this work? If not, I need to see a LOT more detail about how you're accomplishing this. 

product_open() says it "opens product". What does that mean? Does it open the browser and sends it to a URL containing that barcode's product description? Or something else. Needs more clearly defined.

decoder() and draw_bar(): What? Why is it drawing bar codes? I thought you just got the bar code from the camera? Confused on the purpose of these functions.

I see five files listed in the Files section. Three make sense to me (scanner.py, test_suite.py, and Final_project.py). What do the other two files do (bar_detectory.py and bar_detectory.py...)?

There's no info on those two.

Grade: 9/10

