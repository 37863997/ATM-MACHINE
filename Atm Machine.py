# Creating an ATM Machine

# initial balance
Balance= 1000.0

def Atm():
    print("Welcome to the Atm Machine")
    while True:
        print("\nPlease choose an option:")
        print("1.Check balance")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Exit")
 # Enter your choice whether to withdraw,check balance or Deposit
        Option=int(input("\nEnter your Option:"))
        if Option ==1:
            print(f"\nYour current balance is: Ksh{Balance:.2f}")
# Deposit amount option
        elif Option ==2:
            deposit_amount=float(input("\nEnter amount to deposit: Ksh"))
            if deposit_amount>0:
                
                Balance=Balance+deposit_amount
                print(f"\nYou have successfully Deposited Ksh{deposit_amount:.2f}")
                print(f"Your new Balance is:Ksh{Balance:.2f}")
            else:
                print("\nInvalid deposit_amount .Please try again.")
# Withdrawal amount option
        elif Option ==3:
            withdraw_amount=float(input("\nEnter amount to withdraw: Ksh"))
            if 0 < withdraw_amount<=Balance:
                Balance=Balance-withdraw_amount
                print(f"\nYou have successfully withdrwan ${withdraw_amount:.2f}") 
                print(f"Your new balance is:Ksh{Balance:.2f}")
            else:
                print("\nInvalid withdrawal amount.Please try again")
        elif Option == 4:
            print("\nThank you for using the ATM.Goodbye!")
            break
        else:
            print("\nInvalid choice.Please try again.")




    


        