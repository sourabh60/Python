height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi= weight / (height*height)

bmii=round(bmi,2)
if(bmii <=18):
  print(f"Your BMI is"+str(bmii)+" , you are underweight.")
elif(bmii<=22):
  print("Your BMI is"+str(bmii)+" , you are normal.")
elif(bmii<=28):
  print("Your BMI is"+str(bmii)+" , you are slightly overweight.")
elif(bmii<=22):
  print("Your BMI is"+str(bmii)+" , you are obese.")
else:
  print("Your BMI is"+bmii+" , you are clinically obese.")