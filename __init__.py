'''
Version 1.0
Christoph Plusczyk
https://github.com/Chripro/APro/
08.06.2020
'''


from tkinter import *
import algorithm
import sys
from anzeigen import *
from hinzufuegen import *
from entfernen import *
#from aendern import *
Z = {
    'Aron': {'Station1': 22, 'Station2': 14, 'Station3': 120, 'Station4': 21, 'Station5': 4, 'Station6': 51, 'Station7': 51},
    'Brian': {'Station1': 19, 'Station2': 12, 'Station3': 172, 'Station4': 21, 'Station5': 28, 'Station6': 43, 'Station7': 51},
    'Cecilia': {'Station1': 161, 'Station2': 122, 'Station3': 2, 'Station4': 50, 'Station5': 128, 'Station6': 39, 'Station7': 51},
    'David': {'Station1': 19, 'Station2': 22, 'Station3': 90, 'Station4': 11, 'Station5': 28, 'Station6': 4, 'Station7': 51},
    'Erik': {'Station1': 1, 'Station2': 30, 'Station3': 113, 'Station4': 14, 'Station5': 28, 'Station6': 86, 'Station7': 51},
    'Frederik': {'Station1': 60, 'Station2': 70, 'Station3': 170, 'Station4': 28, 'Station5': 68, 'Station6': 104, 'Station7': 51},
    'Gerd': {'Station1': 60, 'Station2': 70, 'Station3': 170, 'Station4': 28, 'Station5': 68, 'Station6': 104, 'Station7': 51},

}

try:
    class MyButton(Button):
        def aktion (self):

            with open('sortiment.txt', 'r') as f:
                G = dict()

                for line in f.read().strip().split('\n\n'):
                    if line.strip() != "":
                        name, Station1, Station2, Station3, Station4, Station5, Station6, Station7 = line.strip().split('\n')
                        G[name] = dict(Station1=int(Station1), Station2=int(Station2), Station3=int(Station3), Station4=int(Station4), Station5=int(Station5), Station6=int(Station6), Station7=int(Station7))
                #s = G.replace(', ',',\n ')
                #print(s)
                #s=pprint.pprint(G, width=7)


            a = algorithm.find_matching(G, matching_type='max', return_type='list')
            print(G)
            print(Z)
            with open('Matchings_mit_Wert.txt', 'w') as outfile:
                outfile.write("\n".join(str(item) for item in a))
            print(a)
    fenster = Tk()

    fenster.geometry("800x350")
    fenster.title("Kuhn Munkres Algorithmus")
    rahmen = Frame(fenster, relief="ridge", borderwidth=5)
    rahmen.pack(fill="both", expand = 1)
    button1 = Anzeigen(rahmen,text="Personen Anzeigen", width = 20, height = 5)
    button1.config(font=("Arial", 12, "bold"))
    button1["command"] = button1.anzeigen
    button1.place(x = 50, y = 50)
    button2 = Hinzufuegen(rahmen,text="Mitarbeiter hinzufügen", width = 20, height = 5)
    button2.config(font=("Arial", 12, "bold"))
    button2["command"] = button2.hinzufuegen
    button2.place(x = 430, y = 50)
    button3 = Entfernen(rahmen,text="Mitarbeiter entfernen", width = 20, height = 5)
    button3.config(font=("Arial", 12, "bold"))
    button3["command"] = button3.entfernen
    button3.place(x = 50, y = 200)
    button4 = MyButton(rahmen,text="Matching Anzeigen", width = 20, height = 5)
    button4.config(font=("Arial", 12, "bold"))
    button4["command"] = button4.aktion
    button4.place(x = 430, y = 200)

    fenster.mainloop()

except:
  print("folgender Fehler ist aufgetreten: ", sys.exec_info()[0])
#finally:
   # outfile.close()
    #f.close()

