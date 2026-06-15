import tkinter as tk
fenster = tk.Tk()
fenster.geometry("400x500")

liste =tk.Listbox(fenster)
liste.place(x=140, y=10, width=150, height=200)

aufgabe = "hinzufügen"
eingabe = tk.Entry(fenster)
eingabe.place(x=10, y=110, width=120, height=30)

#punkte = tk.Button(fenster, width=2, height=1, text="-")
#punkte.pack()
#punkte.place(x=20, y=20)

def hinzufuegen():
    global aufgabe, eingabe, liste
    aufgabe = eingabe.get()
    liste.insert(tk.END, aufgabe)
    eingabe.delete(0, tk.END)

punkte2 = tk.Button(fenster, width=10, height=1, text="Add", command=hinzufuegen)
punkte2.place(x=28, y=20)

def delete_all():
    global aufgabe, eingabe, liste
    aufgabe = eingabe.get()
    liste.delete(0, tk.END)

def delete_one():
    aufgabe = eingabe.get()
    liste.delete(tk.ACTIVE)

löschen_alles = tk.Button(fenster, width=15, height=1, text="Completed all", command=delete_all)
löschen_alles.place(x=11, y=50)

löschen_einzel = tk.Button(fenster, width=15, height=1, text="Completed one", command=delete_one)
löschen_einzel.place(x=11, y=80)

fenster.mainloop()
