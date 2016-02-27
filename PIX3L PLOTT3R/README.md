<h1>PIX3L PLOTT3R Project</h1>

The robot can print from any image file using python!

We provide code to print in black & white and color.
We also provide sample images.



*   Prerequisites:
*   
        sudo apt-get update
        sudo apt-get upgrade
        sudo apt-get install python-pip
        sudo pip install python-ev3dev termcolor pillow

*   The ev3dev version should be the latest. To upgrade:

        sudo apt-get dist-upgrade


<b><i>You will need to download the contents of this folder before continuing</i></b>

*   Run Black and White Code:
  
        sudo python printmonochrome.py sample\ images/monochrome/IMAGE_HERE.jpg

*   Run Color Code:

        sudo python printcolor.py sample\ images/color/IMAGE_HERE.png
        
The color printing program will print 4 times with different pens. The code understands red, green, blue, and black and will automatically split images up into these colors.

When presented with a dialogue, type <code>" "</code> and press enter to continue. If the dialogue prints a color, switch the pen to that color, then continue. 
  
