questions = ["Q.1 what is capital of India?", "Q.2 What is     the currency of korea? ", "Q.3 who wrote vol 1. song ? ", "Q.4 Cape town is capital of which country ?", "Q.5 In july 2024, which former player of indian cricket team was appointed as the head coach of Indian Mens cricket Team?", "Q.6 What is full form of NTA body which conducts The jee and Neet examination?", "Q.7 Out of acne , eczema, epilepsy, bronchitis , how many Primarily affect the skin? "]
print("\n Deviyon Aur Sajjano swagat hai apka 'Kaun Banega Crorepati' mein")
print(questions[0])
user_input = str(input("Ans:"))
if (user_input == 'Delhi' or user_input == 'delhi'):
 print(questions[1])
 user_input2 = str(input("Ans:"))
 if (user_input2 == 'Won'or user_input2 == 'won'):
   print(questions[2])
   user_input3 = str(input("Ans:"))
   if (user_input3 == "honey singh" or user_input3 == "honey paaji" or user_input3 == "Honey singh" or user_input3 == "Honey paaji" ):
    print(questions[3])
    user_input4 = str(input("Ans:"))
    if (user_input4 == 'South Africa' or user_input4 == 'South africa' or user_input4 == 'south africa'):
     print(questions[4])
     user_input5 = str(input("Ans:"))
     if (user_input5 == 'Gautam Gambhir' or user_input5 == 'Gautam gambhir' or user_input5 == 'gautam gambhir'):
      print(questions[5])
      user_input6 = str(input("Ans:"))
      if (user_input6 == 'National Testing Agency' or user_input6 == 'National testing agency' or user_input6 == 'national testing agency'):
       print(questions[6])
       user_input7 = str(input("Ans:"))
       if (user_input7 == 'Eczema' or user_input7 == 'eczema'):
        print("Congratulation ! You won the game and prize money of 28000 Rs.")
       else:
        print("You won 21000 Rs. only")
      else:
       print("sorry You won 10000 Rs. only ")
    else:
      print("sorry u won only 6000 Rs.")
   else:
    print("sorry you won only 3000 Rs.  ")

 else:
   print("sorry wrong answer , You won only 1000 Rs.")
else:
  print("sorry! You are out.")


 

