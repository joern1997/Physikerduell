import tkinter as tk
import numpy as np
import csv
from tkinter.filedialog import askopenfilename

#Anfangsvariablen
Anfangsi=0
Anfangsj=0
Anfangsd=1
Anfangsc=0
Anfangsn=6
Anfangsh=0
Anfangsabstand=1
AGcounter=1


#Fenster werde definiert und konfiguriert
fenster1 = tk.Tk()
fenster1.title('Privat')
fenster2 = tk.Toplevel(fenster1)
fenster2.title('Öffentlich')
FragenFrame=tk.Frame(fenster1)
FragenFrame.grid(row=0,columnspan=3)
PunkteFrame=tk.Frame(fenster1)
PunkteFrame.grid(row=7,columnspan=4)

#Einbinden des Logos 
photo = tk.PhotoImage(file="Physikerduell-0.png")
#Foto = PhotoImage(file="Physikerduell-0.png")
photo1= tk.Label(fenster2,image=photo)
photo2=tk.Label(fenster1,image=photo)
photo1.grid()
photo2.grid()             
photo1.image = photo  
photo2.image = photo





def Aussuchen():
    Dateinname =askopenfilename()
	#Punkte einlesen
    i=0
    global Punkte
    Punkte = np.array([])
    reader = csv.reader(open(Dateinname))
    for row in reader:
        if (row[1] == ""):
            del(row[1])
        else:
            Punkte = np.append( Punkte ,float(row[1]))
            i=i+1

	#Fragen Einlesen       
    i=0
    global Fragen
    Fragen = np.array([])
    reader = csv.reader(open(Dateinname))
    for row in reader:
        if (row[0] == ""):
	        del(row[0])
        else:
            Fragen = np.append( Fragen ,row[0])
            i=i+1
    

	       
	       


#Menü Definition der Funktionen die im Menü Aufgerufen werden
def Exit():
    fenster1.destroy()
    fenster2.destroy()

def Start():
    FramesNext(Anfangsi,Anfangsj, Anfangsd,Anfangsc,Anfangsn,Anfangsabstand)
    photo1.grid_remove()
    photo2.grid_remove()


#Kommando um die Nächte Folie zu ertsellen
def commandnext():
    global Anfangsi
    global Anfangsj
    global Anfangsd
    global Anfangsn
    global Anfangsc
    global Anfangsabstand
    Anfangsi=Anfangsi+7    
    Anfangsj=Anfangsj +6
    Anfangsd=1
    Anfangsc=0
    Anfangsn= Anfangsn + 7
    Anfangsabstand= Anfangsabstand + 1
    FramesNext(Anfangsi,Anfangsj, Anfangsd,Anfangsc,Anfangsn,Anfangsabstand)

#Kommando um eine Folie zurückzugehen    
def commandback():
    global Anfangsi
    global Anfangsj
    global Anfangsd
    global Anfangsn
    global Anfangsc
    global Anfangsabstand
    Anfangsi=Anfangsi - 7    
    Anfangsj=Anfangsj - 6
    Anfangsd=1
    Anfangsc=0
    Anfangsn= Anfangsn - 7
    Anfangsabstand= Anfangsabstand - 1
    FramesNext(Anfangsi,Anfangsj, Anfangsd,Anfangsc,Anfangsn,Anfangsabstand)



#Bestätigt die Anzahl der Arbeitgruppen und Maximalen Runden
#und schließt das Fenster
def accept(AnzahlRunden,AnzahlAG):
    #Nimmt die Zahlen aus dem Eingabefeld entgegen
    Zahl_AnzahlRunden = int(AnzahlRunden.get())
    Zahl_AnzahlAG = int(AnzahlAG.get())
    AGCounter=0
    PunkteAG=([])
    while (AGCounter < Zahl_AnzahlAG):
        PunkteAG.append(([]))
        RundenCounter=0
        tk.Label(PunkteFrame,text='Arbeitsgruppe:').grid(row=0,column=0)
        
        #Erstellt für eine Arbeitsgruppe die Eingabefenster für den Namen sowie für die
        #Punkte für die Runden
        while (RundenCounter <= Zahl_AnzahlRunden):
            PunkteAG[AGCounter].append(tk.Entry(PunkteFrame))
            PunkteAG[AGCounter][RundenCounter].grid(row=RundenCounter,column = AGCounter +1 )
            RundenCounter=RundenCounter+1
        
        #Numeriert die Runden durch
        RundenCounter=0
        while (RundenCounter < Zahl_AnzahlRunden):
            tk.Label(PunkteFrame, text = 'Runde' + str(RundenCounter + 1)).grid(row=RundenCounter+1, column = 0)
            RundenCounter=RundenCounter +1
            
        AGCounter=AGCounter+1
   

