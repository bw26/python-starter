import random
from datetime import *
import hashlib
import collections

def main():
    #  ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    # ex8()
    # ex9()
    # ex10()
    # ex11()
    # ex12()
    # ex13()
    # ex14()
    # ex15()
    # ex16()
    # ex17()
    # ex18()
    # ex19()
    # ex20()
    # ex21()
    # ex22()
    # ex23()
    # ex24()
    #ex25()
    # ex26()
    # ex27()
    ex28()
    #ex29()
    #ex30()
    #ex31()
    #ex32()
    #ex33()
    #ex34()
    #ex35()
    #ex36()
    #ex37()
    #ex38()
    #ex39()
    #ex40()
    #ex41()
    #ex42()
    #ex43()
    #ex44()
    #ex45()
    

def ex1():
    nums = []
    sum = 0
    for i in range(10):
        num = random.randint(0,100)
        sum+=num
        nums.append(num)
    print(nums)
    print(f'The sum is: {sum}')
        
def ex2():
    width = float(input(" Enter width: "))
    height = float(input(" Enter height: "))
    length = float(input(" Enter length: "))
    print(f"Volume is: {width*height*length}")
    
def ex3():
    nums = input("Enter list of numbers: ")
    num = nums.split(",")
    if num[0] == num[-1]: print(True)
    else: print(False)
    
def ex4():
    string = "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado."
    words = string.split(" ")
    count = 0
    for i in words:
        if i == "Python":
            count += 1
    print(count)
    
def ex5():
    myList = [1,2,3]
    mySet = {3,4,5}
    mySet.update(myList)
    print(mySet)
    
def ex6():
    print(list(reversed([11, 100, 101, 999, 1001])))

def ex7():
    rand_num = random.randint(1,100)
    if rand_num < 10: print(f"{rand_num}: You lose")
    elif rand_num < 50: print(f"{rand_num}: Try again")
    else: print(f"{rand_num}: You win!")

def ex8():
    myList = [6,2,7,3,77,7,1]
    min = myList[0]
    for i in myList:
        if i < min:
            min = i
    print(min)

def ex9():
    word = input("Enter String: ")
    if word.isupper():
        print("True")
    else:
        print("False")

def ex10():
    vowels = {'a','e','i','o','u'}
    word = input("Enter string: ").lower()
    v_count = 0
    c_count = 0
    for i in word:
        if i in vowels: v_count+=1
        else: c_count+=1
    print(f"Vowels: {v_count}")
    print(f"Consonants: {c_count}")
    
def ex11():
    f = open("output.txt", "w")
    f.write(f"Today's date is: {date.today().strftime('%m/%d/%y')}.")
    f.close()
    

def ex12():
    num = input("Enter integer: ")
    try:
        num = int(num)
        print(num*-1)
    except ValueError:
        print(f"ERROR: {num} is not an integer")

def ex13():
    while(True):
        num1 = input("Enter first integer: ")
        if num1 == "exit" : break
        num2 = input("Enter second integer: ")
        if num2 == "exit" : break
        print(f"Answer: {int(num1)+int(num2)}")
        
def ex14():
    while(True):
        num1 = input("Enter first integer: ")
        if num1 == "exit" : break
        num2 = input("Enter second integer: ")
        if num2 == "exit" : break
        operation = input("Enter operation(add, sub, mul, div): ").lower()
        match operation:
            case "add":    
                print(f"Answer: {int(num1)+int(num2)}")
            case "sub":    
                print(f"Answer: {int(num1)-int(num2)}")
            case "mul":
                print(f"Answer: {int(num1)*int(num2)}")
            case "div":
                try:
                    print(f"Answer: {int(num1)/int(num2)}")
                except ZeroDivisionError:
                    print("Cannot divide by zero")
        
