#------SECTION 1:Basic Functions------
def greet():
  print("Hello!,Welcome.")

greet()
print("--------------")

#-----SECTION 2:Functions with parameters-----
def greet_user(name):
  print(f"Hello {name}!,Welcome.")

greet_user("Riya")
greet_user("Ravi")
print("--------------")

#-----SECTION 3:Functions with return-----
def add(a,b):
  return a+b
result=add(3,10)
print(f"Sum:{result}")
print("--------------")

#-----SECTION 4:Multiple Parameters-----
def calculate_bmi(weight,height):
  bmi=weight/(height**2)
  return round(bmi,2)
bmi=calculate_bmi(70,1.75)
print(f"BMI:{bmi}")

if bmi<18.5:
  print("Underweight")
elif bmi<25:
  print("Normal")
elif bmi<30:
  print("Overweight")
else:
  print("Obese")
print("--------------")

#-----SECTION 5:Default Parameters-----
def greet_language(name,language="English"):
  if language=="Hindi":
    print(f"Namaste,{name}!")
  elif language=="Tamil":
    print(f"Vanakkam,{name}!")
  else:
    print(f"Hello,{name}!")
    
greet_language("Reema")
greet_language("Priya","Tamil")
print("--------------")

#-----SECTION 6:Functions calling functions-----
def get_grade(marks):
  if marks>=90:
    return "A"
  elif marks>=75:
    return "B"
  elif marks>=60:
    return "C"
  elif marks>=40:
    return "D"
  else:
    return "F"
  
def print_result(name,marks,):
  grade=get_grade(marks)
  print(f"{name}---Marks:{marks},Grade:{grade}")

print_result("Ramya",95)
print_result("Ravi",78)
print_result("Neha",35)

