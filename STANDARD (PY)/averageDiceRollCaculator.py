import random
import ctypes

def rollDice(diceAmount,diceType):
    result = 0
    for i in range(0,diceAmount):
        result += random.randint(1,diceType)
    return result
        
def cauculateAverage(accuracy,diceAmount,diceType):
    result = 0
    if (int(accuracy) <= 1):
        print("Accuracy Must Be A Valid Interger Above 1")
        if input(">>> Do You Want To Reinput? Type Y OR N To Proceed: ").upper() == ("Y"):
            start()
        else:
            print("Exiting Program")
            exit()
    for i in range(0,int(accuracy)):
        result += rollDice(int(diceAmount),int(diceType))
    result /= int(accuracy)
    return result 

def start():
    userInput = input(">>> Type H For Help. Type S To Start A Caculation. Type R To Roll Some Dice. Type E To Exit: ")
    if userInput.upper() == "H":
        print("Accuracy: How Many Times The Program Should Loop Over To Get An Average\nDice Amount: How Many Of The Dice Type Selected To Roll Per Loop\nDice Type: The Dice You Want To Caculate The Average For")
        if input(">>> Do You Want To Go Back? Type Y Or N To Proceeed: ").upper() == "Y":
            start()
        else:
            print("Exiting Program")
            exit()
    elif userInput.upper() == "S":
        print(cauculateAverage(input(">>> Please Give A Accuracy: "),input(">>> Please Give A Amount Of Dice: "), input(">>> Please Give A Dice Type: ")))
        if input(">>> Do You Want To Restart? Press Y Or N To Proceed: ").upper == "Y":
            start()
        else:
            print("Exiting Program")
            exit()
    elif userInput.upper() == "R":
        print("Result: " + str(rollDice(int(input(">>> Please Give Amount Of Dice To Roll: ")),int(input(">>> Please Give A Dice Type: ")))))
        if input(">>> Do You Want To Restart? Press Y Or N To Proceed: ").upper == "Y":
            start()
        else:
            print("Exiting Program")
            exit()
    elif userInput.upper() == "E":
        print("Exiting Program")
        exit()
    else:
        start()
    
ctypes.windll.kernel32.SetConsoleTitleW("Average Dice Roll Caculator For DND")
print(">>> Welcome To Average Dice Roll Caculator For DND. What Would You Like To Do?")   
start()