def ex15():
    f = open("temp2.txt","w")
    while(True):
        num1 = input("Enter first integer: ")
        if num1 == "exit" : break
        num2 = input("Enter second integer: ")
        if num2 == "exit" : break
        operation = input("Enter operation(add, sub, mul, div): ").lower()
        match operation:
            case "add":    
                f.write(f" {date.today().strftime('%m/%d/%y')} {date.ctime}Answer: {int(num1)+int(num2)}")
            case "sub":    
                f.write(f"Answer: {int(num1)-int(num2)}")
            case "mul":
                f.write(f"Answer: {int(num1)*int(num2)}")
            case "div":
                try:
                    f.write(f"Answer: {int(num1)/int(num2)}")
                except ZeroDivisionError:
                    print("Cannot divide by zero")
        
def ex16():
    pass_dict = {}
    while True:
        userName = input("Enter Username: ")
        if userName == "exit": break
        password = input("Enter password: ")
        if password == "exit": break
        pass_dict[userName] = hashlib.sha256(password.encode('utf-8')).hexdigest()
    for key in pass_dict.keys():
        print(f"{key} : {pass_dict[key]}")
        
def ex17():
    pass_dict = {}
    while True:
        mode = input("Enter mode (add|login): ")
        if mode == "exit": break
        userName = input("Enter username: ")
        if userName == "exit": break
        password = input("Enter password: ")
        if password == "exit": break
        
        if mode == "add":
            pass_dict[userName] = hashlib.sha256(password.encode('utf-8')).hexdigest()
        elif mode == "login":
            if userName not in pass_dict.keys(): 
                print("User does not exist.")
            elif pass_dict.get(userName) == hashlib.sha256(password.encode('utf-8')).hexdigest():
                print("Password is correct.")
            else:
                print("Incorrect password.")
        else:
            print("Invalid command")
    for key in pass_dict.keys():
        print(f"{key} : {pass_dict[key]}")
        
def ex18():
    randNum = random.randint(1,10)
    userguess = 0
    while(userguess != randNum):
        userguess = int(input("Enter a number between 1-10: "))
        if userguess > randNum:
            print("Too high.")
        elif userguess < randNum:
            print("Too low.")
        else:
            print("You guessed it!!!")
            
def ex19():
    wordlist = ["Hello", "World", "in", "a", "frame"]
    maxCount = 0
    for i in wordlist:
        maxCount = len(i) if len(i) > maxCount else maxCount
    print("*" * (maxCount+4))
    for i in wordlist:
        print(f"* {i}", end = "")
        print((" " * (maxCount-len(i))), end = "")
        print(" *")
    print("*" * (maxCount+4))
    
def ex20():
    f = open("input.txt", "r")
    wordCount = collections.defaultdict(int)  
    word = f.read().replace(".","").split(" ")
    for i in word : wordCount[i]+=1
    for key in wordCount.keys(): print(f"{key}:{wordCount[key]}")
    f.close()
    
def ex21():
    countDown = int(input("Enter countdown(sec):"))
    for i in range(countDown, 0, -1):
        print(i)
    print("Blast off!!")
    
def ex22():
    def convertTextTOMorseCode(inputString):  
        textToMorseDict = {
                        'a' : '*-',
                        'b' : '-***',
                        'c' : '-*-*',
                        'd' : '-**',
                        'e' : '*',
                        'f' : '**-*',
                        'g' : '--*',
                        'h' : '****',
                        'i' : '**',
                        'j' : '*---',
                        'k' : '-*-',
                        'l' : '*-**',
                        'm' : '--',
                        'n' : '-*',
                        'o' : '---',
                        'p' : '*--*',
                        'q' : '--*-',
                        'r' : '*-*',
                        's' : '***',
                        't' : '-',
                        'u' : '**-',
                        'v' : '***-',
                        'w' : '*--',
                        'x' : '-**-',
                        'y' : '-*--',
                        'z' : '--**'
                        } 
        res = ""
        for i in inputString.replace("\n",""):
            if i == " ": res+=" "
            else: res += textToMorseDict[i] + " "           
        return res
    while True:
        sentence = input("Enter text: ")
        print(f"Morse Code: {convertTextTOMorseCode(sentence)}")
    

