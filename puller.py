import os
import glob
import Tkinter
import glob2 #need to download and install this.
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




def goButtonCallback():
	os.chdir(rawFolder)
	fileName = fileNameEntry.get()
	#list1 = [raw,cop]
	for f in glob2.glob(*/**/'*' + str(fileName) + '*.*'): #search for files that contain FileName
		print (f)
		print (fileName)
		copy(f,destFolder) 
		#if f == fileName + '.iiq':
			#print (fileName)
		#else: print ('nothing found')
		
		 
#Go Button
goButton = Tkinter.Button (top, text = "Go!", command = goButtonCallback)
goButton.pack()



top.mainloop()


