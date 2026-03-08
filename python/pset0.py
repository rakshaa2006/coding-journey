#Indoor voice
text=input()
print(text.lower())


#Playback Speed
text=input()
text=text.replace(" ","...")
print(text)


#Making Faces

text=input()
text=text.replace(":)","🙂")
text=text.replace(":(","🙁")
print(text)

#Einstein
m=float(input("Enter the mass in kg:"))
c=300000000
e=m*c**2
print(f"Energy {e} in joules ")

#Tip calculator
bill=float(input("Enter the bill amount:"))
tip=float(input("Enter the tip percentage:"))
tip_amount=bill*tip/100
print(f"Tip amount: ${tip_amount :.2f}")