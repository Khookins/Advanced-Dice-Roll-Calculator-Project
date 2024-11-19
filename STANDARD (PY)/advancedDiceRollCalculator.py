import random
import ctypes
import os

#def createProgramFiles():
#    appdata_path = os.getenv("APPDATA")
#    program_path = os.path.join(appdata_path, "ADR-CALCULATOR")
#    print(f"Directory created at: {program_path}")
#    if not os.path.exists(program_path):
#        print(f"Directory created at: {program_path}")
#        os.makedirs(program_path)

def rollDice(diceAmount,diceType):
    if (int(diceType) <= 1):
        print("Dice Type Must Be A Valid Interger Must Be Above 1")
        if input(">>> Do You Want To Reinput? Type Y OR N To Proceed: ").upper() == ("Y"):
            os.system("cls")
            start()
        else:
            print("Exiting Program")
            exit()
    result = 0
    for i in range(0,diceAmount):
        result += random.randint(1,diceType)
    return result
        
def calculateAverage(accuracy,diceAmount,diceType):
    result = 0
    if (int(accuracy) <= 1):
        print("Accuracy Must Be A Valid Interger Above 1")
        if input(">>> Do You Want To Reinput? Type Y OR N To Proceed: ").upper() == ("Y"):
            os.system("cls")
            start()
        else:
            print("Exiting Program")
            exit()
    elif (int(diceType) <= 1):
        print("Dice Type Must Be A Valid Interger Must Be Above 1")
        if input(">>> Do You Want To Reinput? Type Y OR N To Proceed: ").upper() == ("Y"):
            os.system("cls")
            start()
        else:
            print("Exiting Program")
            exit()
    for i in range(0,int(accuracy)):
        result += rollDice(int(diceAmount),int(diceType))
    result /= int(accuracy)
    return result 

def multiTestCalculate(testAmount,accuracy,diceAmount,diceType):
    result = 0
    if(int(testAmount) <= 1):
        print("Test Amount Must Be A Valid Interger Must Be Above 1. Please Refer To Single Test Calculation If You Only Want To Preform It Once.")
        if input(">>> Do You Want To Reinput? Type Y OR N To Proceed: ").upper() == "Y":
            os.system("cls")
            start()
        else:
            print("Exiting Program")
            exit()
    elif (int(accuracy) <= 1):
        print("Accuracy Must Be A Valid Interger Above 1")
        if input(">>> Do You Want To Reinput? Type Y OR N To Proceed: ").upper() == ("Y"):
            os.system("cls")
            start()
        else:
            print("Exiting Program")
            exit()
    elif (int(diceType) <= 1):
        print("Dice Type Must Be A Valid Interger Must Be Above 1")
        if input(">>> Do You Want To Reinput? Type Y OR N To Proceed: ").upper() == ("Y"):
            os.system("cls")
            start()
        else:
            print("Exiting Program")
            exit()
    for i in range(0,int(testAmount)):
        result += calculateAverage(accuracy,diceAmount,diceType)
    result /= int(testAmount)
    return result

def start():
    userInput = input(">>> Type H For Help. Type C To Start A Single-test Calculation. Type M To Start A Multi-test Calculation. To Type R To Roll Some Dice. Type E To Exit: ")
    if userInput.upper() == "H":
        os.system("cls")
        print("Accuracy: How Many Times The Program Should Loop Over To Get An Average\nDice Amount: How Many Of The Dice Type Selected To Roll Per Loop\nDice Type: The Dice You Want To Calculate The Average For\nTests (For Multi-test Calculations): The Amount Of Times It Should Calculate Repeatedly To Try To Get The Most Accurate Calculation")
        if input(">>> Do You Want To Go Back? Type Y Or N To Proceeed: ").upper() == "Y":
            os.system("cls")
            start()
        else:
            print("Exiting Program")
            exit()
    elif userInput.upper() == "C":
        os.system("cls")
        print(calculateAverage(input(">>> Please Give A Accuracy: "),input(">>> Please Give A Amount Of Dice: "), input(">>> Please Give A Dice Type: ")))
        if input(">>> Do You Want To Restart? Type Y Or N To Proceed: ").upper() == "Y":
            os.system("cls")
            start()
        else:
            print("Exiting Program")
            exit()
    elif userInput.upper() == "M":
        os.system("cls")
        print(multiTestCalculate(input(">>> Please Give A Amount Of Tests: "),input(">>> Please Give A Accuracy: "), input(">>> Please Give A Amount Of Dice: "), input(">> Please Give A Dice Type: ")))
        if input(">>> Do You Want To Restart? Type Y Or N To Proceed: ").upper() == "Y":
            os.system("cls")
            start()
        else:
            print("Exiting Program")
            exit()
    elif userInput.upper() == "R":
        os.system("cls")
        print("Result: " + str(rollDice(int(input(">>> Please Give Amount Of Dice To Roll: ")),int(input(">>> Please Give A Dice Type: ")))))
        if input(">>> Do You Want To Restart? Type Y Or N To Proceed: ").upper() == "Y":
            os.system("cls")
            start()
        else:
            print("Exiting Program")
            exit()
    elif userInput.upper() == "E":
        os.system("cls")
        print("Exiting Program")
        exit()
    else:
        os.system("cls")
        print("That Was Not A Valid Option.")
        start()
    
ctypes.windll.kernel32.SetConsoleTitleW("Advanced Dice Roll Calculator")
print(">>> Welcome To Advanced Dice Roll Calculator. What Would You Like To Do?")
#createProgramFiles()
start()