#--------Grade  Calculator--------
print("--------Grade calculator------")
print("Enter the marks of 5 subjects(out of 100):\n")

subjects=["Maths","English","Physics","Chemistry","CS"]
marks=[]
total=0

for subject in subjects:
  while True:
    mark=int(input(f"{subject}:"))
    if 0<=mark<=100:
      marks.append(mark)
      total+=mark
      break
    else:
      print("Marks should be between 0 and 100.")

percentage=total/5

print(f"------Results----\n")
print(f"Total:{total}/500")
print(f"Percentage:{percentage:.2f}%")

if percentage>=90:
  grade="A+"
elif percentage>=80:
  grade="A"
elif percentage>=70:
  grade="B"
elif percentage>=60:
  grade="C"
elif percentage>=40:
  grade="D" 
else:
  grade="F"

print(f"Grade:{grade}")

if percentage>=40:
  print("Result:PASSED ✅")
else:
  print("Result:FAILED ❌")