def ex23():
    def convertTextTOMorseCode(inputString):  
        textToMorseDict = {
                        'a' : '*-',
                        'b' : '-***',
                        'c' : '-*-*',
                        'd' : '-**',
                        'e' : '*',
                        'f' : '**-*',
                        'g' : '--*',
                        'h' : '****',
                        'i' : '**',
                        'j' : '*---',
                        'k' : '-*-',
                        'l' : '*-**',
                        'm' : '--',
                        'n' : '-*',
                        'o' : '---',
                        'p' : '*--*',
                        'q' : '--*-',
                        'r' : '*-*',
                        's' : '***',
                        't' : '-',
                        'u' : '**-',
                        'v' : '***-',
                        'w' : '*--',
                        'x' : '-**-',
                        'y' : '-*--',
                        'z' : '--**'
                        } 
        res = ""
        for i in inputString.replace("\n",""):
            if i == " ": res+=" "
            else: res += textToMorseDict[i] + " "           
        return res
    def convertMorseCodeToText(inputString): 
        morseToTextDict = {
                            '*-'   : 'a', 
                            '-***' : 'b',
                            '-*-*' : 'c',
                            '-**'  : 'd',
                            '*'    : 'e',
                            '**-*' : 'f',
                            '--*'  : 'g',
                            '****' : 'h',
                            '**'   : 'i',
                            '*---' : 'j',
                            '-*-'  : 'k',
                            '*-**' : 'l',
                            '--'   : 'm',
                            '-*'   : 'n',
                            '---'  : 'o',
                            '*--*' : 'p',
                            '--*-' : 'q',
                            '*-*'  : 'r',
                            '***'  : 's',
                            '-'    : 't',
                            '**-'  : 'u',
                            '***-' : 'v',
                            '*--'  : 'w',
                            '-**-' : 'x',
                            '-*--' : 'y',
                            '--**' : 'z'
                        }
        res = ""
        for i in inputString.replace("\n","").split("  "):
            letters = i.split(" ")
            for letter in letters:
                res+=morseToTextDict[letter]
            res+=" "         
        return res
    
    while True:
        sentence = input("Enter text or morse code: ")
        if "*" in sentence or "_" in sentence:
            print(f"Text: {convertMorseCodeToText(sentence)}")
        else: 
            print(f"Morse Code: {convertTextTOMorseCode(sentence)}")
            
def ex24():
    txt = input("Enter text: ").split(" ")
    for i in txt:
        for j in range(len(i)):
            print(" "*j, end= "")
            print(f"{i[j]}")
            
def ex25():
    txt = input("Enter text: ")
    upper = 0
    lower = 0
    for i in txt:
        if i.isalpha():
            if i.isupper(): upper+=1
            else: lower+=1  
    print(f"Uppercase: {upper}")
    print(f"Lowercase: {lower}")

def ex26():
    def printDictionary(d):
        d = dict(sorted(d.items(), key= lambda x : x[0]))
        for i in d:
            print(f"{i} : {d[i]}")
    personDictionary = {
        '222-22-2222' : 'joe',
        '333-33-3333' : 'fred',
        '555-55-5555' : 'mary',
        '444-44-4444' : 'fred',
        '111-11-1111' : 'jane'
        }
    printDictionary(personDictionary)
            
def ex27():
    peopleList = [
                    { 
                    'name' : 'joe', 
                    'age' : 20 
                    },
                    { 
                    'name' : 'fred', 
                    'age' : 10 
                    },
                    { 
                    'name' : 'sally', 
                    'age' : 30 
                    },
                    { 
                    'name' : 'sue', 
                    'age' : 15 
                    }
                ]
    def printPersonList(peopleList):
        peopleList = sorted(peopleList, key=lambda x: x['age'])
        for i in peopleList:
            print(f"{i['name']} : {i['age']}")
    printPersonList(peopleList)
    
def ex28():
    def splitAndPrint(numList):
        size = int(len(numList)//2)
        print(f" First half: {numList[0:size]}")
        print(f" Second half: {numList[size::]}")
    splitAndPrint([1,2,3,4,5,6,7,9,10,11])

def ex29():return
def ex30():return
def ex31():return
def ex32():return
def ex33():return
def ex34():return
def ex35():return
def ex36():return
def ex37():return
def ex38():return
def ex39():return
def ex40():return
def ex41():return
def ex42():return
def ex43():return
def ex44():return
def ex45():return

if __name__ == "__main__":
    main()