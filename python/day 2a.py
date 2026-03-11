#------SECTION 5: while loop------
count=1
while count<=5:
  print(f"Count:{count}")
  count+=1


#------SECTION 6: for loop------
fruits=["banana","mango","apple"]
for fruit in fruits:
  print(f"I like {fruit}")


#------SECTION 7: range------
for i in range(1,11):
  print(f"{i}*2={i*2}")


#------SECTION 8: break and continue-------
for i in range(1,20):
  if i==13:
    continue
  if i==16:
    break
  print(i)
  

#------SECTION 9: input validation loop------
while True:
  age=int(input("Enter your age:"))
  if age>0:
    break
  print("Age must be positive.Try again.")
print(f"You are {age} years old.")