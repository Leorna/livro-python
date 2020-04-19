import os
import random
from get_states_and_capitals import get_states_and_capitals


def generate_options(quiz_file, answer_file, state, question_number):
    correct_option = states_and_capitals[state]

    wrong_options = list(states_and_capitals.values())

    wrong_options.remove(correct_option)

    wrong_options = random.sample(wrong_options, 3)

    options = wrong_options + [correct_option]

    random.shuffle(options)

    for i in range(4):
        option = f"\n{'ABCD'[i]}. {options[i]}"
        quiz_file.write(option)

    quiz_file.write("\n\n\n")

    answer_file.write(f"{question_number}. {'ABCD'[options.index(correct_option)]}\n")


def generate_questions(quiz_file, answer_file):
    states = list(states_and_capitals.keys())
    random.shuffle(states)

    for question_number in range(QTD_OF_QUESTIONS):
        question = f"{question_number+1} - What is the capital of {states[question_number]}?\n"
        quiz_file.write(question)

        generate_options(quiz_file, answer_file, states[question_number], question_number+1)


def create_files(files_number):
    try:
        os.makedirs(f"quiz-{files_number}")
    except FileExistsError:
        print("File exists")

    quiz_file = open(f"./quiz-{files_number}/questions.txt", "w")
    answer_file = open(f"./quiz-{files_number}/answers.txt", "w")

    quiz_file.write(f"Student:\n\nDate:\n\nPeriod:\n\n\n{' '*20}Geography Quiz (Form {files_number})\n\n\n")
    answer_file.write(f"{' '*20} Answers (Form {files_number})\n\n\n")
    
    generate_questions(quiz_file, answer_file)

    quiz_file.close()
    answer_file.close()


states_and_capitals = get_states_and_capitals()

QTD_OF_TESTS = 35
QTD_OF_QUESTIONS = 50

try:
    os.makedirs("./exams")
except FileExistsError:
    print("Folder exists")

os.chdir(os.getcwd() + "/exams")

for i in range(QTD_OF_TESTS):
    create_files(i+1)