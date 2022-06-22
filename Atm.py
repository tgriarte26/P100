class Atm:
    def __init__(self,name,cardnumber,pin):
        self.name = name
        self.cardnumber = cardnumber
        self.pin = pin
    
    def BalanceInquiry(self):
        print("Money in bank: $500")
    
    def CashWithdrawl(self,amount):
        remaining_amount = 500 - amount
        print("Amount withdrawn: $" + str(amount) + ", Money left in bank: $" + str(remaining_amount))

    def CashDeposit(self,amount):
        new_amount = 500 + amount
        print("Money in bank: $" + str(new_amount))

def main():
        name = input("Hello, what is your name? ")
        print("Hello, " + name)
        cardnumber = input("Please insert your card number: ")
        pin = input("Please enter your pin: ")
        new_user = Atm(name,cardnumber,pin)

        print("What do you want to do?")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        activity = int(input("Enter choice: "))

        if (activity == 1):
            new_user.BalanceInquiry()
        elif (activity == 2):
            amount = int(input("Enter the amount you want to withdrawl: "))
            new_user.CashWithdrawl(amount)
        elif (activity == 3):
            amount = int(input("Enter the amount you want to deposit: "))
            new_user.CashDeposit(amount)
        else:
            print("Enter a valid number")

if __name__ == '__main__':
    main()
