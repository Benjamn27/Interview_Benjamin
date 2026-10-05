print("Hello! Welcome to my interview. I'll be asking you a couple of questions today. Please answer truthfully and give short answers, not full sentences.")
print("")

firstAnswer = input("Let's start with your name. Who are you? ")

if firstAnswer.upper() == "BEN"or firstAnswer.upper() == "BENJAMIN":
    print(f"Hey, my name is {firstAnswer} too! Cool!")
else:
    print(f"Well, Hello {firstAnswer}!")
print("")

secondAnswer = input("Next, what is your favorite animal? ")

if secondAnswer.upper() == "PANDA":
    print("Wow! That's my favorite animal too! I think we are going to get along.")
else:
    print(f"Ah, the {secondAnswer}, an animal most know for... something probably, I just work here I'm not an expert.")
print("")


thirdAnswer = input("Okay, your final question today, what is your favorite number? ")

try:
    number = eval(thirdAnswer)
    if number >= 0 and number <=10:
        print(f"I see, {number}, you like the classics, nothing too special.")
    elif number < 0:
        print(f"Oh, {number}, you like negative numbers? That's...something.")
    elif number > 10 and number < 100:
        if number == 27:
            print("You have great taste, my friend. 27 is the best number every.")
        else:
            print(f"Okay,okay, {number}, I see. Not a bad selection at all, I respect it.")
    elif number >= 100 and number < 1000:
        print(f"Okay,{number} is a pretty big number, but I can see the appeal.")
    else:
        print(f"Okay, {number}, your going a little overboard, way too many numbers.")

except NameError:
    print(f"{thirdAnswer}. Okay, either you love your answer so much you wrote the entire name or you don't know what a number is. Or you're a nerd.")
    
except ZeroDivisionError:
    print("Real funny man we have here huh? Well, now your favorite number is poop.")
    thirdAnswer = "poop"

print("")
print(f"Okay, so your name is {firstAnswer}, your favorite animal is the {secondAnswer}, and your favorite number is {thirdAnswer}.")
print("Well, that's all the time I have, it was great getting to know you!")