#This is python code is made to be run on a computer (tested on Ubuntu 15.10)
import os, time #import software
path_to_watch = "/home/sanjay/Downloads" #define path where downloads are placed (in web browser)
before = dict ([(f, None) for f in os.listdir (path_to_watch)]) #check files before checking for new files
while 1: #run forever
  time.sleep (2) #check every 2 seconds
  after = dict ([(f, None) for f in os.listdir (path_to_watch)]) #check current files
  added = [f for f in after if not f in before] #see if a file was added
  removed = [f for f in before if not f in after] # or removed
  if added:
    print added[0] #print which file was added
    os.system('mv "Downloads/'+added[0]+'" Downloads/print.png') #rename file
    added[0] = 'print.png' #update array to renamed file
    os.system('sshpass -p maker scp "Downloads/'+added[0]+'" robot@192.168.43.22:~/') #copy file to ev3
    os.system('sshpass -p maker ssh -t robot@192.168.43.22 "~/printer.sh \''+added[0]+'\'"') #start remote printer starter with command line input
  before = after #update file list
