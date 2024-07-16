from tkinter import *
import tkinter as tk
from tkinter import Label
import customtkinter 
from tkinter import messagebox
import sys
import pygetwindow as gw
import pyautogui
import serial
import time
from serial.tools import list_ports 
from pywinauto import Application

arduino1_var = tk.BooleanVar()
arduino2_var = tk.BooleanVar()
arduino3_var = tk.BooleanVar()

def add_message(message):
    output_text.insert(END, message + "\n")
    output_text.see(END)
    
def detect_arduino_ports():
    arduino_ports = []
    ports = list_ports.comports()
    for port in ports:
        if 'Périphérique série USB' in port.description or 'Arduino Uno' in port.description:
            arduino_ports.append(port.device)
    if not arduino_ports:
              print("Aucun Arduino détecté.\n")
    return arduino_ports
#while True:
arduino_ports = detect_arduino_ports()

if arduino_ports:
 
    serial_connections = {}
    for idx, port in enumerate(arduino_ports):
        ser = serial.Serial(port, 9600, timeout=0.1)
        serial_connections[f"Posage_{idx+1}"] = ser
        print(f"Posage_{idx+1} connectée sur {port}\n")
        
        time.sleep(1)
        #break
else:
    print("Aucun Arduino détecté. En attente de connexion...")
    #sys.exit() 

def reconnect_arduino():
    global arduino_ports, serial_connections
    while not arduino_ports:
        print("Aucun Arduino détecté. Tentative de reconnexion...")
        arduino_ports = detect_arduino_ports()
        if arduino_ports:
            serial_connections = {}
            for idx, port in enumerate(arduino_ports):
                ser = serial.Serial(port, 9600, timeout=0.1)
                serial_connections[f"Posage_{idx+1}"] = ser
                time.sleep(1)
            print("Arduino reconnecté avec succès.")
        else:
            time.sleep(5)  # Attendre 5 secondes avant de réessayer la détection de l'Arduino

# Vérifier la détection de l'Arduino au démarrage
arduino_ports = detect_arduino_ports()
if not arduino_ports:
    print("Aucun Arduino détecté. En attente de connexion...")
    reconnect_arduino()

def activate_renesas():
    renesas_window_title = ("Renesas Flash Programmer (Unsupported Freeware Version)")
    renesas_window = gw.getWindowsWithTitle(renesas_window_title)
    if len(renesas_window) > 0:
        renesas_window[0].activate()
        pyautogui.press("space")
        add_message("connect E1..\n")



def activate_IS01():
    renesas_window_title = ("SUPERPRO IS01")
    renesas_window = gw.getWindowsWithTitle(renesas_window_title)
    if len(renesas_window) > 0:
        renesas_window[0].activate()
        app = Application(backend="uia").connect(title="SUPERPRO IS01")
        main_window =app.window(title="SUPERPRO IS01")
        auto_button = main_window.child_window(title="Auto", control_type="Button")
        auto_button.click()
        
        
        time.sleep(2)
       

def activate_mplab():
    mplab_window_title = "MPLAB X IPE v5.30" 
    mplab_window = gw.getWindowsWithTitle(mplab_window_title) 
    if len(mplab_window) > 0: 
        mplab_window[0].activate()
        pyautogui.click()

positions = []

def get_mouse_position1():
    time.sleep(2)
    x, y = pyautogui.position()
    positions.append((x, y)) 
    add_message("instance 1 detectée  - X: {}, Y: {}\n".format(x, y))


def get_mouse_position2():
    time.sleep(2)
    x, y = pyautogui.position()
    position.append((x, y))
    add_message("instance 2 detectée  - X: {}, Y: {}\n".format(x, y))

def get_mouse_position3():
    time.sleep(2)
    x, y = pyautogui.position() 
    position3.append((x, y))
    add_message("instance 3 detectée  - X: {}, Y: {}\n".format(x, y))

    
def instance1():
     
    for pos in positions: 
        x, y = pos 
       
        pyautogui.moveTo(x, y)
        #time.sleep(2)
        pyautogui.click()  
        pyautogui.press("space") 
        add_message("START..\n")

position = [] 
def instance2():
     
    for poss in position: 
        x, y = poss
        pyautogui.moveTo(x, y)
        
        #time.sleep(1)  # Attendre 1 seconde
        pyautogui.click()  # Cliquer à la position actuelle
        pyautogui.press("space")
        add_message("START..\n")
 

position3 = []
def instance3():
   
    
    for posss in position3: 
        x, y = posss
        
        pyautogui.moveTo(x, y)
        pyautogui.click() 
        pyautogui.press("space") 
        add_message("START..\n")
       

