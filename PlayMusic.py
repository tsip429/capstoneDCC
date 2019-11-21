
#! /usr/bin/python
import serial
import inspect
import time
from pygame import mixer
import pygame


arduino = serial.Serial("/dev/cu.usbmodem1421", 9600)
time.sleep(3)
rows = 10000
cols = 10000
comparison = [[0 for x in range(rows)] for y in range(cols)]
i = 0

def getData():
    data = ''
    while data.count(',') != 10:
 
        data = arduino.readline().strip() # reads in String
        print(data)
        data = data.decode('utf-8', "ignore")

    parsed_data = [int(x) for x in data.split(',')] # parses data and
    # converts to integers
    return parsed_data

def calm_or_pump(arr):
    for x in range(0,10):
            if arr[x][0] < arr[x - 1][0] and arr[x][0] < arr[x-2][0] and arr[x][1] > arr[x - 1][1] and arr[x][1] > arr[x-2][1]:
                return '/Users/tsiporastone/Desktop/Capstone Music/calm.mp3'
            elif arr[x][2] > arr[x - 1][2] and arr[x][2] > arr[x-2][2] and arr[x][3] > arr[x - 1][3] and arr[x][3] > arr[x-2][3]:
                return '/Users/tsiporastone/Desktop/Capstone Music/pump.mp3'

    return ''
    
 
for x in range(0,10):
    parsed_data = getData();
                                
    connection = parsed_data[0]
    attention = parsed_data[1]
    meditation = parsed_data[2]
    delta = parsed_data[3]
    theta = parsed_data[4]
    lowAlpha = parsed_data[5]
    highAlpha = parsed_data[6]
    lowBeta = parsed_data[7]
    highBeta = parsed_data[8]
    lowGamma = parsed_data[9]
    highGamma = parsed_data[10]

    # store a few consecutuve values of highAlpha and highBeta and
    # compare to each other
    # if high beta goes up and high alpha goes down - play calming music
    # if high beta drops - print "are you feeling calmer?"
    comparison[x][0] = highAlpha
    comparison[x][1] = highBeta
    comparison[x][2] = theta
    comparison[x][3] = delta

SONG_END = pygame.USEREVENT + 1

mixer.init()
mixer.music.set_endevent(SONG_END)
music_file = calm_or_pump(comparison)
print (music_file)
mixer.music.load(music_file)
mixer.music.play()
print ('hehre')
time.sleep(30)
print('yooo')
while True:
    for x in range(0,10):
        parsed_data = getData();
                                
        connection = parsed_data[0]
        attention = parsed_data[1]
        meditation = parsed_data[2]
        delta = parsed_data[3]
        theta = parsed_data[4]
        lowAlpha = parsed_data[5]
        highAlpha = parsed_data[6]
        lowBeta = parsed_data[7]
        highBeta = parsed_data[8]
        lowGamma = parsed_data[9]
        highGamma = parsed_data[10]

        # store a few consecutuve values of highAlpha and highBeta and
        # compare to each other
        # if high beta goes up and high alpha goes down - play calming music
        # if high beta drops - print "are you feeling calmer?"
        comparison[i][0] = highAlpha
        comparison[i][1] = highBeta
        comparison[i][2] = theta
        comparison[i][3] = delta
        if x > 1 and len(comparison) > 2:
            if comparison[x][0] < comparison[x - 1][0] and comparison[x][0] < comparison[x-2][0] and comparison[x][1] > comparison[x - 1][1] and comparison[x][1] > comparison[x-2][1]:
                music_file = '/Users/tsiporastone/Desktop/Capstone Music/calm2.mp3'
                mixer.init()       
                mixer.music.load(music_file)
                mixer.music.play()
                time.sleep(30)


            elif comparison[x][2] > comparison[x - 1][2] and comparison[x][2] > comparison[x-2][2] and comparison[x][3] > comparison[x - 1][3] and comparison[x][3] > comparison[x-2][3]:
                music_file = '/Users/tsiporastone/Desktop/Capstone Music/pump2.mp3'
                mixer.init()             
                mixer.music.load(music_file)
                mixer.music.play()
                time.sleep(30)

##            else:
##                quit()

       
 


            


        
    
    
 
