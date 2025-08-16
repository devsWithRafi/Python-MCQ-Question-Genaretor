## Owner - "Saiful Islam Rafi"
Questions = [
    # Default Questions ---------------
    {'Ques':'What does OOP stand for?', 
    'options':[
        {'option':'A', 'text':'Object Oriented Programming', 'answer': True},
        {'option':'B', 'text':'Online Operating Program', 'answer': False},
        {'option':'C', 'text':'Open Object Protocol', 'answer': False},
        {'option':'D', 'text':'Optional Oriented Process', 'answer': False},
    ]},
    
    {'Ques':'Which of the following is used for styling web pages?', 
    'options':[
        {'option':'A', 'text':'HTML', 'answer': False},
        {'option':'B', 'text':'CSS', 'answer': True},
        {'option':'C', 'text':'JavaScript', 'answer': False},
        {'option':'D', 'text':'SQL', 'answer': False},
    ]},
    
    {'Ques':'In React.js, which hook is commonly used for managing state?',
    'options':[
        {'option':'A', 'text':'useState', 'answer': True},
        {'option':'B', 'text':'useRouter', 'answer': False},
        {'option':'C', 'text':'useStyle', 'answer': False},
        {'option':'D', 'text':'useMap', 'answer': False},
    ]},
    
    {'Ques':'Which SQL command is used to retrieve data from a database?', 
    'options':[
        {'option':'A', 'text':'INSERT', 'answer': False},
        {'option':'B', 'text':'DELETE', 'answer': False},
        {'option':'C', 'text':'SELECT', 'answer': True},
        {'option':'D', 'text':'UPDATE', 'answer': False},
    ]},
    
    {'Ques':'Which of the following is a NoSQL database?', 
    'options':[
        {'option':'A', 'text':'MySQL', 'answer': False},
        {'option':'B', 'text':'PostgreSQL', 'answer': False},
        {'option':'C', 'text':'MongoDB', 'answer': True},
        {'option':'D', 'text':'Oracle', 'answer': False},
    ]},
    
    {'Ques':'Which protocol is primarily used for client-server communication on the web?', 
    'options':[
        {'option':'A', 'text':'FTP', 'answer': False},
        {'option':'B', 'text':'SMTP', 'answer': False},
        {'option':'C', 'text':'HTTP', 'answer': True},
        {'option':'D', 'text':'SSH', 'answer': False},
    ]},
    
    {'Ques':'In the Software Development Life Cycle (SDLC), which phase comes first?', 
    'options':[
        {'option':'A', 'text':'Testing', 'answer': False},
        {'option':'B', 'text':'Design', 'answer': False},
        {'option':'C', 'text':'Planning/Requirement Analysis', 'answer': True},
        {'option':'D', 'text':'Deployment', 'answer': False},
    ]},
    
    {'Ques':'Agile methodology mainly focuses on:', 
    'options':[
        {'option':'A', 'text':'Strict documentation', 'answer': False},
        {'option':'B', 'text':'Iterative development and customer collaboration', 'answer': True},
        {'option':'C', 'text':'One-time project delivery', 'answer': False},
        {'option':'D', 'text':'Waterfall model improvements', 'answer': False},
    ]},
]

# Get the correct ansewer for the MCQ ----------
def takeChoice_of_anseres():
    take_choice = input("Enter your right ansere(A/B/C/D): ").title()
    if take_choice in ['A','B','C','D']:
        return take_choice
    else:
        print(f"Error: '{take_choice}' Invalid Choice!")
        exit()

# Show the questions to user ----------
def showQuestions():
    for QuesNum, Ques in enumerate(Questions, 1):
        print(f"\n({QuesNum}) - {Ques['Ques']}")
        correcAnser = None # for showing the correct anseres
        for QuesOps in Ques['options']:
            print(f" {QuesOps['option']} : {QuesOps['text']}")
        
        for get_Correct_Ansere in Ques['options']:
            if get_Correct_Ansere['answer'] == True: correcAnser = get_Correct_Ansere

        user_choice = takeChoice_of_anseres() # stored function to variable

        selected_choice = next(
            choice for choice in Ques['options'] if choice['option'] == user_choice
        )

        if selected_choice['answer'] == True:
            print("\nCorrect Answere ✔")
        else:
            print("\nWrong Answere ❌")
            print(f"Correct Answere is '{correcAnser['option']} : {correcAnser['text']}' ✔\n")
            break

    print("Congrats! You have answered all questions.")

# Creating new Questions ------------
def create_new_questions():
    take_question = input("Enter your questions title: ").capitalize()
    new_question = {
        'Ques': take_question,
        'options':[]
    }
    for i in range(4):
        letterOptions = chr(65 + i) # 'A' has ASCII code 65, so (65 = 'A')
        take_question_options = input(f"Enter your options {letterOptions}: ").capitalize()
        new_question['options'].append({
            'option':letterOptions,
            'text': take_question_options,
            'answer':False
        })
    get_the_trueValue = input("Enter your true option (A/B/C/D): ").title() # dont use 'capitalize()'
    if get_the_trueValue in ['A', 'B', 'C', 'D']:
        print(f"Your ture option '{get_the_trueValue}' is added to your questions ✔")
        for i in new_question['options']:
            if get_the_trueValue == i['option']: 
                i['answer'] = True
    else: 
        print("⚠ Invalid type!")

    Questions.append(new_question) # add new question to 'Questions' dictionary

# Display all the Questions ----------
def show_all_questions():
    print(f"\nYou have total '{len(Questions)}' questions: ")
    for QuesNum, allQues in enumerate(Questions, 1):
         print(f"({QuesNum}) - {allQues['Ques']}")
    take_inputs =  input("\nDid you want to solve this? (Y/N) ").title()
    if take_inputs == "Y": showQuestions()
    elif take_inputs == "N": return
    else: print("⚠ Command not found!")

# Deleting Questions ----------
def delete_question():
    if len(Questions) == 0:
        print("⚠ You haven't any questions to delete!")
    else:
        try:
            take_delete_input = int(input("Enter the number of questions you want to Delete: "))
            Questions.pop(take_delete_input - 1)
            print("Your question has been deleted successfully ✔")
        except Exception as error:
            print("⚠ Error: Invalid command")
            print(f"⚠ {error}")

# Giving users a last chance -----
def give_last_chance():
    takeIinput = input("Want to try again ?(Y/N)  ").title()
    if takeIinput == "Y": showQuestions()
    elif takeIinput == "N": print("Thank you! Have a greate day.")
    else: print("⚠ Invalid command ")


while True:
    print(
        "\n1: Solve MCQ Questions\n"
        "2: Add new Questions\n"
        "3: Show my all Questions\n"
        "4: Delete Questions\n"
        "0: Exit Game\n"
    )

    take_user_options = input("Enter your choice: ")
    # Main Executions --------
    if take_user_options == '1': showQuestions(), give_last_chance()
    elif take_user_options == '2': create_new_questions()
    elif take_user_options == '3': show_all_questions()
    elif take_user_options == '4': delete_question()
    elif take_user_options == '0': print("Game Exited, Byee!"), exit()
    else: print(f"⚠ '{take_user_options}' Command Not Found!")

