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
#fenster1   
i=7
FragenListe=([])
while (i<=13):
    FragenListe = np.append(FragenListe , Label(fenster1, text=Fragen[i]))
    i=i+1

i=0
c=0
while (i<=6):
    FragenListe[i].grid(row = c , column = 1 )
    i=i+1  
    c=c+1
    
i=6
PunkteListe=([])
while (i<=11):
    PunkteListe = np.append(PunkteListe , Label(fenster1, text=Punkte[i]))
    i=i+1

i=0
c=1
while (i<=5):
    PunkteListe[i].grid(row = c , column = 2 )
    i=i+1  
    c=c+1





Anzeige=([]) 
i=1
while (i<=7):
    Anzeige= np.append(Anzeige,Label(fenster2))
    
    
def button_action1(i):
    Anzeige[i].config(text=Fragen[i])
    
Anzeigebutton=([])     
i=1
while (i<=7):   
    Anzeigebutton = np.append(Anzeigebutton,Button(fenster1, text="Anzeigen", command=button_action1[i]))
Anzeigegrid=([])    
i=1
while (i<=7):      
    Anzeigegrid=np.append(Anzeigegrid, Anzeigebutton[i].grid(row=i,column=0))    
 
Anzeigen=([])   
button =([])

#while 

#while (i<=6):
#    button = np.append(button,Anzeigen.config(text = Fragen[i] ))

#while (i<=6):
#    button = np.append(button,Anzeigen.config(text = Fragen[i] ))
#    Anzeigen = np.append(Anzeigen , Button(fenster1, text="Anzeigen", command=button[i]))
#    i=i+1
#i=0   
#while (i<=6):
#    Anzeigen[i].grid(row=i, column = 0)
#Funktionen

# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button Klick me anklickt
#def button_action1():
#    Eingabe1 = float(eingabefeld1.get())
#    if (Eingabe1 == ""):
#        welcome_label1.config(text="Error")
#    else:
#        Eingabe1 = Eingabe1
#        welcome_label1.config(text=Eingabe1)
#    Eingabe2 = float(eingabefeld2.get())
#    if (Eingabe2 == ""):
#        welcome_label2.config(text="Error")
#    else:
#        Eingabe2 = Eingabe2
#        welcome_label2.config(text=Eingabe2)
#    Eingabe3 = Eingabe1 + Eingabe2
#    Eingabe3 = Eingabe3
#    Summe.config(text=Eingabe3)

#def quit():
#    command=fenster1.quit
#    command=fenster2.quit



#label
# Anweisungs-Label
label_Punkte1 = Label(fenster1, text="Punkte")
label_Punkte2 = Label(fenster2, text="Punkte")

# Hier kann der Benutzer eine Eingabe machen
#eingabefeld1 = Entry(fenster1, bd=5, width=40)

#eingabefeld2 = Entry(fenster1, bd=5, width=40)



#welcom_button1 = Button(fenster1, text="Klick me", command=button_action1)
#exit_button = Button(fenster1, text="Beenden", command=fenster1.quit)

#Komponenten hinzufügen 
 
label_Punkte1.grid(row = 0, column = 2)
label_Punkte2.grid(row = 0, column = 1)
#eingabefeld1.grid(row = 1, column = 1)
#eingabefeld2.grid(row = 2, column = 1)


#welcom_button1.grid(row = 3, column = 0)
#exit_button.grid(row = 3, column = 1)

#fenster2

#Funktionen

#label

#welcome_label1 = Label(fenster2)
#welcome_label2 = Label(fenster2)
#Summe = Label(fenster2)



#Komponenetn hinzufügen 

#welcome_label1.grid(row = 1, column = 0, columnspan = 2)
#welcome_label2.grid(row = 2, column = 0, columnspan = 2)
#Summe.grid(row = 3, column = 0, columnspan = 2)


# Nun fügen wir die Komponenten unserem Fenster hinzu


fenster1.mainloop()
fenster2.mainloop()
