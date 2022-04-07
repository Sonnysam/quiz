
questions = [ "Javascript is a scripting language?",
              "H.E Nana Addo  the president of the Ghana?",
              "Tokyo is the capital of Ghana?",
              "To understand any programming language, you need to print hello world" ]

answer = [ "true", 
           "true",
           "false",
           "false" ]

score = 0

print("Welcome to Sonny's Python Quiz. Choose whether true or false")
# name = print("Start by entering your name")
name = input("What is your name?")

for i in range(0, len(questions)):
    print(questions[i])
    user_answer = input("Answer: ")

    if user_answer == answer[i]:
        print("Hurray answer is correct :) ") 
        score = score + 1
    else:
        print("Oops answer is incorrect")

print(f"Hello {name} your final score is: {score} ")