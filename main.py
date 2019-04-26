import textwrap 
correct = 0
wrong = 0
value = """This is a web development quiz, but on Python. 
        Don't ask me why. I have no idea why I did this! HAHAHAHAHAHAHAHAHAHA!"""
wrapper = textwrap.TextWrapper(width=50) 
word_list = wrapper.wrap(text=value)
for element in word_list: 
    print(element) 
print("The quiz is starting now!")
qone = input("What is the fundamental language to make websites, HTML, JS, PHP, or XML - ")
if qone == "HTML":
    wrong += 0
else:
    wrong += 1
qtwo = input("What does HTML stand for (in all caps, with no spaces or hyphens) - ")
if qtwo == "HYPERTEXTMARKUPLANGUAGE":
    wrong += 0
else:
    wrong += 1
qthr = input("What does CSS stand for (write it the same format you wrote the last answer) - ")
if qthr == "CASCADINGSTYLESHEETS":
    wrong += 0
else:
    wrong += 1
qfor = input("What does JS stand for (you know the drill) - ")
if qfor == "JAVASCRIPT":
    wrong += 0
else:
    wrong += 1
qfiv = input("What type of language is HTML, A - Markup, B - Programming, C - Object Oriented, or D - Assembly (Type the letter) - ")
if qfiv == "A":
    wrong += 0
else:
    wrong += 1
print("Review Time!")
ans = " Your answer - "
print("What is the fundamental language to make websites, HTML, JS, PHP, or XML" + ans + qone)
print("What does HTML stand for (in all caps, with no spaces or hyphens)" + ans + qtwo)
print("What does CSS stand for (write it the same format you wrote the last answer) - " + ans + qthr)
print("What does JS stand for (you know the drill) - " + ans + qfor)
print("What type of language is HTML, A - Markup, B - Programming, C - Object Oriented, or D - Assembly (Type the letter) - " + ans + qfiv)
choice = input("Would you like to change any of your answers (y/n) - ")
while choice == "y":
    qnum = int(input("Which number (integer form, there were 5 questions) - "))
    if qnum == 1:
        qone = input("What is the fundamental language to make websites, HTML, JS, PHP, or XML - ")
        if qone == "HTML":
            wrong -= 1
        else:
            wrong += 0
    if qnum == 2:
        qtwo = input("What does HTML stand for (in all caps, with no spaces or hyphens) - ")
        if qtwo == "HYPERTEXTMARKUPLANGUAGE":
            wrong -= 1
        else:
            wrong += 0
    if qnum == 3:
        qthr = input("What does CSS stand for (write it the same format you wrote the last answer) - ")
        if qthe == "CASCADINGSTYLESHEETS":
            wrong -= 1
        else:
            wrong += 0
    if qnum == 4:
        qfor = input("What does JS stand for (you know the drill) - ")
        if qfor == "JAVASCRIPT":
            wrong -= 1
        else:
            wrong += 0
    if qnum == 5:
        qfiv = input("What type of language is HTML, A - Markup, B - Programming, C - Object Oriented, or D - Assembly (Type the letter) - ")
        if qfiv == "A":
            wrong -= 1
        else:
            wrong += 0
    choice = input("Would you like to change any more of your answers (y/n) - ")
if choice == "n":
    correct = 5-wrong
    print("You got " + str(wrong) + " questions wrong")
    print("You got " + str(correct) + " question correct")
    if int(correct) == 5 and int(wrong) == 0:
        print("Congratulations - You got a 100%!")
exit()