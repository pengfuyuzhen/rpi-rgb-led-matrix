import pygame
import pygame.midi
import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit
import serial
from playsound import playsound


# instrument = 0
# note = 74
# volume = 127

# pygame.init()
# pygame.midi.init()

# for id in range(pygame.midi.get_count()):
#   print pygame.midi.get_device_info(id)

# port = 0
# midiOutput = pygame.midi.Output(port, 1)
# midiOutput.set_instrument(instrument)
# for note in range(0,127):
#   midiOutput.note_on(note,volume)
#   sleep(.25)
#   midiOutput.note_off(note,volume)
# del midiOutput
# pygame.midi.quit()



port = serial.Serial("/dev/ttyUSB0", baudrate=115200)

pygame.mixer.init(48000, -16, 1, 1024)

print "Songs Ready."

while True:

   try:
      rcv = port.readline()[:2]
      print rcv
      if (rcv == "DO"):
         pygame.mixer.music.load("newsounds/Do.mp3")
         pygame.mixer.music.play()
      if (rcv == "RE"):
         pygame.mixer.music.load("newsounds/Re.mp3")
         pygame.mixer.music.play()
      if (rcv == "MI"):
         pygame.mixer.music.load("newsounds/Mi.mp3")
         pygame.mixer.music.play()
      if (rcv == "FA"):
         pygame.mixer.music.load("newsounds/Fa.mp3")
         pygame.mixer.music.play()
      if (rcv == "SO"):
         pygame.mixer.music.load("newsounds/So.mp3")
         pygame.mixer.music.play()
      if (rcv == "LA"):
         pygame.mixer.music.load("newsounds/La.mp3")
         pygame.mixer.music.play()
      if (rcv == "TI"):
         pygame.mixer.music.load("newsounds/Ti.mp3")
         pygame.mixer.music.play()
      if (rcv == "B1"):
         pygame.mixer.music.load("newsounds/B1.mp3")
         pygame.mixer.music.play()
      if (rcv == "B2"):
         pygame.mixer.music.load("newsounds/B2.mp3")
         pygame.mixer.music.play()
      if (rcv == "B3"):
         pygame.mixer.music.load("newsounds/B3.mp3")
         pygame.mixer.music.play()
      if (rcv == "B4"):
         pygame.mixer.music.load("newsounds/B4.mp3")
         pygame.mixer.music.play()
      if (rcv == "B5"):
         pygame.mixer.music.load("newsounds/B5.mp3")
         pygame.mixer.music.play()
   except KeyboardInterrupt:
      exit()