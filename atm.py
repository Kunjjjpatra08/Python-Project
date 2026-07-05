class ATM:
    print("=====ATM starting=====") 
    def __init__(self):
        self.balance=5000

    def check_balance(self):
        print("Your current balance : ",self.balance)

    def deposite(self):
        deposite_amount=int(input("Enter your deposite amount : "))
        self.balance=self.balance+deposite_amount
        print("You sucessfully deposite",self.balance,"rs")

    def withdrawl(self):
        withdrawl_amount=int(input("Enter your withdrawl amount : "))
        if withdrawl_amount<=self.balance:
            self.balance=self.balance-withdrawl_amount
            print("You sucessfully withdrawl",withdrawl_amount,"rs")
        else:
            print("Insuffient amount")    

    def exit(self):
        print("Thank you!")    

    def menu(self):
        while True:   
            print("\nEnter your choice :-")
            print("1.Check balance")
            print("2.Deposite")
            print("3.Withdrawl")
            print("4.Exit\n")

            user=int(input("Enter the options : "))

            if user==1:
                self.check_balance()

            elif user==2:
                self.deposite()

            elif user==3:
                self.withdrawl()

            elif user==4:
                self.exit()            
                break

            else:
                print("You enter invalid option")
    
atm=ATM()
atm.menu()