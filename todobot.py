# coding=utf-8
import tweepy
import time
from threading import Timer
#from peewee import *
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)


toDoList = [
{'todo':'NO','fecha':'21/10:1', 'mensaje':'Comenzamos ToDoList #EBE15 #10EBE'},
{'todo':'SI','fecha':'21/10:55', 'titulo':'Storytelling y Big Data: las historias como conectores de la información','sala':'#VerdeEBE'},
{'todo':'SI','fecha':'21/11:25', 'titulo':'Growth Hacking y el crecimiento exponencial','sala':'#VerdeEBE'},
{'todo':'SI','fecha':'21/12:25', 'titulo':'Las claves para captar más potenciales clientes a través del Inbound Marketing','sala':'#VerdeEBE'},
{'todo':'SI','fecha':'21/12:55', 'titulo':'Instagram, la revolución social fotográfica cumple 5 años','sala':'#AmarillaEBE'},
{'todo':'SI','fecha':'21/13:25', 'titulo':'Entrega de Premios Instagram','sala':'#AmarillaEBE'},
{'todo':'SI','fecha':'21/16:25', 'titulo':'Web 2.0: nuevos usos y lenguaje para sumar personas a una marca y sus objetivos','sala':'#AmarillaEBE'},
{'todo':'SI','fecha':'21/16:55', 'titulo':'Social, móvil y vídeo, los tres retos del periodismo','sala':'#AzulEBE'},
{'todo':'SI','fecha':'21/17:25', 'titulo':'Tweets and data visualizations','sala':'#azulEBE'},
{'todo':'SI','fecha':'21/19:0', 'titulo':'Los avances que están por llegar de aquí a 2020','sala':'#AmarillaEBE'},
]

def maximoTexto(texto,max):
    if(len(texto) >= max):
        texto = texto[0:max -3]+"..."
        return texto
    else:
        return texto

def reloj():
    print "Creando el reloj"
    d = int(time.strftime("%d"))
    h = int(time.strftime("%I"))
    H = int(time.strftime("%H"))
    m = int(time.strftime("%M"))
    ts = int(time.time())
    fecha = "%s/%s:%s" %(d, H, m)
    print fecha
    for tarea in toDoList:
        if(tarea['fecha'] == fecha):
            if(tarea['todo'] == "SI"):
                msj = "Amo @jreyesgs le recuerdo que en 5 min. %s en sala %s #10EBE #EBE15" % (maximoTexto(tarea['titulo'],84),tarea['sala'])
                print msj
                api.update_status(status=msj)
                #api.send_direct_message(screen_name="jreyesgs", text=msj)
            else:
                msj = "Amo @jreyesgs, %s" % tarea['mensaje']
                print msj
                api.update_status(status=msj)
                #api.send_direct_message(screen_name="jreyesgs", text=msj)



    Timer(60.0, reloj).start()

reloj()
