import random
from datetime import date

def main():
    # ex1()
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
    ex13()

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
        

if __name__ == "__main__":
    main()