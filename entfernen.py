from tkinter import *

class Entfernen(Button):
  def entfernen (self):
    class MyButton (Button):
      def aktion (self):
        artnr = eingabe1.get()
        f = open('sortiment.txt','r')
        liste = f.readlines()
        f.close()
        geloescht = False
        for i in range(len(liste)):
          if liste[i] == artnr+"\n":
            f = open('sortiment.txt','w')
            liste = liste[:i] + liste[i+9:]
            for linie in liste:
                f.write(linie)
            geloescht = True
            break
        f.close()
        fenster.destroy()
        if geloescht:
          fenster2 = Tk()
          fenster2.geometry("300x100")
          fenster2.title("Mitarbeiter entfernt!")
          rahmen2 = Frame(fenster2, relief="ridge", borderwidth=5)
          rahmen2.pack(fill="both", expand = 1)
          label2 = Label(rahmen2, text="Mitarbeiter entfernt!")
          label2.pack(expand = 1)
          button2 = Button(rahmen2,text="OK", command=fenster2.destroy)
          button2.pack(side = "bottom", pady = 5)
          fenster2.mainloop()
        else:
          fenster2 = Tk()
          fenster2.geometry("300x100")
          fenster2.title("Warnung!")
          rahmen2 = Frame(fenster2, relief="ridge", borderwidth=5)
          rahmen2.pack(fill="both", expand = 1)
          label2 = Label(rahmen2, text="Name nicht gefunden!")
          label2.pack(expand = 1)
          button2 = Button(rahmen2,text="OK", command=fenster2.destroy)
          button2.pack(side = "bottom", pady = 5)
          fenster2.mainloop()
    fenster = Tk()
    fenster.geometry("500x400")
    fenster.title("Mitarbeiter löschen")
    rahmen = Frame(fenster, relief="ridge", borderwidth=5)
    rahmen.pack(fill="both", expand = 1)
    label = Label(rahmen, text = "Welchen Mitarbeiter möchten Sie entfernen?")
    label.config(font=("Arial", 14, "bold"))
    label.place(x = 50, y = 10)
    label1 = Label(rahmen, text = "Name:")
    label1.place(x = 100, y = 100)
    eingabe1 = Entry(rahmen, bd = 2, width = 22)
    eingabe1.place(x = 200, y = 100)
    button = MyButton(rahmen,text="Eingabe")
    button["command"] = button.aktion
    button.place(x = 180, y = 220)
    fenster.mainloop()