import time
import sys
import datetime
import keyboard

# keyboard.add_hotkey("ctrl+alt+j", lambda: print("ctrl+alt+j was pressed"))
isRunning = True

def arreter_horloge():
    global isRunning
    isRunning = not isRunning

keyboard.add_hotkey("space", lambda: arreter_horloge())

def regler_heure(tuple):
    return datetime.datetime(1,1,1, tuple[0], tuple[1], tuple[2])
    
def afficher_heure(tuple, format, alarme):
    global isRunning
    isRunning = True 
    if tuple == (0,0,0):
        time_start = datetime.datetime.now()
    else:
        time_start = regler_heure(tuple)
        
    time_alarm = regler_heure(alarme)
    
    if format:
        while isRunning:
            if time_start.time() == time_alarm.time():
                print(time_start.strftime("%I:%M:%S %p"), end="\r")
                sys.stdout.flush()
                print("Alarm!!!!!!Alarm!")
            else:
                print(time_start.strftime("%I:%M:%S %p"), end="\r")
                sys.stdout.flush()
            time_start += datetime.timedelta(seconds=1)
            time.sleep(1)
            
                
    else:
        while isRunning:
            if time_start.time() == time_alarm.time():
                print(time_start.strftime("%H:%M:%S"), end="\r")
                sys.stdout.flush()
                print("Alarm!!!!!!Alarm!")
            else:
                print(time_start.strftime("%H:%M:%S"), end="\r")
                sys.stdout.flush()
            time_start += datetime.timedelta(seconds=1)
            time.sleep(1)
    while not isRunning:
        continue
    time_start = (time_start.hour,time_start.minute, time_start.second)
    time_alarm = (time_alarm.hour,time_alarm.minute, time_alarm.second)
    afficher_heure(time_start,format,time_alarm)
        

        

am_pm = False
afficher_heure((0,0,0), am_pm, (14,50,30))

#Si le tuple est nul alors il nous affichera l'heure locale
# Pour régler am/pm ou 24h nous utilisons un booléen
# True pour am/pm; False pour le format 24h
# Le troisième parametre configure l'heure de l'alarme
# Avec al touche space vous pouvez stopper l'horloge

# L'alarme ne sonne pas lorsqu'on utilise l'argument tuple=(0,0,0)