#Question 1

marks=int(input("Enter your marks:"))
if marks <25:
    print("Grade - F")
elif marks <45:
    print("Grade - E")
elif marks <50:
    print("Grade - D")
elif marks <60:
    print("Grade - C")
elif marks <80:
    print("Grade - B")
else:
    print("Grade - A")

#Enter your marks:100
#Grade - A

#Question 2

year=int(input("Enter the Year"))
if year%4==0 or year%400==0:
    print(year,"is the Leap year")
else:
    print(year,"is not a Leap year")
#Enter the Year4044
#4044 is the Leap year

#Question 3

import random
i=1
while i<=10:
    a=random.randint(1,25)
    b=random.randint(1,25)
    print(a, "X",b,"=")
    c=int (input ("Enter your answer: "))
    d=int(a*b)
    if c==d:
        print ("correct answer")
    else:
        print("wrong answer")
    i=i+1
print ("end")

#1 X 2 =
#Enter your answer: 2
#correct answer
#14 X 3 =
#Enter your answer: 42
#correct answer
#14 X 22 =
#Enter your answer: 308
#correct answer
#23 X 18 =
#Enter your answer: 414
#correct answer
#8 X 9 =
#Enter your answer: 72
#correct answer
#6 X 1 =
#Enter your answer: 6
#correct answer
#17 X 18 =
#Enter your answer: 306
#correct answer
#14 X 16 =
#Enter your answer: 224
#correct answer
#8 X 10 =
#Enter your answer: 80
#correct answer
#25 X 7 =
#Enter your answer: 175
#correct answer
#end

#Question 4

x=200
for i in range(x):
    if i%5==2:
        if i%6==3:
            if i%7==2:
                print(i,"is the Number of Candies in the Jar")
    i=i+1
print("end")

#177 is the Number of Candies in the Jar
#end
