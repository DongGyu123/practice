#함수

def open_account():
    print("새로운 계좌가 생성되었습니다")
open_account()

#전달값과 반환값
def deposit(balance, money):
    return balance+money

balance=0
balance=deposit(balance, 1000)

def new_account(balance, money):
    if balance >= money:
        print("돈이 {0} 만큼 출금되었고 {1}원이 잔고에 남았습니다".format(money, balance-money))
        return balance-money
    else:
        print("잔액이 부족합니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

balance=new_account(balance, 500)
balance=new_account(balance, 1100)

def withdraw_night(balance, money):
    commission=100
    return commission, balance-money-commission

balance=0
balance=deposit(balance, 10000)
commission, balance=withdraw_night(balance, 500)

print("수수로 {0}원이며, 잔액은 {1}원입니다".format(commission, balance))

