import os
from pickle import TRUE
import sys
import pydub
import wave
import numpy as np
from scipy import signal
from  music21 import converter
import time


# pyaudio documentation: https://people.csail.mit.edu/hubert/pyaudio/docs/ and https://people.csail.mit.edu/hubert/pyaudio/

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def sine(frequency=440.0, duration =1.0, sample_rate=44100, amplitude=0.5):
    return (np.sin(2*np.pi*np.arange(sample_rate*duration)*frequency/sample_rate)).astype(np.float32)*amplitude

def square(frequency=440.0, duration =1.0, sample_rate=44100, amplitude=0.5):
    samples= sine(frequency, duration, sample_rate, amplitude)
    for i in range(0,len(samples)):
        if samples[i] > 0:
            samples[i]= amplitude
        elif samples[i] < 0:
            samples[i] = -amplitude
        else:
            samples[i] = 0.0
    return samples

def sawtooth(frequency=440.0, duration =1.0, sample_rate=44100, amplitude=0.5):
    t = np.linspace(0, duration, sample_rate)
    x= signal.sawtooth(2 * np.pi * frequency * t)
    x = x * amplitude
    return x

def triangle(frequency=440.0, duration =1.0, sample_rate=44100, amplitude=0.5):
    return np.abs(sawtooth(frequency=frequency, duration =duration, sample_rate=sample_rate, amplitude=amplitude))

def option1(): # change waveform type
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
            output = sine()
            print("Press enter to return to main menu")
            input()
        case '2' :
            cls()
            print("Wave changed to square wave")
            output = square()
            print("Press enter to return to main menu")
            input()
        case '3' :
            cls()
            print("Wave changed to sawtooth wave")
            output = sawtooth()
            print("Press enter to return to main menu")
            input()
        case '4' :
            cls()
            print("Wave changed to triangle wave")
            output = triangle()
            print("Press enter to return to main menu")
            input()
        case '5': 
            __name__ == "__main__" # return to main menu
        case _:
            cls()
            print("The input value is not valid. Please try again.") # report invalid input
            input()
            option1() # return to wave menu
    

def option2(): # adjust volume
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
                    output = output + dbIn
                    print("Press enter to return to main menu")
                    input()
                if dbIn < 0:
                    cls()
                    print("Volume decreased by", dbIn) # tell user volume decreased by specified db
                    output = output - dbIn
                    print("Press enter to return to main menu")
                    input()
            except ValueError:
                cls()
                print("Please input a number") # if input isn't number give error
                input()
                option2() # return to bpm menu
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
                temp = converter.parse(filePath)
                temp.write('midi', fp='temp.mid') # temporarily convert abc to midi
                time.sleep(1) # wait for file to be written
                output = pydub.AudioSegment.from_file('temp.mid', format='midi') # convert midi to audio segment
            elif filePath.endswith('.abc"'):
                filePath = filePath.replace('"', "") # remove apostrophes from any imput
                temp = converter.parse(filePath)
                temp.write('midi', fp='temp.mid')
                time.sleep(1) # wait for file to be written
                output = pydub.AudioSegment.from_file('temp.mid', format='wav') #convert midi to audio segment
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
            print("Please input pitch change in Hz")
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
    print("1) Mix within external WAV file")
    print("2) Return to main menu")
    input()

def option8():
    global output
    cls()
    print("1) Play ABC file")
    print("2) Return to main menu")
    input()

def option9():
    global output
    cls()
    print("1) Save as WAV file")
    print("2) Return to main menu")

    choose = input()
    match choose:
        case '1':
            cls()
            print("Name your file")
            name = input
            output.export(f'output\{name}.wav', format='wav')
            print("File saved to output")
            if not output:
                print("No file to download!")
                input() # send back to main menu

        case '2':
             __name__ == "__main__" # return to main menu
        
        case _:
            cls()
            print("The input value is not valid. Please try again.")
            input()
            option9()
    
    
    input()

def option10():
    cls()    
    yesNo = input("Are you sure you want to exit the program?(y=yes/n=no)")
    if yesNo=='y':
        sys.exit()

if __name__ == "__main__":
    out = 1
    while(TRUE):
        cls()
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
    
