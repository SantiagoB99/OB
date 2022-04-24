import time

print('Son las:', time.localtime().tm_hour,":", time.localtime().tm_min)

if(time.localtime().tm_hour<19):
    print("Aun quedan", 18-time.localtime().tm_hour, "horas", 59-time.localtime().tm_min, "minutos de trabajo")
else:
    print("Puedes irte a casa")