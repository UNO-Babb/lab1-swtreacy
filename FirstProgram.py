#FirstProgram.py
#Name: Sean Treacy
#Date: September 1st, 2024
#Assignment: First Program

def main():
  print("First Program")
  #Say hello
  print("Hello, nice to meet you!")
  #Ask for the user's name
  name = input("Please state your name.")
  #Use the user's name in the program.
  print("A pleasure to be acquainted with you,", name)
  #Ask the user for their age.
  age = input("How old are you?")
  age = int(age)
  #Tell the user what year they were born in.
  born = 2024 - age
  #Assume that they have not had their birthday yet this year.
  print("You were born in", born)

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
