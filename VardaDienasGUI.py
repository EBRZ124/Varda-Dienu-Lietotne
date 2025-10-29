import tkinter as tk
import datetime
import dati

varda_dienas = tk.Tk()
varda_dienas.title("Vārda Dienas")
varda_dienas.geometry("740x580")
varda_dienas.configure(bg="#E6E6E6", cursor="star")

home_page = tk.Frame(varda_dienas, bg = "#E6E6E6")
home_page.pack(pady=10)

def dienu_kastes():
    for widget in home_page.winfo_children():
        widget.destroy()

    tk.Label(home_page, text = "Šodienas vārda dienas", bg="#E6E6E6", fg="black", font = ("Comfortaa", 24, "bold")).grid(row=0, column=0, columnspan=3, pady=20) 
    today = datetime.date.today()
    tomorrow = today+datetime.timedelta(days=1)
    yesterday = today-datetime.timedelta(days=1)

    key_today = (today.month, today.day)
    key_tomorrow = (tomorrow.month, tomorrow.day)
    key_yesterday = (yesterday.month, yesterday.day)

    formatted_string_today = today.strftime("%B %d, %Y")
    formatted_string_tomorrow = tomorrow.strftime("%B %d, %Y")
    formatted_string_yesterday = yesterday.strftime("%B %d, %Y")

    # Yesterday
    if key_yesterday in dati.datumi_vardi:
        vardu_saraksts = dati.datumi_vardi[key_yesterday]["vārdi"]

        vardu_yesterday_frame = tk.Frame(home_page, borderwidth=2, bg="white", relief="ridge",padx=20, pady=20)
        vardu_yesterday_frame.grid(row=1, column=0, padx=10, pady=10)
        tk.Label(vardu_yesterday_frame, text=formatted_string_yesterday, font=("Comfortaa", 16, "bold"), fg="black", bg="white").pack(side="top", pady=5)
        for vards in vardu_saraksts:
            tk.Label(vardu_yesterday_frame, text=vards, font=("Comfortaa", 16), fg="black", bg="white").pack(side="top")
    else:
        tk.Label(home_page, text= "Šodien nevienam nav vārda dienas.", font=("Comfortaa", 16), fg="black", bg="white").grid(row=1, column=0, pady=20)
    
    # Today
    if key_today in dati.datumi_vardi:
        vardu_saraksts = dati.datumi_vardi[key_today]["vārdi"]

        vardu_today_frame = tk.Frame(home_page, borderwidth=2, bg="white", relief="ridge",padx=20, pady=20)
        vardu_today_frame.grid(row=1, column=1, padx=10, pady=10)
        tk.Label(vardu_today_frame, text=formatted_string_today, font=("Comfortaa", 16, "bold"), fg="black", bg="white").pack(side="top", pady=5)
        for vards in vardu_saraksts:
            tk.Label(vardu_today_frame, text=vards, font=("Comfortaa", 16), fg="black", bg="white").pack(side="top")
    else:
        tk.Label(home_page, text= "Šodien nevienam nav vārda dienas.", font=("Comfortaa", 16), fg="black", bg="white").grid(row=1, column=0, pady=20)
    
    # Tomorrow
    if key_tomorrow in dati.datumi_vardi:
        vardu_saraksts = dati.datumi_vardi[key_tomorrow]["vārdi"]

        vardu_tomorrow_frame = tk.Frame(home_page, borderwidth=2, bg="white", relief="ridge",padx=20, pady=20)
        vardu_tomorrow_frame.grid(row=1, column=2, padx=10, pady=10)
        tk.Label(vardu_tomorrow_frame, text=formatted_string_tomorrow, font=("Comfortaa", 16, "bold"), fg="black", bg="white").pack(side="top", pady=5)
        for vards in vardu_saraksts:
            tk.Label(vardu_tomorrow_frame, text=vards, font=("Comfortaa", 16), fg="black", bg="white").pack(side="top")
    else:
        tk.Label(home_page, text= "Šodien nevienam nav vārda dienas.", font=("Comfortaa", 16), fg="black", bg="white").grid(row=1, column=0, pady=20)

dienu_kastes()
varda_dienas.mainloop()
