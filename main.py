# Visualization of Tower of Hanoi with Python and package Turtle
# Filip Nachtman 27/11/2022
# For example - 7 discs -> can be adjusted where *** appear
# V této práci jsem vycházel z mé znalosti package turtle v jazyce python -> dříve, jsem již dělal "grafiku" v pythonu, jakožto pracovní projekt

import turtle
import time  # adjust speed

#GUI of app
win = turtle.Screen()
win.setup(800, 600)
win.title('Tower of Hanoi - Algoritmy')
win.bgpic('giphy.gif')
win.tracer(0)

#GUI of base for 3 pins with x discs
base = turtle.Turtle()
base.color('light grey')
base.shape('square')
base.up()
base.goto(0, -200)
base.shapesize(1, 35)


# class for GUI of 3 pins
class Pin(turtle.Turtle):

  def __init__(self, xpos):

    
      super().__init__(shape='square')
      self.xpos = xpos
      self.up()
      self.color('light grey')
      self.shapesize(10, 1)
      self.goto(self.xpos, -100)
      self.count = 0
      self.pos_list = [-180, -160, -140, -120, -100, -80, -60, -40]
      self.discs = []


# class for GUI of x discs
class Disk(turtle.Turtle):

  def __init__(self, xpos, ypos, size, color):
    super().__init__(shape='square')
    self.xpos = xpos
    self.ypos = ypos
    self.size = size
    self.color(color)
    self.up()
    self.shapesize(1, self.size)
    self.goto(self.xpos, self.ypos)

# def pro pohyb disků -> zde zajištuji přesun na základě velikosti platformy, která se pohybuje -> ale vychází to s tále z níže popsaného algoritmu 
    
#  def hanoi(n, a, h, b):
#  if n == 0:  # zabranuje kodu v hýbaní pokud počet disků je 0.
#    pass
#  else:
#    hanoi(n - 1, a, b, h)  
#    move(a, b)  
#    hanoi(n - 1, h, a, b)  

def move_disc(disk, pin):
  while disk.ycor() < 100:
    disk.goto(disk.xcor(), disk.ycor() + 5)
    win.update()
  disk.goto(pin.xcor(), 100)
  win.update()
  while disk.ycor() > pin.pos_list[pin.count]:
    disk.goto(disk.xcor(), disk.ycor() - 5)
    win.update()
  time.sleep(0.5)  
  # rychlost přemisťování disků v simulaci 


def move(a, b):
  print(f'Move disc from {a} to {b}!')
  if a == 'A':
    top_disc = pin1.discs[-1]
    start_pin = pin1
  elif a == 'B':
    top_disc = pin2.discs[-1]
    start_pin = pin2
  elif a == 'C':
    top_disc = pin3.discs[-1]
    start_pin = pin3

  if b == 'A':
    pin = pin1
  elif b == 'B':
    pin = pin2
  elif b == 'C':
    pin = pin3

  move_disc(top_disc, pin)
  start_pin.count -= 1
  start_pin.discs.pop()
  pin.count += 1
  pin.discs.append(top_disc)



def hanoi(n, a, h, b):
  if n == 0:  # zabranuje kodu v hýbaní pokud počet disků je 0.
    pass
  else:
    hanoi(n - 1, a, b, h)  
    move(a, b)  
    hanoi(n - 1, h, a, b)  

    # Rekurzivní řešení -> musí obsahovat nejméně jeden tah = přesun největšího kotouče (n=1).
    # Nejprve přesuneme (n-1) kotoučů (všechny kromě největšího) -> na pomocnou věž.
    # Dále vezmeme největši na koncovou věž a opaakujeme první krok.
    # Zbytek (n-1) z odkladací věže přesuneme na cílovou.
    # Algoritmus je všeobecně znám. 

pin1 = Pin(-200)
pin2 = Pin(0)
pin3 = Pin(200)



#***
disk1 = Disk(-200, -180, 11, 'light green')
disk2 = Disk(-200, -160, 9.5, 'green')
disk3 = Disk(-200, -140, 8, 'light blue')
disk4 = Disk(-200, -120, 6.5, 'blue')
disk5 = Disk(-200, -100, 5, 'dark blue')
disk6 = Disk(-200, -80, 3.5, 'purple')
disk7 = Disk(-200, -60, 2, 'pink')



#***
pin1.count = 7
pin1.discs = [disk1, disk2, disk3, disk4, disk5, disk6, disk7]


#***
hanoi(7, 'A', 'B', 'C')


# time complexity O(2^n - 1)
# 7 disků -> 127 přesunů
# 6 disků -> 63 přesunů
# 5 disků -> 31 přesunů
# 4 disky -> 15 přesunů
# 3 disky -> 7 přesunů
# 2 disky -> 3 přesuny
# 1 disk ->1 přesun 
