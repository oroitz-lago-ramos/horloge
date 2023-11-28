import time
import sys
import datetime

def arreter_horloge():
    pass

def regler_heure(tuple):
    return datetime.datetime(1,1,1, tuple[0], tuple[1], tuple[2])
    
def afficher_heure(tuple, format):
    if tuple == (0,0,0):
        time_start = datetime.datetime.now()
    else:
        time_start = datetime.datetime(1,1,1, tuple[0], tuple[1], tuple[2])
        
    time_alarm = regler_heure((14,6,2))
    
    if format:
        while True:
            if time_start == time_alarm:
                print(time_start.strftime("%I:%M:%S %p"), end="\r")
                sys.stdout.flush()
                print("Alarm!!!!!!Alarm!")
            else:
                print(time_start.strftime("%I:%M:%S %p"), end="\r")
                sys.stdout.flush()
            time_start += datetime.timedelta(seconds=1)
            time.sleep(1)
    else:
        while True:
            if time_start == time_alarm:
                print(time_start.strftime("%H:%M:%S"), end="\r")
                sys.stdout.flush()
                print("Alarm!!!!!!Alarm!")
            else:
                print(time_start.strftime("%H:%M:%S"), end="\r")
                sys.stdout.flush()
            time_start += datetime.timedelta(seconds=1)
            time.sleep(1)

am_pm = True
afficher_heure((12,59,55), am_pm)

#Si le tuple est nul alors il nous affichera l'heure locale
# Pour régler am/pm ou 24h nous utilisons un booléen
# True pour am/pm; False pour le format 24h