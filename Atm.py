money = int(input("How much money do you have in your account?: "))
cash_withdrawl = int(input("How much money do you want to withdraw?: "))

class atm(object):
    def __init__(self,pin_number):
        self.pin_number = pin_number
    def MONEY(self):
        print("You have",money,"dollars in your account.")
    def CashWithdrawl(self):
        print("You took out",cash_withdrawl,"dollars.")
    def BalanceEnquiry(self):
        print("You now have",money-cash_withdrawl,"dollars in your account.")

atm_card = atm("908765453")

atm_card.MONEY()
atm_card.CashWithdrawl()
atm_card.BalanceEnquiry()
