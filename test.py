from time import sleep
def ask_mcq(**kwargs):
    # Print questions
    for question in kwargs["question"]:
        print(question)
        sleep(1.5)

    print("----------")

    # Print answers
    for index, answer in enumerate(kwargs["answer"]):
        print(index + 1, ". " ,answer)
    
    while True:
        user_input = input("Enter your choice")
        if user_input in [n+1 for n in answer]:
            return user_input

    
ask_mcq(dialogue = ["qn1", "qn2"], question = ["ans1", "ans2"])