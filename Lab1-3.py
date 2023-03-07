name = input("What is your name? ")
print("Name: " + name)

labGrade = input("Enter your lab grade? ")
print("Lab: " + labGrade)
labGrade = float(labGrade)

midTermGrade = input("Enter your lab grade? ")
print("Lab: " + midTermGrade)
midTermGrade = float(midTermGrade)

finalGrade = input("Enter your lab grade? ")
print("Lab: " + finalGrade)
finalGrade = float(finalGrade)

lastScore = (labGrade*0.25) + (midTermGrade*0.35) + (finalGrade*0.4)
lastScore = str(lastScore)
print("Last Score :" + lastScore)