for arduino_name, ser in serial_connections.items():
  if arduino_name == "Arduino_1" and arduino1_var.get() or arduino_name == "Arduino_1" and arduino1_var.get() or arduino_name == "Arduino_1" and arduino1_var.get() :
   def rotate_motor_cw():
    # Envoyer la commande pour faire tourner le moteur dans le sens horaire
    ser.write(b"CW\n")
    add_message("le moteur tourne dans le sens horaire...\n")

   def rotate_motor_cw_pulse():
    # Envoyer la commande pour faire tourner le moteur dans le sens horaire
    ser.write(b"CW+\n")
    add_message("le moteur accelére dans le sens horaire...\n ")

  def rotate_motor_ccw():
    add_message("le moteur tourne dans le sens antihoraire...\n ")
    # Envoyer la commande pour faire tourner le moteur dans le sens antihoraire
    ser.write(b"CCW\n")

  def rotate_motor_ccw_pulse():
    # Envoyer la commande pour faire tourner le moteur dans le sens antihoraire
    ser.write(b"CCW+\n")
    add_message("le moteur accelére dans le sens antihoraire...\n ")

  def stop_motor():
    # Envoyer la commande pour faire tourner le moteur dans le sens antihoraire
    ser.write(b"STOP\n")
    add_message("le moteur est en mode veille!\n ")

  def set_Delay():
    in_delay = delay_Var.get()  # Récupérer la valeur du délai depuis l'entrée
    command = 'SET_DELAY ' + in_delay + '\n'
    ser.write(command.encode())
    add_message("mise à jour temps de programmation \n ")


    
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")
root=customtkinter.CTk()
root.geometry("670x630")

  
root.title("Watts Programmation App ")
  
def changeMode():
    val=switch.get()
    if val:
        customtkinter.set_appearance_mode("dark")
    else: 
      customtkinter.set_appearance_mode("light")
setting_window = None

    
def on_button_click():
    choice= app_choice.get()
    if choice == "renesas":
        activate_renesas()
    elif choice == "mplab":
        activate_mplab()

    elif choice == "ISO1":
        activate_IS01()
    



app_choice = StringVar()
app_choice.set("renesas")  # Choix par défaut
full_mode = StringVar()

arduino1_var = tk.BooleanVar()
arduino2_var = tk.BooleanVar()
arduino3_var = tk.BooleanVar()

operator_id_var = tk.StringVar()
delay_Var = tk.StringVar()
quantite_var = tk.StringVar()


pass_count = 0
fail_count = 0


  
    
frame_outil = customtkinter.CTkFrame(root,)
frame_outil.pack( pady=5,ipady=3,ipadx=50, fill=X )


   

frame_operate = customtkinter.CTkFrame(root,)#"#0476e0"
frame_operate.pack(side=LEFT, ipady=100,ipadx=10,pady=8,padx=5, anchor=NE,fill=Y)#  pady=5,ipady=3,ipadx=20,
jog_controller =customtkinter.CTkFrame(frame_operate,border_width=3,width=200 )#"#0476e0"
jog_controller.place(x=10,y=320)
setting = customtkinter.CTkFrame(frame_operate,border_width=3,width=200,height=250 )#"#0476e0"
setting.place(x=10,y=50)




def open_setting_frame():
    global setting_window  # Déclarer setting_window comme globale pour pouvoir l'utiliser dans la fonction
    setting_window = tk.Toplevel(root)
    setting_frame = tk.Frame(setting_window, width=300, height=300)
    setting_frame.pack()
    
    operator_id = customtkinter.CTkEntry(setting_frame, width=120, height=20, textvariable=operator_id_var)
    operator_id.place(x=100, y=50)
    operator_id_label = customtkinter.CTkLabel(setting_frame, text="Operatore ID", text_color="Black")
    operator_id_label.place(x=10, y=50)

    delay= customtkinter.CTkEntry(setting_frame, width=120, height=20, textvariable=delay_Var)
    delay.place(x=100, y=100)
    delay_label = customtkinter.CTkLabel(setting_frame,text="Delay Prog")
    delay_label.place(x=10, y=100)

    quantite_entry = customtkinter.CTkEntry(setting_frame, width=120, height=20, textvariable=quantite_var)
    quantite_entry.place(x=100, y=150)
    quantite_label = customtkinter.CTkLabel(setting_frame, text="Nb Total", text_color="Black")
    quantite_label.place(x=10, y=150)

    ok_button = customtkinter.CTkButton(setting_frame, text="Insert", command=lambda: insert_data())
    ok_button.place(x=90, y=190)
    ok_button = customtkinter.CTkButton(setting_frame, text="Apply", command=set_Delay )
    ok_button.place(x=90, y=220)

