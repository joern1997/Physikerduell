from tkinter import *
import numpy as np
import csv
from PIL import Image




Anfangsi=0
Anfangsj=0
Anfangsd=1
Anfangsc=0
Anfangsn=6
Anfangsabstand=1
AGcounter=1

fenster1 = Tk()
fenster1.title('Privat')
fenster2 = Toplevel(fenster1)
fenster2.title('Öffentlich')

photo = PhotoImage(file="Physikerduell-0.png")
#Foto = PhotoImage(file="Physikerduell-0.png")
photo1= Label(fenster2,image=photo)
photo2=Label(fenster1,image=photo)
photo1.grid()
photo2.grid()             
photo1.image = photo  
photo2.image = photo



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








#Menü
def Exit():
    exit(0)
#def Start():
#    FramesStart(Anfangsi,Anfangsj, Anfangsd,Anfangsc,Anfangsn,Anfangsabstand)
def Start():
    FramesNext(Anfangsi,Anfangsj, Anfangsd,Anfangsc,Anfangsn,Anfangsabstand)
    Punktestand()
    photo1.grid_remove()
    photo2.grid_remove()

menu = Menu(fenster1)
fenster1.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=Exit)
filemenu.add_command(label='Start',command=Start)
#filemenu.add_command(label='Start',command=Start)


#def NewAG():
#    global AGcounter
#    AGcounter=AGcounter + 1
#    Arbeitsgruppe=Entry(Punkteframe)
#    Arbeitsgruppe.grid(row=0,column=AGcounter)    
#    
#    
#def Punktestand():
#    Punkteframe=Frame(fenster1)
#    Punkteframe.grid(row=8,columnspan=2)
#    #Arbeitsgruppen=Label(Punkteframe,text='Arbeitsgruppe')
#    Arbeitsgruppen.grid(row=0, column=0)
#    Arbeitsgruppe=Entry(Punkteframe)
#    Arbeitsgruppe.grid(row=0,column=AGcounter)
#    PunkteEntry=Entry(Punkteframe)
#    PunkteEntry.grid(row=1,column=1)
#    NewAgCounter = AGcounter + 1
#    NewArbeistgruppe = Button(Punkteframe, text='Neue #AG', command=NewAG)
#    NewArbeistgruppe.grid(row=0,column=NewAgCounter)
    


#Schleife zum erneuern der Anzeige	
def FramesNext(Anfangsi,Anfangsj, Anfangsd,Anfangsc,Anfangsn,Anfangsabstand):
    
    
    
    
    
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
    
    Next =Button(fenster1, text ='Next' , command = commandnext)
    Next.grid(row=7,column=3)
    
    Back = Button(fenster1, text = 'Back' , command = commandback)
    Back.grid(row=7, column = 0)
    
    
    
    
    
    
    
    
    
    #erlaubt das ändern der Variabeln
    global Frage1
    global Frage2
    global Punkte1
    global Punkte2
	
    #Allgemeine Überschrift
    Punkte1=Label(fenster1,text="Punkte",width=8)
    Punkte2=Label(fenster2, text="Punkte",width=8)
    Punkte1.grid(row = 0, column = 1)
    Punkte2.grid(row = 0, column = 1)




    #Setzt parameter
    i=Anfangsi
    j=Anfangsj
    d=Anfangsd
    c=Anfangsc
    n=Anfangsn


    #Stellt fragen/Punkte dar bzw. Platzhalter
    while (i<=n):
        Frage1=Label(fenster1, text = Fragen[i],width=100)
        Frage1.grid(row = c, column = 0)
        Frage2=Label(fenster2, text = Fragen[Anfangsi],width=100)
        Frage2.grid(row = 0, column = 0)
        
        if (i<=n-1):
            Punkte1=Label(fenster1, text = Punkte[j],width=4)
            Punkte1.grid(row = d, column = 1)
            Frage2=Label(fenster2, text='____________',width=100)
            Frage2.grid(row = d, column = 0)
            Punkte2=Label(fenster2, text = '___',width=4)
            Punkte2.grid(row = d, column = 1)
        i=i+1
        d=d+1
        c=c+1
        j=j+1

    #Button Aktionen Zum Anzeigen der Fragen und Punkte im 2.ten Fenster
    def Anzeigen1():
        Frage2=Label(fenster2, text = Fragen[i],width=100)
        Frage2.grid(row = 1, column = 0)
        Punkte2=Label(fenster2, text= Punkte[j],width=4)
        Punkte2.grid(row =1, column = 1)
    def Anzeigen2():
        Frage2=Label(fenster2, text = Fragen[i+1],width=100)
        Frage2.grid(row = 2, column = 0)
        Punkte2=Label(fenster2, text= Punkte[j+1],width=4)
        Punkte2.grid(row =2, column = 1)
    def Anzeigen3():
        Frage2=Label(fenster2, text = Fragen[i+2],width=100)
        Frage2.grid(row = 3, column = 0)
        Punkte2=Label(fenster2, text= Punkte[j+2],width=4)
        Punkte2.grid(row =3, column = 1)
    def Anzeigen4():
        Frage2=Label(fenster2, text = Fragen[i+3],width=100)
        Frage2.grid(row = 4, column = 0)
        Punkte2=Label(fenster2, text= Punkte[j+3],width=4)
        Punkte2.grid(row =4, column = 1)
    def Anzeigen5():
        Frage2=Label(fenster2, text = Fragen[i+4],width=100)
        Frage2.grid(row = 5, column = 0)
        Punkte2=Label(fenster2, text= Punkte[j+4],width=4)
        Punkte2.grid(row =5, column = 1)
    def Anzeigen6():
        Frage2=Label( fenster2,text = Fragen[i+5],width=100)
        Frage2.grid(row = 6, column = 0)
        Punkte2=Label( fenster2,text= Punkte[j+5],width=4)
        Punkte2.grid(row =6, column = 1)

    i=Anfangsi + 1
    j=Anfangsj
    d=Anfangsd

    #Buttons zum Anzeigen der Fragen auf dem 2.ten Fester
    Anzeigebutton1= Button(text='Anzeigen', command = Anzeigen1)
    Anzeigebutton1.grid(row= 1, column= 3)
    
    Anzeigebutton2= Button(text='Anzeigen', command = Anzeigen2)
    Anzeigebutton2.grid(row= 2, column= 3)
    
    Anzeigebutton3= Button(text='Anzeigen', command = Anzeigen3)
    Anzeigebutton3.grid(row= 3, column= 3)

    Anzeigebutton4= Button(text='Anzeigen', command = Anzeigen4)
    Anzeigebutton4.grid(row= 4, column= 3)
    
    Anzeigebutton5= Button(text='Anzeigen', command = Anzeigen5)
    Anzeigebutton5.grid(row= 5, column= 3)
    
    Anzeigebutton6= Button(text='Anzeigen', command = Anzeigen6)
    Anzeigebutton6.grid(row= 6, column= 3)
    
    




fenster1.mainloop()
fenster2.mainloop()
