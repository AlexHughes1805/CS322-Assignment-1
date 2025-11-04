import os
from pickle import TRUE
import sys
import pydub
from pydub import effects
from pydub.playback import play
import numpy as np
from scipy import signal
from  music21 import converter
import time
import acoustics
import pretty_midi
import soundfile


# pydub documentation - https://github.com/jiaaro/pydub/blob/master/API.markdown and https://github.com/jiaaro/pydub/tree/master/pydub
# music21 documentation https://www.music21.org/music21docs/
# pretty_midi documentation - https://craffel.github.io/pretty-midi/

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#code from the provided waveAudio.py file
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
    if 'output' in globals() and isinstance(output, pydub.AudioSegment):
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

    else:
        print("No file loaded")
        print("Returning to main menu")
        time.sleep(2) # wait 2 seconds before returning to main menu
        __name__ == "__main__" # return to main menu
    

def option2(): # adjust volume
    global output
    cls()
    if 'output' in globals() and isinstance(output, pydub.AudioSegment):
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

    else:
        print("No file loaded")
        print("Returning to main menu")
        time.sleep(2) # wait 2 seconds before returning to main menu
        __name__ == "__main__" # return to main menu

def option3(): # import abc file and convert to wav
    global output # make abc file a global variable so other functions can access it
    cls()
    print("1) Set ABC file path")
    print("2) Return to main menu")
    choose = input()
    match choose:
        case '1':
            cls()
            print("Please input file path")
            filePath = input()
            filePath = filePath.replace('"', "") # remove any apostrophes in filepath
            filePath = os.path.abspath(filePath)
            if filePath.endswith('.abc'):
                temp = converter.parse(filePath) # music21 parsing abc file
                temp.write('midi', fp='temp.mid') # temporarily convert abc to midi
                time.sleep(1) # wait for file to be written
                midi = pretty_midi.PrettyMIDI("temp.mid") # parse midi file
                audio = midi.fluidsynth()
                soundfile.write("temp.wav", audio, 44100) # write wav file that user will handle and edit
                time.sleep(1) # wait for wav file
                os.remove("temp.mid") # delete temp midi file
                output = pydub.AudioSegment.from_file('temp.wav', format='wav') # convert midi to audio segment
            else:
                print("Not a valid file")
                input()
                option3()
            
        case '2':
             __name__ == "__main__" # return to main menu

def changeBPM(seg, change: float):
    if change == 1.0:
        return seg
    if change > 1.0: 
        return effects.speedup(seg, play_backspeed=change) # increase playback tempo
    else:
        newSpeed = max(1, int(seg.frane_rate * change)) # slowing down playback speed
        return seg.spawn(seg.raw_data, overrides={'frame_rate': newSpeed}).set_frame_rate(seg.frame_rate)

def option4(): # chance the tempo of the song
    global output
    cls()
    if 'output' in globals() and isinstance(output, pydub.AudioSegment):
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
                    change = bpmIn / float(bpmIn) if bpmIn != 0 else 1.0
                    output = changeBPM(output, change)
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
    else:
        print("No file loaded")
        print("Returning to main menu")
        time.sleep(2) # wait 2 seconds before returning to main menu
        __name__ == "__main__" # return to main menu
    

def option5():
    global output
    cls()
    if 'output' in globals() and isinstance(output, pydub.AudioSegment):
        print("1) Change pitch")
        print("2) Return to main menu")
        select = input()
        match select:   
            case '1':
                cls()
                print("Please input pitch change in octaves")
                pitchIn = input()
                try:
                    pitchIn = int(pitchIn) #convert input into int
                    cls()
                    if pitchIn > 0:
                        cls()
                        print("Pitch increased by", pitchIn, "octaves") # tell user pitch increased
                        octaves = pitchIn
                        newSample = int(output.frame_rate * (2.0 ** octaves))
                        newPitch = output._spawn(output.raw_data, overrides={'frame_rate': newSample})
                        output = newPitch
                        print("Press enter to return to main menu")
                        input()
                    if pitchIn < 0:
                        cls()
                        print("Pitch decreased by", pitchIn, "octaves") # tell user pitch decreased 
                        octaves = pitchIn
                        newSample = int(output.frame_rate * (2.0 ** octaves))
                        newPitch = output._spawn(output.raw_data, overrides={'frame_rate': newSample})
                        output = newPitch
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

    else:
        print("No file loaded")
        print("Returning to main menu")
        time.sleep(2) # wait 2 seconds before returning to main menu
        __name__ == "__main__" # return to main menu

# code from provided noise.py
def white(output):
    output = acoustics.generator.noise(44100*10, color='white', state=None)
    return output

def pink(output):
    output = acoustics.generator.noise(44100*10, color='pink', state=None)
    return output

def brown(output):
    output = acoustics.generator.noise(44100*10, color='brown', state=None)
    return output

def option6():
    global output
    if 'output' in globals() and isinstance(output, pydub.AudioSegment):
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
                output = white(output)
                print("Press enter to return to main menu")
                input()
            case '2':
                cls()
                print("Added pink noise")
                output = pink(output)
                print("Press enter to return to main menu")
                input()
            case '3':
                cls()
                print("Added brown noise")
                output = brown(output)
                print("Press enter to return to main menu")
                input()
            case '4':
                __name__ == "__main__" # return to main menu
            case _:
                cls()
                print("The input value is not valid. Please try again.")
                input()
                option6()
    else:
        print("No file loaded")
        print("Returning to main menu")
        time.sleep(2) # wait 2 seconds before returning to main menu
        __name__ == "__main__" # return to main menu


def option7():
    global output
    cls()
    if 'output' in globals() and isinstance(output, pydub.AudioSegment):
        print("1) Mix within external WAV file")
        print("2) Return to main menu")
        input()

    else:
        print("No file loaded")
        print("Returning to main menu")
        time.sleep(2) # wait 2 seconds before returning to main menu
        __name__ == "__main__" # return to main menu

def option8():
    global output
    cls()
    if 'output' in globals() and isinstance(output, pydub.AudioSegment):
        print("1) Play ABC file")
        print("2) Return to main menu")
        choose = input()
        match choose:
            case '1':
                cls()
                print("Playing ABC file")
                play(output)
                input()
            case '2':
                __name__ == "__main__" # return to main menu
            case _:
                cls()
                print("The input value is not valid. Please try again.")
                input()
                option9()
    else:
        print("No file loaded")
        print("Returning to main menu")
        time.sleep(2) # wait 2 seconds before returning to main menu
        __name__ == "__main__" # return to main menu
        

def option9():
    global output
    cls()
    if 'output' in globals() and isinstance(output, pydub.AudioSegment):
        print("1) Save as WAV file")
        print("2) Return to main menu")

        choose = input()
        match choose:
            case '1':
                cls()
                print("Name your file")
                name = input()
                file = f"Output/{name}.wav"
                file = os.path.abspath(file)
                if name == "":
                    cls()
                    print("Please type file name")
                    input()
                else:
                    cls()
                    output.export(file, format="wav")
                    print("File saved to output")
                    input()

            case '2':
                __name__ == "__main__" # return to main menu
            
            case _:
                cls()
                print("The input value is not valid. Please try again.")
                input()
                option9()
    else:
        print("No file loaded")
        print("Returning to main menu")
        time.sleep(2) # wait 2 seconds before returning to main menu
        __name__ == "__main__" # return to main menu

def option10():
    cls()    
    print("Are you sure you want to exit the program?")
    print("[y=yes/n=no]")
    yesNo = input()
    if yesNo=='y':
        os.remove("temp.wav") # remove any temporary files
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