# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 10:03:36 2015

@author: Ardit Sulce
"""

import simplekml
import pandas
import tkinter
from tkinter.filedialog import askopenfilename

def browse():
    global infile    
    infile=askopenfilename()

def kmlFunction(outfile="C:\\out\\Coordinates.kml"):
    global infile
    if infile is None:       
       infile=browse()
    df=pandas.read_csv(infile)
    kml=simplekml.Kml()
    for lon,lat in zip(df["Longitude"],df["Latitude"]):
        kml.newpoint(coords=[(lon,lat)])
    kml.save(outfile)
    
root=tkinter.Tk()
root.title("KML Generator")
label=tkinter.Label(root,text="This program generates a KML file out of a CSV")
label.pack()
browseButton=tkinter.Button(root,text="Browse",command=browse)
browseButton.pack()
kmlButton=tkinter.Button(root,text="Generate KML",command=kmlFunction)
kmlButton.pack()
root.mainloop()


