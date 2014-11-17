import os
import glob
import Tkinter
import glob2  #need to download and install this.
import shutil 
from shutil import copy
from tkFileDialog import askdirectory

top = Tkinter.Tk()

 
#Select Capture Folder button chooses input folder
def rawButtonCallback():
	global rawFolder
	rawFolder = askdirectory()
	

#Select Destination Folder button chooses output folder
def destButtonCallback():
	global destFolder
	destFolder = askdirectory()
	
#Select Capture Folder button
rawPathButton = Tkinter.Button (top, text = "Select Capture Folder", command = rawButtonCallback)
rawPathButton.pack()

#Select Destination Folder button
destPathButton = Tkinter.Button (top, text = "Select Destination Folder", command = destButtonCallback)
destPathButton.pack()

#File Name entry field
fileNameEntry = Tkinter.Entry(top)
fileNameEntry.pack()



#Main Functionality
def goButtonCallback():
	os.chdir(rawFolder) #the function will work on this folder
	fileName = fileNameEntry.get()
	fileExt = ['.iiq', '.CR2', '.eip', '.cos'] #need to figure out how to make this not case sensitive
	settingsDir = (destFolder + '/CaptureOne/Settings70') #create settings folder
	if not os.path.isdir(settingsDir): #if the settings folder is not there,
				os.makedirs(settingsDir) #make it
	for f in glob.glob('*' + str(fileName) + '*' + str(fileExt[1])): #Search for raw file types (right now just .CR2)
		#print (f)
		shutil.copy(f,destFolder)
		print ('Copied RAW - ' + str(f))	
			
	for f in glob2.glob('*/**/*' + str(fileName) + '*' + str(fileExt[3])): #search recursive for files that contain FileName .cos
				shutil.copy(f,settingsDir) # copy the setting files over
		print ('Copied Settings - ' + str(f))
					
		 
#Go Button
goButton = Tkinter.Button (top, text = "Go!", command = goButtonCallback)
goButton.pack()


top.mainloop()
