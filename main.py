# This is a sample Python script.
name1 = input("Insert 1st name")
name2 = input("Insert 2nd name")

combined_string = name1 + name2
lower_case_string = combined_string.lower()
t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l + o + v + e

true_love = str(true)+ str(love)

score = int(true_love)

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")

elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")

else:
  print(f"Your score is {score}")


