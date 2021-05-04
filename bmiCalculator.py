height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi= weight / (height*height)
bmii=round(bmi,2)

if(bmii <18.5):
  print(f"Your BMI is {bmii}, you are underweight.")
elif(bmii<25):
  print(f"Your BMI is {bmii}, you are normal.")
elif(bmii<30):
  print(f"Your BMI is {bmii}, you are slightly overweight.")
elif(bmii<35):
  print(f"Your BMI is {bmii}, you are obese.")
else:
  print(f"Your BMI is {bmii}, you are clinically obese.")