def insert_data():
    operator_id_value = operator_id_var.get()
    delay_value = delay_Var.get()
    quantite_value = quantite_var.get()

    operator_id1.delete(1.0, END)
    operator_id1.insert(END, operator_id_value)
    of1.delete(1.0, END)
    of1.insert(END, delay_value)
   
    
    quantite1.delete(1.0, END)
    quantite1.insert(END, quantite_value)

    setting_window.destroy()  # Fermer la fenêtre des paramètres






def open_debug_window():
    # Créer une nouvelle fenêtre Toplevel pour le mode Debug
    debug_window = tk.Toplevel()
    debug_window.title("Fenêtre de Debug")
    debug_window.geometry("400x250")  # Taille de la fenêtre
    
    # Ajouter des widgets à la fenêtre de debug si nécessaire
    label = tk.Label(debug_window, text="Bienvenue dans le mode Debug! ")
    label.pack(pady=20)
     
    cw = tk.Button(debug_window, text=">>",borderwidth=5,fg= "green", command= rotate_motor_cw, )
    cw.place(x=200, y= 85)
    ccw = tk.Button(debug_window, text="<<",borderwidth=5, fg= "green", command= rotate_motor_ccw)
    ccw.place(x=110, y= 85)
    cw_pulse = tk.Button(debug_window, text="<<<<",borderwidth=5,fg= "green", command= rotate_motor_ccw_pulse)
    cw_pulse.place(x=40, y= 85)
    ccw_pulse = tk.Button(debug_window, text=">>>>",borderwidth=5,fg= "green", command= rotate_motor_cw_pulse)
    ccw_pulse.place(x=280, y=85)
    STOP_button = tk.Button(debug_window, text=" STOP ",borderwidth=5,width=10, fg= "red",command= stop_motor)
    STOP_button.place(x=140, y= 130)


    ok_button = tk.Button(debug_window, text=" terminer ",borderwidth=5, command= debug_window.destroy)
    ok_button.place(x=295, y= 210)


 
setting_button = tk.Button(frame_operate, text="Setting",borderwidth=5, command= open_setting_frame)
setting_button.place(x=15, y= 2)


debug_button = tk.Button(frame_operate, text="Programing",borderwidth=5, command= open_debug_window )
debug_button.place(x=70, y= 2)

#program_choice_menu = customtkinter.CTkOptionMenu(root, values=["*choix du prog*", "programmation", "Debug"])
#program_choice_menu .place(x=20, y=400)





operator_id1 = customtkinter.CTkTextbox(setting, width=90, height=20)
operator_id1.place(x=100, y=30)
operator_id_label = customtkinter.CTkLabel(setting, text="Operatore ID")
operator_id_label.place(x=10, y=30)

of1 = customtkinter.CTkTextbox(setting, width=80, height=20)
of1.place(x=100, y=90)
of_label = customtkinter.CTkLabel(setting, text="Delay")
of_label.place(x=20, y=90)
#button = tk.Button(frame_operate, text="Ok", command=set_Delay)
#button.place(x=50, y=200)

quantite1 = customtkinter.CTkTextbox(setting, width=80, height=20)
quantite1.place(x=100, y=140)
quantite_label = customtkinter.CTkLabel(setting, text="Nb Total")
quantite_label.place(x=10, y=140)

operator_id2 = customtkinter.CTkTextbox(setting, width=80, height=20)
operator_id2.place(x=100, y=200)
quantite_label2 = customtkinter.CTkLabel(setting, text="carte Ok")
quantite_label2.place(x=10, y=200)








button = tk.Button(jog_controller, text="instance 1", command=get_mouse_position1)
button.place(x=40,y=40)
button = tk.Button(jog_controller, text="instance 2", command=get_mouse_position2)
button.place(x=40,y=85)
button = tk.Button(jog_controller, text="instance 3", command=get_mouse_position3)
button.place(x=40,y=130)
switch = customtkinter.CTkSwitch(jog_controller,text= "Dark Mode",
                                 onvalue=1,
                                 offvalue=0,
                                 command=changeMode
                                 )
switch.place(x=25,y=170)






def checkbox_event():
    output_text.insert(END, f"Mode deux posages: {check_var.get()}\n")

check_var = customtkinter.StringVar(value="off")
checkbox = customtkinter.CTkCheckBox(jog_controller, text="change mode", command=checkbox_event,
                                      variable=check_var, onvalue="on", offvalue="off", hover=True)
checkbox.place(x=25 , y = 10)
 


