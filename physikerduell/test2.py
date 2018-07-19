import tkinter
from functools import partial

def close_window(handler):
    handler.quit()

def main():
    print ("in main")
    mainwindow = tkinter.Tk()
    mainwindow.title("nasobeme")

    eingabefeld_integer=tkinter.Entry(mainwindow)
    eingabefeld_integer.pack()

    def werte_zeigen():
        print (eingabefeld_integer.get())

    beenden_button=tkinter.Button(mainwindow, text="Beenden", command=partial(close_window, mainwindow))
    beenden_button.pack()
    wertezeigen_button=tkinter.Button(mainwindow, text="Werte zeigen", command=werte_zeigen)
    wertezeigen_button.pack()

    mainwindow.mainloop()

if __name__ == '__main__':
    main()
