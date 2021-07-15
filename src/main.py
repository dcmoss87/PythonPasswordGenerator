import re
import random

def numChar(finalPass):
  correctPass = re.compile(r'\S{8,}')
  searchObj = correctPass.search(finalPass)
  if searchObj == None:
    print("Password is not at least eight characters.")
  else:
    return True

def upCase(finalPass):
  correctPass2 = re.compile(r'[A-Z]+')
  searchObj = correctPass2.search(finalPass)
  if searchObj == None:
    print("Password does not have an upper case letter.")
  else:
    return True

def lowCase(finalPass):
  correctPass3 = re.compile(r'[a-z]')
  searchObj = correctPass3.search(finalPass)
  if searchObj == None:
    print("Password does not have a lower case letter.")
  else:
    return True

def chNum(finalPass):
  correctPass4 = re.compile(r'\d+')
  searchObj = correctPass4.search(finalPass)
  if searchObj == None:
    print("Password does not have a number.")
  else:
    return True

def chSymb(finalPass):
  correctPass5 = re.compile(r'\W+')
  searchObj = correctPass5.search(finalPass)
  if searchObj == None:
    print("Password does not have a symbol.")
  else:
    return True
    
def chkTrue(bool2, bool3, bool4, bool5, bool6):
  global bool1
  if bool2 and bool3 and bool4 and bool5 and bool6:
      print("*" *10)
      print("You have successfully entered a password!")
      print(f"Your password is: {finalPass}")
      print("*" *10)
      bool1 = False

bool1 = True
randPass = ['a','b','c','A','B','C', 1, 2, 3,'#','%','$','@']
finalPass = ''

if __name__ == "__main__":
  while bool1:
    userPass = input("Please enter a password or press enter to generate random: ")
    finalPass = userPass.replace(' ', '')

    if userPass == '':
      for x in range(8):
        finalPass = finalPass + str(random.choice(randPass))
      chkTrue(numChar(finalPass), upCase(finalPass), lowCase(finalPass), chNum(finalPass), chSymb(finalPass))
    
    else:
      chkTrue(numChar(finalPass), upCase(finalPass), lowCase(finalPass), chNum(finalPass), chSymb(finalPass))
