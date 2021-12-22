"""Coffee machine water coffee
1. expresso 50 18 1.5
2. latte 200 24 150 2.5
3. cappuccino 250 24 100 3.0

coin operateed
1 2 5 10 20

report

"""
from coffee_machine import coffeemachine
obj=coffeemachine()
cond=True
while cond:

    print("""This is a Coffee Machine
You can choose :
expresso
latte
cappuccino
You can enter:
off - turn off the machine
report - to get details on remaining resources""")
    p=0
    val = input()
    if val=="report":
        obj.resources()
    elif val=="off":
        print('The machine is turning off')
        cond=False
    else:
        obj.run(val)