#Fenster in dem die Anzahl an Maximalen Runden sowie dei Anzahl an Arbeitsgruppen eingegeben wird
def Arbeitsgruppenanzahl():
    AGFenster=tk.Tk()
    AGFenster.title('Arbeitsgruppen')
    tk.Label(AGFenster,text="Anzahl an AG's").grid(row=0, column=0)
    tk.Label(AGFenster,text="Anzahl der Runden").grid(row=1, column=0)
    AnzahlAG=tk.Entry(AGFenster)
    AnzahlAG.grid(row=0,column=1)
    AnzahlRunden=tk.Entry(AGFenster)
    AnzahlRunden.grid(row=1,column=1)
    #Buton der die Eingaben bestätigt
    tk.Button(AGFenster,text='Accept', command = lambda AnzahlRunden=AnzahlRunden,AnzahlAG=AnzahlAG :accept(AnzahlRunden,AnzahlAG)).grid(row=2,column=1)
    #Schliest das Fenster
    tk.Button(AGFenster,text='Exit',command=lambda: AGFenster.destroy()).grid(row=2,column=0)

#Menüpunkte die in der oberen Leiste zu sehen sind 
menu = tk.Menu(fenster1)
fenster1.config(menu=menu)
menu.add_command(label='Exit', command=Exit)# Menü um das Programm zu beenden
menu.add_command(label='Start',command=Start)#Menu um das Programm zu starten
menu.add_command(label='Datei', command=Aussuchen)
menu.add_command(label='Back',command = commandback)#Menu üm ine Folie zurück zu gehen
menu.add_command(label='Next',command = commandnext)#Menü um zu nächsten Folie zu gehen
menu.add_command(label='Arbeitsgruppen',command=Arbeitsgruppenanzahl)




    

#Dies ist die Hauptschleife
#(Geht bestimmt schöner)
#Diese Schleife wird jedesmal aufgerufen wenn auf start,back, next gedrückt wird
def FramesNext(Anfangsi,Anfangsj, Anfangsd,Anfangsc,Anfangsn,Anfangsabstand):


    
    #erlaubt das ändern der Variabeln
    global Frage1
    global Frage2
    global Punkte1
    global Punkte2
	
    #Allgemeine Überschrift
    Punkte1=tk.Label(FragenFrame,text="Punkte",width=8)
    Punkte2=tk.Label(fenster2, text="Punkte",width=8)
    Punkte1.grid(row = 0, column = 1)
    Punkte2.grid(row = 0, column = 1)
    Punkte2.config(font=(15))




    #Setzt parameter
    i=Anfangsi
    j=Anfangsj
    d=Anfangsd
    c=Anfangsc
    n=Anfangsn


    #Stellt fragen/Punkte dar bzw. Platzhalter
    while (i<=n):
        Frage1=tk.Label(FragenFrame, text = Fragen[i],width=80)
        Frage1.grid(row = c, column = 0)
        Frage2=tk.Label(fenster2, text = Fragen[Anfangsi],width=80)
        Frage2.config(font=(15))
        Frage2.grid(row = 0, column = 0)
        
        if (i<=n-1):
            Punkte1=tk.Label(FragenFrame, text = Punkte[j],width=4)
            Punkte1.grid(row = d, column = 1)
            Frage2=tk.Label(fenster2, text='_________________',width=80)
            Frage2.config(font=(15))
            Frage2.grid(row = d, column = 0)
            Punkte2=tk.Label(fenster2, text = '___',width=4)
            Punkte2.grid(row = d, column = 1)
            Punkte2.config(font=(15))
        i=i+1
        d=d+1
        c=c+1
        j=j+1

    #Button Aktionen Zum Anzeigen der Fragen und Punkte im 2.ten Fenster
    def AnzeigenAktion(i,j,d):
        tk.Label(fenster2, text = Fragen[i],width=80).grid(row = d, column = 0).config(font=(15))
        tk.Label(fenster2, text= Punkte[j],width=4).grid(row =d, column = 1).config(font=(15))
    

    i=Anfangsi + 1
    j=Anfangsj
    d=Anfangsd
    h=Anfangsh
    AnzeigeButton={}
    
    #Buttons zum Anzeigen der Fragen auf dem 2.ten Fester
    while (i<=n):
        AnzeigeButton[h]=tk.Button(FragenFrame,text='Anzeigen', command = lambda  i=i,j=j,d=d :AnzeigenAktion(i,j,d)).grid(row= d, column= 3)
        i=i+1
        j=j+1
        d=d+1
        h=h+1
 
#Dieser Abschnitt sorgt dafür, dass Layout im 2.ten Fenster sich an die Größe anpasst
fenster2.grid_columnconfigure(0,weight=1)
fenster2.grid_columnconfigure(1,weight=1)
fenster2.grid_rowconfigure(0,weight=2)
fenster2.grid_rowconfigure(1,weight=2)    
fenster2.grid_rowconfigure(2,weight=2)
fenster2.grid_rowconfigure(3,weight=2)
fenster2.grid_rowconfigure(4,weight=2)
fenster2.grid_rowconfigure(5,weight=2)
fenster2.grid_rowconfigure(6,weight=2)
fenster2.grid_rowconfigure(7,weight=2)


fenster1.mainloop()
fenster2.mainloop()