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
        option = "\n{}. {}".format("ABCD"[i], options[i])
        quiz_file.write(option)

    quiz_file.write("\n\n\n")

    answer_file.write("{}. {}\n".format(question_number, "ABCD"[options.index(correct_option)]))


def generate_questions(quiz_file, answer_file):
    for question_number in range(QTD_OF_QUESTIONS):
        states = list(states_and_capitals.keys())
        random.shuffle(states)

        question = "{} - What is the capital of {}?\n".format(question_number+1, states[question_number])
        quiz_file.write(question)

        generate_options(quiz_file, answer_file, states[question_number], question_number+1)


def create_files(files_number):
    try:
        os.makedirs("quiz-{}".format(files_number))
    except FileExistsError:
        print("File exists")

    quiz_file = open("./quiz-{}/questions.txt".format(files_number), "w")
    answer_file = open("./quiz-{}/answers.txt".format(files_number), "w")

    quiz_file.write("Student:\n\nDate:\n\nPeriod:\n\n\n{}Geography Quiz (Form {})\n\n\n".format(' '*20, files_number))
    answer_file.write("{} Answers (Form {})\n\n\n".format(' '*20, files_number))
    
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