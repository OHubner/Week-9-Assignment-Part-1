
#Question 1
print("QUESTION 1")
listA = [10, 20, 30, 40, 50]

listLength = len(listA)
listB = []
for i in range(listLength):
    if i == 0:
        listB.append(listA[i] + listA[i + 1])
    elif i == listLength - 1:
        listB.append(listA[i] + listA[i-1])
    else:
        listB.append(listA[i - 1] + listA[i] + listA[i + 1])
print(listA)
print(listB)

#Question 2
print("\nQUESTION 2")
#This only really looks nice if you enter a number <= 10. It will work regardless but doesnt look as pretty
numDays = 5#int(input("Enter how many days you worked: "))
dailySalary = 1
totalSalary = 0
print("Day Number \t| Salary for Day \t| Salary to Date")
for i in range(numDays):
    totalSalary = totalSalary + dailySalary
    print(i + 1, "\t\t|", dailySalary / 100, "\t\t\t|", totalSalary / 100)
    dailySalary = dailySalary * 2

#Question 3
print("\nQUESTION 3")
def _encrypt(st):
    st = st.lower()
    st = st.replace(" ", "")
    encryptedStr = ""
    for i in st:
        ascNum = ord(i) + 4
        if ascNum > 122:
            ascNum = ascNum - 26
        encryptedStr = encryptedStr + chr(ascNum)
    return encryptedStr

def _decrypt(st):
    st = st.lower()
    decryptedStr = ""
    for i in st:
        ascNum = ord(i) - 4
        if ascNum < 97:
            ascNum = ascNum + 26
        decryptedStr = decryptedStr + chr(ascNum)
    return decryptedStr

encryptedStr = _encrypt("How do you do")
print(encryptedStr)
decryptedStr = _decrypt(encryptedStr)
print(decryptedStr)

#Question 4
print("\nQUESTION 4")
#4A
print("A)")
x = 5
sum = 0
for i in range(x):
    sum = sum + (i + 1)
print(sum)
#4B
print("B)")

for i in range(x):
    sum = 0
    for j in range(i + 1):
        sum = sum + (j + 1)
    print(sum)

#Question 5
print("\nQUESTION 5")
x = 120
y = 0
z = 0
if x > 100:
    y = 20
    z = 40
print(x, y, z)
a = 7
b = 0
c = 0
if a < 10:
    b = 0
    c = 1
print(a, b, c)
a = 10
if a < 10:
    b = 0
else:
    b = 99
print(a, b)

#Question 6
print("\nQUESTION 6")
def numVowCons(st):
    print(st)
    st = st.lower()
    numCons = 0
    numVow = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in st:
        ascNum = ord(i)
        if ascNum >= 97 and ascNum <= 122:
            if i in vowels:
                numVow = numVow + 1
            else:
                numCons = numCons + 1
    print("Number of Vowels:", numVow)
    print("Number of Consonents:", numCons)

numVowCons("Hello World")

#Question 7
print("\nQUESTION 7")
n = 10
def printFibNums(num):
    fibSeq = []
    for i in range(num):
        if i < 2:
            fibSeq.append(1)
        else:
            fibSeq.append(fibSeq[i - 2] + fibSeq[i -1])
    print(fibSeq)

def printLastFib(num):
    onePrev = 1
    twoPrev = 1
    newNum = 2
    for i in range(num):
        if i > 2:
            twoPrev = onePrev
            onePrev = newNum
            newNum = onePrev + twoPrev
    print(newNum)
printFibNums(n)
printLastFib(n)
