from tkinter import *

class Anzeigen(Button):
  def anzeigen (self):
    fenster = Tk()
    fenster.geometry("500x400")
    fenster.title("Werte pro Station")
    rahmen = Frame(fenster, relief="ridge", borderwidth=5)
    rahmen.pack(fill="both", expand = 1)
    label = Label(rahmen, text = "Mitarbeiterliste:")
    label.config(font=("Arial", 14, "bold"))
    label.pack(pady = 20)
    rahmen2 = Frame(rahmen, relief="ridge", borderwidth=1)
    rahmen2.pack(pady = 20, padx = 30)
    f = open('sortiment.txt','r')
    inhalt = f.readlines()
    scrollbar = Scrollbar(rahmen2)
    liste = Listbox(rahmen2, yscrollcommand = scrollbar.set, width = 50)
    i = 0
    for zeile in inhalt:
      if i == 0:
        ausgabe = "Mitarbeiter: "+zeile
        i += 1
      elif i == 1:
        ausgabe = "Radmontage A: "+zeile
        i += 1
      elif i == 2:
        ausgabe = "Radmontage B: "+zeile
        i += 1
      elif i == 3:
        ausgabe = "Antriebsmontage: "+zeile
        i += 1
      elif i == 4:
        ausgabe = "Elekroinstallation: "+zeile
        i += 1
      elif i == 5:
        ausgabe = "Verkabelung: " + zeile
        i += 1
      elif i == 6:
        ausgabe = "Karosseriemontage: " + zeile
        i += 1
      elif i == 7:
        ausgabe = "Qualitätskontrolle: " + zeile
        i += 1
      elif i == 8:
        ausgabe = ""
        i = 0
      liste.insert(END, ausgabe)
    f.close()
    scrollbar.config(command=liste.yview)
    liste.pack(side="left", fill = "both")
    scrollbar.pack(side = "left", fill = "y")
    button = Button(rahmen,text="OK", command=fenster.destroy, width = 10, height = 2)
    button.config(font=("Arial", 10))
    button.pack(pady = 10)
    fenster.mainloop()