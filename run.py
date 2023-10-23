# This function creates a new game when is called

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------------------------------------------------------------------------------")
        print(key)
        """
        Displays all the different options for each question,
        takes the input answer from the player and
        converts to uppercase if the user typed lowercase

        """
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter your answer (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# This function checks the answers provided by the user

def check_answer(answer, guess):
    
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# This function displays the score 

def display_score():
    pass
# This function starts a new game when the player answers yes
def play_again():
    pass


questions = {
 "Roger Taylor is the drummer in which band?: ": "A",
 "In which year did the Spice Girls release Wannabe?: ": "B",
 "Which rock band was founded by Trent Reznor in 1988?: ": "A",
 "In what year did Elvis Presley die?: ": "D",
 "Which Bob Dylan song did Adele include on her first album?: ": "C",
 "What was the name of the band formed by Jack Bruce, Eric Clapton, and Ginger Baker?: ": "C",
 "Singer Fergie was previously a member of which hip hop group?: ": "B",
 "Which singer had a charts resurgence in 2022 after one of her songs was heard in Stranger Things?: ": "D",
 "Rock band AC/DC originates from which country?: ": "C",
 "Rockstar David Howell Evans is better known by what name?: ": "B",

}

options = [["A. Queen", "B. Led Zeppelin", "C. Kiss", "D. The Smashing Pumpkins"],
    ["A. 1992", "B. 1996", "C. 1995", "D. 1993"],
    ["A. Nine Inch Nails", "B. Tool", "C. Rammstein", "D. White Zombie"],
    ["A. 1978","B. 1975", "C. 1979", "D. 1977"],
	["A. Hurricane","B. Blowin' In The Wind", "C. Make You Feel My Love", "D. Tangled Up In Blue"],
    ["A. Led Zeppelin","B. Genesis", "C. Cream", "D. The Who"],
    ["A. The Pussycat Dolls","B. The Black Eyed Peas", "C. No Doubt", "D. Outkast"],
    ["A. Björk","B. PJ Harvey", "C. Tina Turner", "D. Kate Bush"],
    ["A. USA","B. England", "C. Australia", "D. Denmark"],
    ["A. Hozier","B. The Edge", "C. Gene Simmons", "D. Bono"]]

new_game()