#def clear_output():
#    output_text.delete('1.0', END)

frame_out = customtkinter.CTkFrame(root, width=420, height=220,  )
frame_out.pack(pady=10,padx=10,ipady=30,ipadx=50)
output_text = customtkinter.CTkTextbox(frame_out,border_width=5,width=320,height=230,activate_scrollbars= True,font=("Arial", 14))
output_text.place(x=48, y=32)
Outputlabel = Label(frame_out, text="Output Panel", font="calibre 15 ")
Outputlabel.place(x=1, y=1 )
#clear_button = customtkinter.CTkButton(frame_out, text="Clear Output", command=clear_output)
#clear_button.place(x=227, y=229)

def check_output_messages():
    if output_text.get("1.0", "end-1c") == "":  # Vérifier s'il n'y a pas de messages actuellement
        output_text.insert(END, "Positionner la carte comme illustré  dans la photo.\n")

statistics= customtkinter.CTkFrame(root, width=320, height=60, )#fg_color="#0476e0"
statistics.pack(pady=5,padx=10,ipady=30,ipadx=50) 
label=customtkinter.CTkLabel(statistics,text="Statistics")
label.place(x=20, y= 1 )
pass_label=customtkinter.CTkLabel(statistics, text=" 0%")
pass_label.place(x=325, y= 35 )
fail_label=customtkinter.CTkLabel(statistics, text=" 0%")
fail_label.place(x=325, y= 75 )
pass_l=customtkinter.CTkLabel(statistics,text="PASS")
pass_l.place(x=45, y= 35 )
fail_l=customtkinter.CTkLabel(statistics,text="FAIL")
fail_l.place(x=45, y= 75 )
c_Pass=customtkinter.CTkProgressBar(statistics,mode= "determinate",progress_color="green")
c_Pass.place(x=120, y= 40)
c_Pass["maximum"] = 100
c_fail=customtkinter.CTkProgressBar(statistics,mode= "determinate",progress_color="red")
c_fail.place(x=120, y= 80)

jog= customtkinter.CTkFrame(root, width=320, height=60, )#fg_color="#0476e0"
jog.pack(pady=5,padx=10,ipady=20,ipadx=50)
label=customtkinter.CTkLabel(jog,text="Jog Controller")
label.place(x=20, y= 1 )
Posagr1_check = tk.Checkbutton(jog, text="Posage 1", variable=arduino1_var)
Posagr1_check.place(x=30, y= 80)

Posagr2_check = tk.Checkbutton(jog, text="Posage 2", variable=arduino2_var)
Posagr2_check.place(x=180, y= 80)

Posagr3_check = tk.Checkbutton(jog, text="Posage 3", variable=arduino3_var)
Posagr3_check.place(x=330, y= 80)

cw = tk.Button(jog, text=">>",borderwidth=5,fg= "green", command= rotate_motor_cw, )
cw.place(x=265, y= 35)
ccw = tk.Button(jog, text="<<",borderwidth=5, fg= "green", command= rotate_motor_ccw)
ccw.place(x=95, y= 35)
cw_pulse = tk.Button(jog, text="<<<<",borderwidth=5,fg= "green", command= rotate_motor_ccw_pulse)
cw_pulse.place(x=25, y= 35)
ccw_pulse = tk.Button(jog, text=">>>>",borderwidth=5,fg= "green", command= rotate_motor_cw_pulse)
ccw_pulse.place(x=320, y=35)
STOP_button = tk.Button(jog, text=" STOP ",borderwidth=5,width=10, fg= "red",command= stop_motor)
STOP_button.place(x=152, y= 35)






frame_renesas = Frame(frame_outil, borderwidth=5, relief="groove") 
frame_renesas.pack(pady=10,side=LEFT,  expand=True)
button_renesas = Radiobutton(frame_renesas, text=" Renesas", value="renesas", variable=app_choice, font=20)
button_renesas.grid(row=1)



frame_mplab = Frame(frame_outil, borderwidth=5, relief="groove")
frame_mplab.pack(pady=10, side=LEFT,  expand=True)
button_mplab = Radiobutton(frame_mplab, text="MPLAB", value="mplab", variable=app_choice, font=20)
button_mplab.grid(row=2)
    
frame_ISO1 = Frame(frame_outil, borderwidth=5, relief="groove")
frame_ISO1.pack(pady=10, side=LEFT,  expand=True)
button_ISO1 = Radiobutton(frame_ISO1, text="ISO1", value="ISO1", variable=app_choice, font=20)
button_ISO1.grid(row=3)

