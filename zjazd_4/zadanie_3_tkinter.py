# koszty przejazdu na zadanym dystansie na podstawie ceny paliwa oraz spalania samochodu

import tkinter

def policz_koszt_przejazdu():
    dystans = int(dystans_entry.get())
    spalanie = float(spalanie_entry.get())
    cena_paliwa = float(cena_paliwa_entry.get())

    koszt = (dystans / 100) * spalanie *cena_paliwa

    wynik.configure(text = f'{koszt} PLN')


root = tkinter.Tk()

dystans_label = tkinter.Label(master=root, text="Dystans")
dystans_label.pack()
dystans_entry = tkinter.Entry(master=root)
dystans_entry.pack()

spalanie_label = tkinter.Label(master=root, text="Spalanie")
spalanie_label.pack()
spalanie_entry = tkinter.Entry(master=root)
spalanie_entry.pack()

cena_paliwa_label = tkinter.Label(master=root, text="Cana paliwa")
cena_paliwa_label.pack()
cena_paliwa_entry = tkinter.Entry(master=root)
cena_paliwa_entry.pack()

koszt_label = tkinter.Label(master=root, text="Koszt przejazdu")
koszt_label.pack()

wynik = tkinter.Label(master=root, text=" - ")
wynik.pack()

policz_button = tkinter.Button(master=root, text="Policz", command=policz_koszt_przejazdu)
policz_button.pack()

root.title("KOSZTY PRZEJAZDU")
root.mainloop()