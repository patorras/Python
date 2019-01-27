import random, pyperclip


com = random.randint(10,30)  #size of pass
password = chr(random.randint(48,122)) #begining of pass

for i in range(com):
  password = password + chr(random.randint(48,122))

print(password)
pyperclip.copy(password)
