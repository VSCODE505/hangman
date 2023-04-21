#Initialization: DONE
import re
import random
print("Welcome To Hangman!\n----------------------------------------------------------")

user_help= int(input("Enter 1 for rules\nEnter anything else to continue\nEnter Here:"))

if user_help == 1:
  print("\n\nRules:\n-----------------------------------------------------------\n\tHangman is a guessing game for two or more players. \n\tOne player thinks of a word, phrase or sentence and the other(s) tries to guess it by suggesting letters within a certain number of guesses.\n\tEvery time the player guesses incorrectly another body part adds to the hangman.\n\tThere are 6 body parts; the head, the body, the right arm, the left arm, the right leg, and the left leg. \n\tWhen the guesser completes the body, the hangman falls, and the guesser loses, while the one who chose the word wins.\n\tHowever, if the guesser guesses the word before the body is complete, the guesser wins.\n\tBut, since we have coding and machines in this world, you can play by yourself!\n\nReady?\nLets PLay HANGMAN!")
else:
  print("Let's Play HANGMAN!")

#GAME STRUCTURE: STARTED


#PRINTING STICKMAN: DONE
def stickman_printing(wrong):
   if(wrong == 0):
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
   elif(wrong == 1): 
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("   ===")
   elif(wrong == 2):
    print("\n+---+")
    print("O   |")
    print("|   |")
    print("    |")
    print("   ===")
   elif(wrong == 3):
    print("\n+---+")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("   ===")
   elif(wrong == 4):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("   ===")
   elif(wrong == 5):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("   ===")
   elif(wrong == 6):
    print("\n+---+")
    print(" O   |")
    print("/|\  |")
    print("/ \  |")
    print("    ===")


#INTERNAL MECHANICS
wrong_count=0
word="_"
WORD_DICTIONARY = ["sunflower", "cheif", "citizen", "motivation", "trend", "ballet", "weapon", "coast", "throne","screen", "parameter"]
guessed_letters=[]
random_word = random.choice(WORD_DICTIONARY)
for l in random_word:
    print("_", end=" ")
   
random_word_list = list(random_word)
print(random_word_list)

for l in range(1,len(random_word)):
    word= word+"_"
    
word=list(word)

while wrong_count < 6:
    random_word_list_sorted = [*set(random_word_list)]
    guessed_letters_sorted=guessed_letters
    random_word_list_sorted.sort()
    guessed_letters_sorted.sort()    
    letter_input = input("\nEnter a letter:")
      
    if random_word_list_sorted == guessed_letters_sorted:
        print("YOU WON")
        break
    elif letter_input not in random_word or letter_input in guessed_letters:    
        wrong_count+=1
        stickman_printing(wrong_count)
        print(word)
    elif letter_input in random_word_list and letter_input not in guessed_letters:
        print('Good Job!')
        stickman_printing(wrong_count)
        guessed_letters.append(letter_input)
        print(guessed_letters) 
        indexes=[m.start() for m in re.finditer(letter_input, random_word)]
        print(indexes)
        if len(indexes) == 1:
          indexnum=random_word_list.index(letter_input)
          print(word[indexnum])
          word[indexnum]=random_word[indexnum]
          print(word)
        else:
          for x in indexes:
            word[x] = random_word[x]
          print(word)

if wrong_count==6:
    print("GAME OVER")
    stickman_printing(wrong_count)
    print(random_word)

