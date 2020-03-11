# coding: utf-8
import socket
from datetime import datetime



class CentralCore():
    def __init__(self,instr,audio_de,end,port):
        self.cmd = instr
        self.cap_audio_de = audio_de
        self.porta = port
        self.endereco = end
        self.connecting(self.cmd,self.cap_audio_de)


    def connecting(self,adc,de):
        power_plug = socket.socket()
        power_plug.bind((self.endereco, self.porta))
        power_plug.listen(1)
        conn, addr = power_plug.accept()
        if 'cam' in adc:
            transferirCam(conn, adc,auth=de)
            conn.send('sair '.encode())

        elif 'audio' in adc:
            transferirAudio(conn, adc,auth=de)
            conn.send('sair'.encode())




datas = datetime.now()
file = "armazenar/{}-{}-{}_hora_{}:{}".format(datas.day, datas.month, datas.year, datas.hour, datas.minute)

def transferirCam(conn, cmd,auth):
    conn.send(cmd.encode())
    foto ="/home/jfc-me/Documentos/DevOps/ctrl_esp/fotos/{}_{}-{}-{}_hora_{}:{}".format(auth,datas.day, datas.month, datas.year, datas.hour, datas.minute)

    f = open(str(foto+'.jpeg'), 'wb')
    while True:
        bits = conn.recv(9000000)
        if bits.endswith('DONE'.encode('utf-8')):
            f.write(bits[:-4])
            f.close()
            print('Camera')
            break
        f.write(bits)

def transferirAudio(conn, cmd,auth):
    conn.send(cmd.encode())
    aud = "/home/jfc-me/Documentos/DevOps/ctrl_esp/audios/{}_{}-{}-{}_hora_{}:{}".format(auth,datas.day, datas.month, datas.year, datas.hour, datas.minute)
    f = open(str(aud+".wav"), 'wb')
    while True:
        bits = conn.recv(9000000)
        if bits.endswith('DONE'.encode('utf-8')):
            f.write(bits[:-4])
            f.close()
            print('Camera')
            break
        f.write(bits)

def transferirAudiVideo(conn, cmd):
    conn.send(cmd.encode())
    f = open(str(file + '.avi'), 'wb')
    while True:
        bits = conn.recv(9000000)
        if bits.endswith('DONE'.encode('utf-8')):
            f.write(bits[:-4])
            f.close()
            print('Camera')
            break
        f.write(bits)
