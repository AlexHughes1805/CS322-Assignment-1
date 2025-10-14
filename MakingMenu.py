import os
from pickle import TRUE
import sys

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def option1():
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
            print("The input value is not valid. Please try again.")
            option1()
    

def option2():
    cls()
    print("Set loudness")
    input()

def option3():
    cls()
    print("Set ABC file path")
    input()

def option4():
    cls()
    print("Set BPM (Speed)")
    bpmIn = input()
    try:
        bpmIn = int(bpmIn)
    except ValueError:
        print("Please input a number")
    else:
        bpm = bpmIn

def option5():
    cls()
    print("Change pitch")
    input()

def option6():
    cls()
    print("Add background noise")
    input()

def option7():
    cls()
    print("Mix within external WAV file")
    input()

def option8():
    cls()
    print("Play WAV file")
    input()

def option9():
    cls()
    print("Save as WAV file")
    input()
    

def option10():
    cls()    
    yesNo = input("Are you sure you want to exit the program?(y=yes/n=no)")
    if yesNo=='y':
        sys.exit()



if __name__ == "__main__":
    while(TRUE):
        cls()
        print("1) Choose waveform type")
        print("2) Set loudness")
        print("3) Set ABC file path")
        print("4) Set BPM (Speed)")
        print("5) Change pitch")
        print("6) Add background noise")
        print("7) Mix within external WAV file")
        print("8) Play WAV file")
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
            case '10' :
                option10()
            case _:
                cls()
                print("The input value is not valid. Please try again.")
                input()
    
