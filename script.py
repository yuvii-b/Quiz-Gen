import json
import random
import time
    
# Questions in json file are created by ChatGPT    
def load_questions():
    with open("questions.json", "r") as f:
        questions = json.load(f)["questions"]

    return questions

def generate_questions(questions, num_of_questions):
    if num_of_questions > len(questions):
        num_of_questions = len(questions)
    
    gen_questions = random.sample(questions, num_of_questions)
    return gen_questions

def display_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(str(i + 1) + ") ", option)
    number = int(input("Enter the option for the correct answer: "))
    if number < 1 or number > len(question["options"]):
        print("Invalid option, Wrong Answer")
        return False
    correct_ans = question["options"][number - 1] == question["answer"]
    return correct_ans

correct = 0
questions = load_questions()
num_questions = int(input("Enter the number of questions for the quiz: "))
start_time = time.time()
quiz_questions = generate_questions(questions, num_questions)
for question in quiz_questions:
    is_correct = display_question(question)
    if is_correct:
        correct += 1
    print("---------------------------------")
completed_time = time.time() - start_time

print("RESULT")
print("Total number of questions: {}".format(num_questions))
print("Correct Answers: {}".format(correct))
print("Score: {}%".format(round((correct / num_questions) * 100)))
print("Time taken: {} seconds".format(round(completed_time)))