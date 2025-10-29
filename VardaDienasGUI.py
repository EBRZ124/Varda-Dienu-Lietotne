import tkinter as tk
import datetime
import dati

varda_dienas = tk.Tk()
varda_dienas.title("Vārda Dienas")
varda_dienas.geometry("740x580")
varda_dienas.configure(bg="#E6E6E6", cursor="star")

home_page = tk.Frame(varda_dienas, bg = "#E6E6E6")
home_page.pack(pady=10)

def sodienas_teksta_kaste():
    for widget in home_page.winfo_children():
        widget.destroy()

    tk.Label(home_page, text = "Šodienas vārda dienas", bg="#E6E6E6", fg="black", font = ("Comfortaa", 24, "bold")).grid(row=0, column=0, columnspan=2, pady=20) 
    today = datetime.date.today()
    key = (today.month, today.day)

    if key in dati.datumi_vardi:
        vardu_saraksts = dati.datumi_vardi[key]["vārdi"]

        vardu_frame = tk.Frame(home_page, borderwidth=2, bg="white", padx=20, pady=20)
        vardu_frame.grid(row=1, column=0, padx=10, pady=10)

        for vards in vardu_saraksts:
            tk.Label(vardu_frame, text=vards, font=("Comfortaa", 16), fg="black", bg="white").pack(side="top")
    else:
        tk.Label(home_page, text= "Šodien nevienam nav vārda dienas.", font=("Comfortaa", 16), fg="black", bg="white").grid(row=1, column=0, pady=20)

sodienas_teksta_kaste()

varda_dienas.mainloop()


