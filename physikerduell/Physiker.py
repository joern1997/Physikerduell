from tkinter import *
import numpy as np
import csv

fenster1 = Tk()
fenster2 = Tk()

fenster1.title('Privat')
eingabefeld = Entry(fenster1, bd=5, width=40)

fenster2.title('Öffentlich')


#Punkte einlesen
i=0
Punkte = np.array([])
reader = csv.reader(open("Katalog01.csv"))
for row in reader:
    if (row[1] == ""):
        del(row[1])
    else:
        Punkte = np.append( Punkte ,float(row[1]))
        i=i+1
#Fragen Einlesen
        
i=0
Fragen = np.array([])
reader = csv.reader(open("Katalog01.csv"))
for row in reader:
    if (row[0] == ""):
        del(row[0])
    else:
        Fragen = np.append( Fragen ,row[0])
        i=i+1



#Allgemeine Überschrift
label_Punkte1 = Label(fenster1, text="Punkte")
label_Punkte2 = Label(fenster2, text="Punkte")
label_Punkte1.grid(row = 0, column = 1)
label_Punkte2.grid(row = 0, column = 1)


#Frage
i=7
j=6
d=1
c=0
n=13
while (i<=n):
	Frage1 = Label(fenster1, text = Fragen[i])
	Frage1.grid(row = c, column = 0)
	Frage2 = Label(fenster2, text = Fragen[7])
	Frage2.grid(row = 0, column = 0)
	if (i<=n-1):
		Punkte1 = Label(fenster1, text = Punkte[j])
		Punkte1.grid(row = d, column = 1)
	i=i+1
	j=j+1
	d=d+1
	c=c+1

def Anzeigen():
	Frage2 = Label(fenster2, text = Fragen[i])
	Frage2.grid(row = c, column = 0)
	Punkte1 = Label(fenster1, text = Punkte[j])
	Punkte1.grid(row = d, column = 1)
i=7
j=6
d=1
c=0
n=13
Zeigefrage=[]

while (i<n):
	Varname = 'ZeigeFrage%04d' %i
	Zeigefrage.append(Varname)
	i=i+1
	
f=0
i=7
j=6
d=1
c=0
while (f<5):
	Zeigefrage[f]= Button(fenster1, text="Anzeigen", command= Anzeigen)
	Zeigefrage[f].grid(row = 1, column = 3)
	i=i+1
	d=d+1
	j=j+1
	c=c+1









fenster1.mainloop()
fenster2.mainloop()