frame_flasheur = Frame(frame_outil, borderwidth=5, relief="groove")
frame_flasheur.pack(pady=10, side=LEFT, expand=True)
button_flasheur = Radiobutton(frame_flasheur, text="flasher", value="flasher", variable=app_choice, font=20)
button_flasheur.grid(row=4)

original_renesas_color = button_renesas.cget("background")
original_mplab_color = button_mplab.cget("background")

def change_color_green(*args):
        if app_choice.get() == "renesas":
            button_renesas.config(background="green", fg="white")
            button_mplab.config(background=original_mplab_color, fg="black")
            button_ISO1.config(background=original_mplab_color, fg="black")
            button_flasheur.config(background=original_mplab_color, fg="black")
        elif app_choice.get() == "mplab":
            button_mplab.config(background="green", fg="white")
            button_renesas.config(background=original_renesas_color, fg="black" )
            button_ISO1.config(background=original_mplab_color, fg="black")
            button_flasheur.config(background=original_mplab_color, fg="black")
        elif app_choice.get() == "ISO1":
            button_ISO1.config(background="green", fg="white")
            button_renesas.config(background=original_renesas_color, fg="black")
            button_mplab.config(background=original_mplab_color, fg="black")
            button_flasheur.config(background=original_renesas_color, fg="black")
        elif app_choice.get() == "flasher":
            button_flasheur.config(background="green", fg="white")
            button_renesas.config(background=original_renesas_color, fg="black")
            button_mplab.config(background=original_mplab_color, fg="black")
            button_ISO1.config(background=original_renesas_color, fg="black")

app_choice.trace("w", change_color_green)  # Enregistrer la fonction de changement de couleur






counter = -1

def update_counter():
 global counter
 counter += 1
 operator_id2.delete("1.0", END)
 operator_id2.insert("1.0", str(counter))

pass_percentage = 0
fail_percentage = 0

pass_count = 0
fail_count = 0

def update_statistics(result):
    global pass_count, fail_count
    if result == "PASS":
        pass_count += 1
    elif result == "FAIL":
        fail_count += 1

    total_count = pass_count + fail_count
    pass_percentage = (pass_count / total_count) * 100 if total_count > 0 else 0

    fail_percentage = (fail_count / total_count) * 100 if total_count > 0 else 0
    c_Pass.set(pass_percentage)
    c_fail.set(fail_percentage)


    pass_label.configure(text=f" {pass_percentage:.0f}%")
    fail_label.configure(text=f" {fail_percentage:.0f}%")
    

    root.after(1000, lambda: update_statistics(result))


def check_arduino_command():
    for key, ser in serial_connections.items():
     if ser.in_waiting > 0:
            received_data = ser.readline().decode().strip()
           # output_text.insert(END ,f"Commande reçue de {key}: {received_data}\n")
            
            if received_data == 'START' and check_var.get() == "off"  :
                print("mode seul application ") 
                on_button_click()
                update_counter()
                update_statistics("PASS")

                add_message("Programmation en cours...\n")
                add_message("10%\n")
                add_message("20%\n")
                add_message("30%\n")
                add_message("40%\n")
                add_message("50%\n")
                add_message("60%\n")
                add_message("70%\n")
                add_message("80%\n")
                add_message("90%\n")
                add_message("100%\n")
                add_message("PASS\n")
            elif    check_var.get() == "on" : 
             
             
             if key == "Posage_1"  :
              if received_data == "START":
                instance1()
                add_message( "Posage 1 en cours...\n10%\n20%\n30%\n40%\n50%\n60%\n70%\n80%\n90%\n100%\nFin de Programmation\n")
                update_counter() 
                update_statistics("PASS")      
                

             elif key == "Posage_2" :
                if received_data == "START":
                    instance2() 
                    add_message( "Posage 2 en cours...\n10%\n20%\n30%\n40%\n50%\n60%\n70%\n80%\n90%\n100%\nFin de Programmation\n")
                    update_counter()
                    update_statistics("PASS")      
             elif key == "Posage_3" :
                if received_data == "START":
                    instance3()
                    add_message("Posage 3 en cours...\n10%\n20%\n30%\n40%\n50%\n60%\n70%\n80%\n90%\n100%\nFin de Programmation\n")
                    update_counter()
                    update_statistics("PASS")        

     #else:
      #    output_text.insert(END, "Commande non reconnue de l'Arduino.\n")
    
    root.after(100, check_arduino_command)  # Appel récursif pour vérifier périodiquement les commandes de l'Arduino

root.after(100, check_arduino_command)  # Démarrer la vérification des commandes de l'Arduino
root.after(1000, update_counter)  # Démarrer la mise à jour du compteur
root.mainloop()