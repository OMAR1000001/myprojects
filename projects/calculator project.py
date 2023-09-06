logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
def add(n1,n2):
    return n1+n2

def subtarct(n1,n2):
    return n1-n2

def mutiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

# في الحقيقه عندما يطلب المستخدم عمل عمليه معينه فأنه سيكت الرمز اللذي يدل علي العمليه لا الكلمه الدله لذالك يجب ترجمة العمليه اللي الرمز الدال عليها
opreations = {
    "+": add,
    "-": subtarct,
    "*": mutiply,
    "/": divide
}
# نطلب الرقمين و رمز العمليه
num1=float(input("write the first number her: "))
opreation_symbol=input("pick the opreation from the line above( + , - , * , /)  ")
num2=float(input("write the second number her: "))

def calc(num1,num2,opreation_symbol):
    # نترجم الرمز الذي ادخله الشخص عن طريق القاموس
    chosen_syb= opreations[opreation_symbol]
    # بعد ترجمه الرمز لكلمه و الكلمه لها داله ناخذ الداله ( و التي تدل علي عمليه حسابيه معينه ) و نضع بها الارقم لنصل للنتيجه
    answer = (chosen_syb(num1, num2))
    return answer
answer=(calc(num1=num1,opreation_symbol=opreation_symbol,num2=num2))
print(answer)

yy=True

while yy:
    contanue = input("Do you want to contanue ? y/n ")
    if contanue == "y":
        opreation_symbol2 = input("pick the opreation from the line above( + , - , * , /)  ")
        num21 = float(input("write the second number her: "))
        answer2 =(calc(num1=answer,opreation_symbol=opreation_symbol2,num2=num21))
        print(answer2)

    if contanue =="n":
        yy=False
    else:
        print("try again")