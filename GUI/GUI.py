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

min_counter.place(x=300, y=160)
sendscreen.place(x=300, y=130)
testwebhook.place(x=300, y=200)
discordlabel.place(x=340, y=60)
serversection.place(x=140, y=180)
player.place(x=140, y=60)
public.place(x=100, y=250)
server.place(x=100, y=220)
discord_webhookurl.place(x=300, y=100)
player_speed.place(x=100, y=100)
hive.place(x=100, y=140)
autore.place(x=100, y=280)

#gathering GUI

gather_label = ctk.CTkLabel(
    gathering_frame,
    text="Gather",
    font=("Arial", 18, 'bold')
)

field = ctk.CTkComboBox(
    gathering_frame,
    values=["Dandelion Field", "Sunflower Field", "Mushroom Field", "Blue Flower Field", "Clover Field",
    "Strawberry Field", "Spider Field", "Bamboo Field", "Pineapple Patch", "Stump Field", "Cactus Field",
    "Pumpkin Patch", "Pine Tree Forest", "Rose Field", "Mountain Top Field", "Pepper Patch", "Coconut Field"],
    state="readonly"
)

field.set("Dandelion Field")

where_field = ctk.CTkComboBox(
    gathering_frame,
    values=["Center", "Upper Right Corner", "Upper Left Corner", "Lower Right Corner", "Lower Left Corner"],
    state="readonly"
)

where_field.set("Center")

pattern = ctk.CTkComboBox(
    gathering_frame,
    values=["Zigzag", "Circle"],
    state="readonly"
)

pattern.set("Zigzag")

gather_time = ctk.CTkComboBox(
    gathering_frame,
    values=("5 Minutes", "10 Minutes", "15 Minutes", "20 Minutes"),
    state="readonly"
)

gather_time.set("5 Minutes")

return_to_hive = ctk.CTkCheckBox(
    gathering_frame,
    text="Return To Hive"
)

active_seconds = 0

is_on = False

def timer():
    global active_seconds

    if is_on:
        active_seconds += 1
        hours = active_seconds // 3600
        minutes = (active_seconds % 3600) // 60
        seconds = active_seconds % 60
        timerlabel.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        main_window.after(1000, timer)

def change_color():
    global is_on, active_seconds

    if is_on == False:
        active_seconds = 0
        timerlabel.configure(text="00:00:00")

        status.configure(
            fg_color="green",
            hover_color="red",
            text="Running"
        )

        is_on = True
        timer()

    else:
        status.configure(
            fg_color="red",
            hover_color="green",
            text="Click To Start"
        )

        is_on = False

status = ctk.CTkRadioButton(
    gathering_frame,
    fg_color="red",
    text="Click To Start",
    hover_color="green",
    command=change_color
)

timerlabel = ctk.CTkLabel(
    gathering_frame,
    text="00:00:00"
)

gather_label.place(x=140,y=60)
field.place(x=100, y=100)
where_field.place(x=100, y=140)
pattern.place(x=100, y=180)
gather_time.place(x=100, y=220)
return_to_hive.place(x=100, y=260)
status.place(x=25, y=500)
timerlabel.place(x=150, y=500)

#mainloop (nie tykać) / Mainloop (Dont touch)
main_window.mainloop()
