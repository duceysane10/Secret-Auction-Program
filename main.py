from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
beci={}
biding_finish = False

def find_highst_bider(biding_record):
  highst_bider = 0
  for bider in beci:
    bider_amount = beci[bider]
    if bider_amount > highst_bider:
      highst_bider = bider_amount
      winar = bider
  print(f"the winar is {winar} with a bid of {highst_bider}")
    
    

while not biding_finish:
  pid_name = input("what is your name?: ")
  pid_pr= int(input("what are your pid $"))
  beci[pid_name]=pid_pr
  should_continue = input("is there any other biding yes or no. \n")
  if  should_continue =="no":
    biding_finish = True
    find_highst_bider(beci)
  elif  should_continue == "yes":
    clear()
