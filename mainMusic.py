import os
from pickle import TRUE
import sys
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal


# pyaudio documentation: https://people.csail.mit.edu/hubert/pyaudio/docs/ and https://people.csail.mit.edu/hubert/pyaudio/

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def option1():
    global output
    cls()
    print("Choose waveform type")
    print("1) Sine wave")
    print("2) Square wave")
    print("3) Sawtooth wave")
    print("4) Triangle wave")
    print("5) Return to main menu")
    wave = input()
    match wave:
        case '1':
            cls()
            print("Wave changed to sine wave")
            print("Press enter to return to main menu")
            input()
        case '2' :
            cls()
            print("Wave changed to square wave")
            print("Press enter to return to main menu")
            input()
        case '3' :
            cls()
            print("Wave changed to sawtooth wave")
            print("Press enter to return to main menu")
            input()
        case '4' :
            cls()
            print("Wave changed to triangle wave")
            print("Press enter to return to main menu")
            input()
        case '5': 
            __name__ == "__main__" # return to main menu
        case _:
            cls()
            print("The input value is not valid. Please try again.") # report invalid input
            input()
            option1() # return to wave menu
    

def option2():
    global output
    cls()
    print("1) Change volume")
    print("2) Return to main menu")
    choose = input()
    match choose:
        case '1':
            cls()
            print("Increase or decrease loudness by decibels")
            dbIn = input()
            try:
                dbIn = int(dbIn) #convert input into int
                if dbIn > 0:
                    cls()
                    print("Volume increased by", dbIn) # tell user volume increased by specified db
                    print("Press enter to return to main menu")
                    input()
                if dbIn < 0:
                    cls()
                    print("Volume decreased by", dbIn) # tell user volume decreased by specified db
                    print("Press enter to return to main menu")
                    input()
            except ValueError:
                cls()
                print("Please input a number") # if input isn't number give error
                input()
                option2() # return to bpm menu
            else:
                db = dbIn
        case '2': 
                __name__ == "__main__" # return to main menu

def option3():
    global output # make abc file a global variable so other functions can access it
    global filePath
    cls()
    print("1) Set ABC file path")
    print("2) Return to main menu")
    choose = input()
    match choose:
        case '1':
            cls()
            print("Please input file path")
            filePath = input()
            if filePath.endswith('.abc'):
                output = wav
            elif filePath.endswith('.abc"'):
                filePath = filePath.replace('"', "") # remove apostrophes from any imput
                output = wav
            else:
                print("Not a valid file")
                input()
                option3()
            
        case '2':
             __name__ == "__main__" # return to main menu

def option4():
    global output
    cls()
    print("1) Set BPM (Speed)")
    print("2) Return to main menu")
    select = input()
    match select:   
        case '1':
            cls()
            print("Please input bpm")
            bpmIn = input()
            try:
                bpmIn = int(bpmIn) #convert input into int
                cls()
                print("BPM set to", bpmIn) # tell user the bpm changed
                print("Press enter to return to main menu")
                input()
            except ValueError:
                cls()
                print("Please input a number") # if input isn't number give error
                input()
                option4() # return to bpm menu
            else:
                bpm = bpmIn
        case '2': 
                __name__ == "__main__" # return to main menu
        case _:
            cls()
            print("The input value is not valid. Please try again.")
            input()
            option4()
    

def option5():
    global output
    cls()
    print("1) Change pitch")
    print("2) Return to main menu")
    select = input()
    match select:   
        case '1':
            cls()
            print("Please input bpm")
            pitchIn = input()
            try:
                pitchIn = int(pitchIn) #convert input into int
                cls()
                if pitchIn > 0:
                    cls()
                    print("Volume increased by", pitchIn) # tell user pitch increased by specified hz
                    print("Press enter to return to main menu")
                    input()
                if pitchIn < 0:
                    cls()
                    print("Volume decreased by", pitchIn) # tell user pitch decreased by specified hz
                    print("Press enter to return to main menu")
                    input()
            except ValueError:
                cls()
                print("Please input a number") # if input isn't number give error
                input()
                option4() # return to bpm menu
            else:
                pitch = pitchIn
        case '2': 
                __name__ == "__main__" # return to main menu
        case _:
            cls()
            print("The input value is not valid. Please try again.")
            input()
            option5()

def option6():
    global output
    cls()
    print("Add background noise")
    print("1) White noise")
    print("2) Pink noise")
    print("3) Brown noise")
    print("4) Return to main menu")
    noise = input()
    match noise:
        case '1':
            cls()
            print("Added white noise")
            print("Press enter to return to main menu")
            input()
        case '2':
            cls()
            print("Added pink noise")
            print("Press enter to return to main menu")
            input()
        case '3':
            cls()
            print("Added brown noise")
            print("Press enter to return to main menu")
            input()
        case '4':
            __name__ == "__main__" # return to main menu
        case _:
            cls()
            print("The input value is not valid. Please try again.")
            input()
            option6()


def option7():
    global output
    cls()
    print("Mix within external WAV file")
    input()

def option8():
    global output
    cls()
    print("Play ABC file")
    output.show('midi')
    input()

def option9():
    global output
    cls()
    output.export(r'output\test.wav', format='wav')
    print("File saved to output")
    if not output:
        print("No file to download!")
        input() # send back to main menu
    
    input()

def option10():
    cls()    
    yesNo = input("Are you sure you want to exit the program?(y=yes/n=no)")
    if yesNo=='y':
        sys.exit()

if __name__ == "__main__":
    global filePath
    out = 1
    while(TRUE):
        cls()
        print("Current file:", filePath)
        print("1) Choose waveform type")
        print("2) Change volume")
        print("3) Set ABC file path")
        print("4) Set BPM (Speed)")
        print("5) Change pitch")
        print("6) Add background noise")
        print("7) Mix within external WAV file")
        print("8) Play ABC file")
        print("9) Save as WAV file")
        print("10) Exit")
        inputText = input("Please select a number between 1 and 10: ")
        match inputText:
            case '1':
                option1()
            case '2':
                option2()
            case '3':
                option3()
            case '4':
                option4()
            case '5':
                option5()            
            case '6':
                option6()  
            case '7' :
                option7()
            case '8' :
                option8()
            case '9' :
                option9()
            case '10':
                option10()
            case _:
                cls()
                print("The input value is not valid. Please try again.")
                input()
    
