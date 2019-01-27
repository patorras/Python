import random, pyperclip, string


com = random.randint(10,20)  #size of pass
password = chr(random.randint(48,122)) #begining of pass

for i in range(com):
  password = password + string.ascii_letters[random.randint(0, 40)] + string.digits[random.randint(0,8)]

pyperclip.copy(password)
