
#Initialization: DONE
import random
"""
print("Welcome To Hangman!\n----------------------------------------------------------")

user_help= int(input("Enter 1 for rules\nEnter anything else to continue\nEnter Here:"))

if user_help == 1:
  print("\n\nRules:\n-----------------------------------------------------------\n\tYou have to guess letters belonging to a random and secretive word\n\tOne wrong guess and you hangman gets a part of his body added.\n\tA full body, then he falls and you lose!\n\nReady?\nLets PLay HANGMAN!")
else:
  print("Let's Play HANGMAN!")"""

#GAME STRUCTURE: STARTED


#PRINTING STICKMAN: DONE
def StickmanPrinting(wrong):
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
WrongCount=0
WordDict = ["sunflower", "cheif", "citizen", "motivation", "trend", "ballet", "weapon", "coast", "throne","screen", "parameter"]

RandomWord= random.choice(WordDict)
print(RandomWord)
for l in RandomWord:
  print("_", end=" ")
  
RandomList = list(RandomWord)
print(RandomList)

while WrongCount < 6:




    LetterInput = input("\nEnter a letter:")
    print("HI")
    guessedletters=[]
  
    if LetterInput not in RandomList or LetterInput in guessedletters:
        
        print(guessedletters)
        WrongCount+=1
        StickmanPrinting(WrongCount)
        for l in RandomWord:
            print("_", end=" ")
        print(WrongCount)

    elif LetterInput in RandomList and LetterInput not in guessedletters:
        print('Goodjob')
        StickmanPrinting(WrongCount)
        guessedletters.append(LetterInput)
        print(guessedletters)
        for l in RandomWord:
            print("_", end=" ")
        

        

if WrongCount==6:
    print("THE END")
    StickmanPrinting(WrongCount)
    print(RandomWord)
                