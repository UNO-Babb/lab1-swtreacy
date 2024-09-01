#MadLib.py
#Name: Sean Treacy
#Date: September 1st, 2024
#Assignment: MadLib

def main():
  print("Madlib")
  #Ask user for words
  person = input("Please write a person")
  place = input("Please write a place")
  object = input("Please write an object")
  adjective = input("Please write an adjective")
  number = input("Please write a number")
  emotion = input("Please write an emotion")
  #Print the story with the user supplied words.
  print("I went to" , place , "with" , person , "to pick up" , number , adjective , object , ". This made me" , emotion + "!" )


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
