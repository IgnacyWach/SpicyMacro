import customtkinter as ctk

#tworzenie głównego okna / Creating main window
main_window = ctk.CTk()

#Główne okno / Main Window
main_window.title("SpicyMacro")
main_window.geometry("1000x600")
main_window.resizable(False, False)

#ciekawe / Intresting

frame_placement = {
    "x": 10, 
    "y": 60, 
}

#Definicje / Define



def switch_tabs(choice):
    gathering_frame.place_forget()
    kill_collect_frame.place_forget()
    boosts_frame.place_forget()
    quests_frame.place_forget()
    settings_frame.place_forget()


    if choice == "Gathering":
        gathering_frame.place(**frame_placement)
    elif choice == "Collect/Kill":
        kill_collect_frame.place(**frame_placement)
    elif choice == "Boosts":
        boosts_frame.place(**frame_placement)
    elif choice == "Quests":
        quests_frame.place(**frame_placement)
    elif choice == "Settings":
        settings_frame.place(**frame_placement)

#zakładki / Tabs

menu = ctk.StringVar(value="Gathering")

segment_menu = ctk.CTkSegmentedButton(
    main_window,
    values=["Gathering", "Collect/Kill", "Boosts", "Quests", "Settings"],
    variable=menu,
    command=switch_tabs,
    font=('Arial', 15),
)
segment_menu.pack(pady=10)

gathering_frame = ctk.CTkFrame(
    main_window,
    width=980,
    height=530
)

kill_collect_frame = ctk.CTkFrame(
    main_window,
    width=980,
    height=530
)

boosts_frame = ctk.CTkFrame(
    main_window,
    width=980,
    height=530
)

quests_frame = ctk.CTkFrame(
    main_window,
    width=980,
    height=530
)

settings_frame = ctk.CTkFrame(
    main_window,
    width=980,
    height=530
)

#gathering frame 

gatheringtext = ctk.CTkLabel(
    gathering_frame,
    text="Gathering",
    font=('Arial', 20, 'bold')
)

gatheringtext.place(relx=0.5, rely=0.05, anchor="n")

#Kill/collect frame

kill_collect_text = ctk.CTkLabel(
    kill_collect_frame,
    text="Kill/Collect",
    font=('Arial', 20, 'bold')
)

kill_collect_text.place(relx=0.5, rely=0.05, anchor="n")

#boosts frame text

boosts_frame_text = ctk.CTkLabel(
    boosts_frame,
    text="Boosts",
    font=('Arial', 20, 'bold')
)

boosts_frame_text.place(relx=0.5, rely=0.05, anchor="n")

#Quests frame text

quests_frame_text = ctk.CTkLabel(
    quests_frame,
    text="Quests",
    font=('Arial', 20, 'bold')
)

quests_frame_text.place(relx=0.5, rely=0.05, anchor="n")

#settings frame text

settings_frame_text = ctk.CTkLabel(
    settings_frame,
    text="Settings",
    font=('Arial', 20, 'bold')
)

settings_frame_text.place(relx=0.5, rely=0.05, anchor="n")

switch_tabs("Gathering")

#settings frame (buttons etc etc)

hive = ctk.CTkComboBox(
    settings_frame,
    values=["1", "2", "3", "4", "5", "6"],
    state="readonly",
)

hive.set("Hive Slot")

autore = ctk.CTkCheckBox(
    settings_frame,
    text="Auto Rejoin",
)

discordlabel = ctk.CTkLabel(
    settings_frame,
    text="Discord",
    font=("Arial", 18, 'bold')
)

serversection = ctk.CTkLabel(
    settings_frame,
    text="Server",
    font=("Arial", 18, 'bold')
)

player = ctk.CTkLabel(
    settings_frame,
    text="Player",
    font=("Arial", 18, 'bold')
)

player_speed = ctk.CTkEntry(
    settings_frame,
    placeholder_text="Player Speed"
)

discord_webhookurl = ctk.CTkEntry(
    settings_frame,
    placeholder_text="Webhook URL"
)

testwebhook = ctk.CTkButton(
    settings_frame,
    text="Test Webhook"
)

sendscreen = ctk.CTkCheckBox(
    settings_frame,
    text="Send Screenshots"
)

min_counter = ctk.CTkComboBox(
    settings_frame,
    values=["5 Minutes", "10 Minutes", "15 Minutes"],
    state="readonly"
)

min_counter.set("5 Minutes")

def switch():
    if checkbox_var.get() == 1:
        server.configure(state="disabled")
    else:
        server.configure(state="normal")

checkbox_var = ctk.IntVar()

server = ctk.CTkEntry(settings_frame, placeholder_text="Private Server URL")

public = ctk.CTkCheckBox(
    settings_frame, 
    text="Public Server", 
    variable=checkbox_var, 
    command=switch
)

min_counter.place(x=100, y=380)
sendscreen.place(x=100, y=350)
testwebhook.place(x=100, y=410)
discordlabel.place(x=140, y=290)
serversection.place(x=140, y=170)
player.place(x=140, y=60)
public.place(x=100, y=230)
server.place(x=100, y=200)
discord_webhookurl.place(x=100, y=320)
player_speed.place(x=100, y=100)
hive.place(x=100, y=130)
autore.place(x=100, y=260)

#mainloop (nie tykać) / Mainloop (Dont touch)
main_window.mainloop()
