print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

   


#used for loop below:


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

namee1=name1.lower()
namee2=name2.lower()


names1= int(sum(namee1.count(x) for x in ("t", "r", "u",'e')))
names2= int(sum(namee2.count(x) for x in ("t", "r", "u",'e')))
final=names1+names2

names11= int(sum(namee1.count(x) for x in ("l", "o", "v",'e')))
names22= int(sum(namee2.count(x) for x in ("l", "o", "v",'e')))
final1=(names11)+(names22)
finall= str(final)+str(final1)
print('your score is ' +finall)