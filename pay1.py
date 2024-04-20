

  
  
  
# banking
def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

def deposit(account, amount):
    account['balance'] += amount
    account['transactions'].append(f"Deposit: ${amount}")
    print(f"Deposit successful. Remaining balance: ${account['balance']}")

def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    return account['transactions']

mail1 =  "rizwan@gmail.com"
pso=9740608412
otp=345
mail=str(input("enter the your email:"))
if(mail == mail1):
     pso1=int(input("enter the possward:"))
     if(pso == pso1):
          print("otp = 345")
          otp1=int(input("enter your otp:"))
          if (otp == otp1):
              print("login successful")
              star=50
              print("*"*star)
              word="welcom to paytm"
              width=50
              print(word.center(width))
              # Create an account dictionary
              account = {'balance': 1000,'transactions': []}
              # Dictionary to map user choices to functions
              choices = {
                                 '1': deposit,
                                 '2': withdraw,
                                 '3': get_balance,
                                 '4': get_transaction_history
                                  }

              while True:
                  print("\n1. Deposit")
                  print("2. Withdraw")
                  print("3. Check Balance")
                  print("4. Transaction History")
                  print("5. Exit")

                  choice = input("Enter your choice: ")

                  if choice == '5':
                      print("Exiting program.")
                      break

                  if choice in choices:
                      if choice == '1' or choice == '2':
                          amount = float(input("Enter amount: "))
                          choices[choice](account, amount)
                      else:
                         print(choices[choice](account))
                  else:
                      print("Invalid choice. Please try again.")

          else:
               print("invalid otp")
     else:
         print("invalid possword")
else:
    print("invalid email")

