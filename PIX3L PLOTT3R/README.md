<h1>PIX3L PLOTT3R Project</h1>

The robot can print from image file. The python code 

The python code is using [Python on ev3dev](https://github.com/rhempel/ev3dev-lang-python).

*   Prerequisites:
*   
        sudo apt-get update
        sudo apt-get upgrade
        sudo apt-get install python-pip
        sudo pip install termcolor pillow

*   The ev3dev version should be the latest. To upgrade:

        sudo apt-get dist-upgrade


<b><i>You will need to download the contents of this folder before continuing</i></b>

*   Run Black and White Code:
  
        sudo python printmonochrome.py sample\ images/monochrome/IMAGE_HERE.jpg

*   Run Color Code:

        sudo python printcolor.py sample\ images/color/IMAGE_HERE.png
  
