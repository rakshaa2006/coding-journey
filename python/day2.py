#-----SECTION 1:Basic if/else------

age=int(input("Enter your age:"))

if age>=18:
  print("You are adult")
else:
  print("You are minor")

#-----SECTION 2:elif chain-------

marks=int(input("Enter your marks:"))

if marks>=90:
  print("Grade: A")
elif marks>=80:
  print("Grade:B")
elif marks>=60:
  print("Grade:C")
elif marks>=40:
  print("Grade:D")
else:
  print("Grade:F study harder.")


#-----SECTION 3:and/or-----
username=input("Username:")
password=input("Password:")
if username=="admin" and password=="1234":
  print("login successfull")
else:
  print("Wrong credentials")


#------SECTION 4:match statement-----

day=input("Enter the day:").lower()

match day:
  case "mon":
    print("Start of the grind.")
  case "fri":
    print("Almost weekend.")
  case "sat"|"sun":
    print("Weekend--Still code.")
  case _:
    print("Midweek.Stay focused.")



