print('Welcome To My MasterQuiz!')

play = input('Would You Like To Play? ')
score = 0
if play.lower() != 'yes':
  quit()

print("Alright, Let's Start!" )  

answer = input("Which language is used to style web pages (Write it in full)? ")

if answer.lower() == "cascading style sheets":
  print("Correct!")
  score +=1

else:
  print("Incorrect")  



answer = input("What does VPN stand for? ").lower()

if answer == "virtual private network":
  print("Correct!")
  score +=1
else:
  print("Incorrect")  


answer = input("Which keyword is used to define a function in Python? ").lower()

if answer == "def":
  print("Correct!")
  score +=1
else:
  print("Incorrect")  



answer = input("What does API stand for? ").lower()

if answer == "application programming interface":
  print("Correct!")
  score +=1
else:
  print("Incorrect") 



answer = input("Which function is used to get user input in Python? ").lower()

if answer == "input()":
  print("Correct!")
  score +=1
else:
  print("Incorrect")  


answer = input("What keyword is used to exit a loop in Python? ").lower()

if answer == "break":
  print("Correct!")
  score +=1
else:
  print("Incorrect")  

print("You Got " +  str(score) +" Questions Correct")
print("You Got " +  str((score/6)*100) +"%")