#Function-------------------------------------------------------------------------------
def Prime_number_checker():
    num = int(input("Enter the number you want to check for prime: "))
    if num <= 1:
        print("Not a Prime Number")
        return
    prime = True #Flagging Variable
    for j in range(2, num):
        if num % j == 0:
            prime = False
            break

    if prime:
        print(f"The number {num} is a Prime Number")
    else:
        print(f"The number {num} is not a Prime Number")
#----------------------------------------------------------------------------------------           
while True:

  print("========== Prime Number Checker ==========")
  print("1.Check for Prime Number\n2.Exit\n")
  choice=int(input("Enter (1-2):"))
  if choice==1:
      Prime_number_checker() #function_call

  elif choice==2:
    print("Exiting Checker...")
    print("Exit Successsful")
    break
  
  else:
    print("Invalid Choice:")
#-----------------------------------------------------------------------------------------    