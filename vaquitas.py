import os
import random
import time
import threading

semaforo = threading.Semaphore(1)
inicioPuente = 10
largoPuente = 20

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.5)

  def avanzar(self):
    time.sleep(self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + "🐮")

  def run(self):

    while(True):
      if(self.posicion < inicioPuente):
        self.avanzar()
      if(self.posicion == inicioPuente):
        semaforo.acquire()
      self.avanzar()
      if(self.posicion == largoPuente + inicioPuente):
        semaforo.release()
        break
      
          
vacas = []
for i in range(5):
  v = Vaca()
  vacas.append(v)
  v.start()

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
  print(' ' * inicioPuente + '=' * largoPuente)

while(True):
  cls()
  print('-------->NO TE LAS COMAS!<--------')
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()
  for v in vacas:
    v.dibujar()
  dibujarPuente()
  time.sleep(0.2)
