#Initialization: DONE
import re
import random
print("Welcome To Hangman!\n----------------------------------------------------------")

user_help= int(input("Enter 1 for rules\nEnter anything else to continue\nEnter Here:"))

if user_help == 1:
  print("\n\nRules:\n-----------------------------------------------------------\n\tYou have to guess letters belonging to a random and secretive word\n\tOne wrong guess and you hangman gets a part of his body added.\n\tA full body, then he falls and you lose!\n\nReady?\nLets PLay HANGMAN!")
else:
  print("Let's Play HANGMAN!")

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

RandomWord = random.choice(WordDict)
for l in RandomWord:
  print("_", end=" ")
  
  
RandomList = list(RandomWord)
print(RandomList)
guessedletters=[]


    

def duplicate_characters(string):
    # Create an empty dictionary
     
     chars = {} 
 
     for char in string:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
 
     duplicates = []
 
     for char, count in chars.items():
        if count > 1:
            duplicates.append(char)


word="_"
for l in range(1,len(RandomWord)):
          word= word+"_"
word=list(word)
while WrongCount < 6:
    RandomList_sorted = [*set(RandomList)]
    guessedletters_sorted=guessedletters

    RandomList_sorted.sort()

    guessedletters_sorted.sort()
    

    LetterInput = input("\nEnter a letter:")
    
      
    if RandomList_sorted == guessedletters_sorted:
        print("YOU WON")
        break
   
    elif LetterInput not in RandomWord or LetterInput in guessedletters:
        
        print(guessedletters)
        WrongCount+=1
        StickmanPrinting(WrongCount)
        
        
        print(word)
        print(WrongCount)
        print(guessedletters)

    elif LetterInput in RandomList and LetterInput not in guessedletters:
        print('Good Job!')
        StickmanPrinting(WrongCount)
        guessedletters.append(LetterInput)
        print(guessedletters) 
        indexes=[m.start() for m in re.finditer(LetterInput, RandomWord)]
        print(indexes)
        if len(indexes) == 1:
          indexnum=RandomList.index(LetterInput)
          print(word[indexnum])
          word[indexnum]=RandomWord[indexnum]
          print(word)
        else:
          for x in indexes:
        
            word[x] = RandomWord[x]  

          print(word)


        
        
            
        
if WrongCount==6:
    print("THE END")
    StickmanPrinting(WrongCount)
    print(RandomWord)

