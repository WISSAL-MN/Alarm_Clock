import datetime
from playsound import playsound 
alarmHour = int(input("Enter Hour :"))
alarmMin  = int(input("Enter Minutes :"))
alarmAm   = int(input("am/ pm:"))
# le module Date time donne l'heure au format 24 heures
# donc je doit ajouter12h a l'heure de l'larm s'il sagit de l'heur de laprès-midi
if alarmAm  == "pm":
    alarmHour = alarmHour+12
while  True:
    if alarmHour == datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("Playing..") 
        playsound("Creepy-clock-chiming.mp3")
        break