import tkinter as tk

#tworzenie głównego okna
main_window = tk.Tk()

#Główne okno 
main_window.title("SpicyMacro")
main_window.geometry("1000x600")
main_window.resizable(False, False)

#ciekawe

frame_placement = {
    "x": 10, 
    "y": 60, 
    "width": 980, 
    "height": 530
}

#Definicje
def switch_tabs():
    gathering_frame.place_forget()
    kill_collect_frame.place_forget()
    boosts_frame.place_forget()
    quests_frame.place_forget()
    settings_frame.place_forget()


    choice = button.get()

    if choice == 1:
        gathering_frame.place(**frame_placement)
    elif choice == 2:
        kill_collect_frame.place(**frame_placement)
    elif choice == 3:
        boosts_frame.place(**frame_placement)
    elif choice == 4:
        quests_frame.place(**frame_placement)
    elif choice == 5:
        settings_frame.place(**frame_placement)
        

#przyciski
button = tk.IntVar(value=1)

gathering = tk.Radiobutton(
    main_window,
    text="Gathering",
    font=('Arial', 15),
    width=10,
    height=1,
    indicatoron=False,
    value=1,
    variable=button,
    command=switch_tabs
)

collect_kill = tk.Radiobutton(
    main_window,
    text="Collect/Kill",
    font=('Arial', 15),
    width=10,
    height=1,
    indicatoron=False,
    value=2,
    variable=button,
    command=switch_tabs
)

boosts = tk.Radiobutton(
    main_window,
    text="Boosts", 
    font=('Arial', 15),
    width=10,
    height=1,
    indicatoron=False,
    value=3,
    variable=button,
    command=switch_tabs
)

quests = tk.Radiobutton(
    main_window,
    text="Quests",
    font=('Arial', 15), 
    width=10, 
    height=1, 
    indicatoron=False,
    value=4,
    variable=button,
    command=switch_tabs
    
)

settings = tk.Radiobutton(
    main_window,
    text="Settings",
    font=('Arial', 15), 
    width=10, 
    height=1, 
    indicatoron=False,
    value=5,
    variable=button,
    command=switch_tabs
)

#zakładki
gathering_frame = tk.Frame(
    main_window,
)

kill_collect_frame = tk.Frame(
    main_window,
)

boosts_frame = tk.Frame(
    main_window,
)

quests_frame = tk.Frame(
    main_window
)

settings_frame = tk.Frame(
    main_window
)

#gathering frame

gatheringtext = tk.Label(
    gathering_frame,
    text="Gathering",
    font=('Arial', 20, 'bold')
)

gatheringtext.pack(
    padx=10,
    pady=10
)

#Kill/collect

kill_collect_text = tk.Label(
    kill_collect_frame,
    text="Kill/Collect",
    font=('Arial', 20, 'bold')
)

kill_collect_text.pack(
    padx=10,
    pady=10
)

#boosts

boosts_frame_text = tk.Label(
    boosts_frame,
    text="Boosts",
    font=('Arial', 20, 'bold')
)

boosts_frame_text.pack(padx=10, pady=10)

#Quests

quests_frame_text = tk.Label(
    quests_frame,
    text="Quests",
    font=('Arial', 20, 'bold')
)

quests_frame_text.pack(padx=10, pady=10)

#settings

settings_frame_text = tk.Label(
    settings_frame,
    text="Settings",
    font=('Arial', 20, 'bold')
)

settings_frame_text.pack(padx=10, pady=10)

#Opcje przycisków (miejsce)
gathering.place(x=10, y=10)

collect_kill.place(x=130, y=10)

boosts.place(x=250, y=10)

quests.place(x=370, y=10)

settings.place(x=490, y=10)

switch_tabs()

#mainloop (nie tykać)
main_window.mainloop()