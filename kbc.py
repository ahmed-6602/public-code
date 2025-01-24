question = [
    'who is the developer of python language?'
    'when did india get independence?'
    'what is the currency in india?'
    'which state does bangalore belongs to? '
    'which is the latest i phone?'
]

answer = [
    'guido van'
    '1947'
    'inr'
    'karnataka'
    'i phone 14'
]

options = [
    ['albert', 'raju', 'guido van', 'david'],
    ['1854', '1456', '1946', '1947'],
    ['bnr', 'inr', 'dollar', 'riyal'],
    ['karnataka', 'delhi', 'mah ara stra', 'telangana'],
    ['i phone 14', 'i phone 11i', 'i phone 15', 'i phone 23'],
]

def play_game(username, questions, answers, options):
    print("hello", username, "to kbc game")
    for i in range(len(questions)):
        current_question = questions[i]
        correct_answer = answers[i]
        current_question_options = options[i]
        print("Question: ", current_question)
        for each_option in current_question_options:
            print(each_option)

def view_scores():
    pass

def kbc(questions, answers, options):
    while True:
        print("welcome to kbc game!")
        print("1)play game\n2)view score\n3exit")
        choice = int(input("please enter  your choice :"))
        if choice == 1:
            username = input("please enter your name : ")
            play_game(username, question, answer, options)

        elif choice == 2:
            view_scores()

        elif choice == 3:
                'break'

    else:
      print("your choice is not valid")

kbc(question, answer, options)