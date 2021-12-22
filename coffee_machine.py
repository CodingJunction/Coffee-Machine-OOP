class coffeemachine:
    def __init__(self):
        self.a=1000
        self.b=1000
        self.c=1000
    def resources(self):
        print('Water',self.a,'ml')
        print('Coffee',self.b,'ml')
        print('Milk',self.c,'ml')
    
    def check(self,val):
        if val==1:
            if self.a-200<0:
                return 0
            if self.b-24<0:
                return 0
            if self.c-150<0:
                return 0
            self.a-=200
            self.b-=24
            self.c-=150
            return 1
        if val==2:
            if self.a-15<0:
                return 0
            if self.b-18<0:
                return 0
            self.a-=15
            self.b-=18
    
            return 1
        if val==3:
            if self.a-250<0:
                return 0
            if self.b-24<0:
                return 0
            if self.c-100<0:
                return 0
            self.a-=250
            self.b-=24
            self.c-=100
            return 1
    
    def run(self,val):
        coffee=""
        p1,p2,p3=100,200,300
        p=0
        one=int(input('Enter the number of ₹1 coins : ₹'))
        two=int(input('Enter the number of ₹2 coins : ₹'))
        five=int(input('Enter the number of ₹5 coins : ₹'))
        ten=int(input('Enter the number of ₹10 coins : ₹'))
        twenty=int(input('Enter the number of ₹20 coins : ₹'))
        total=one+(two*2)+(five*5)+(ten*10)+(twenty*20)
        if val=="latte":
            coffee="latte"
            chk=self.check(1)
            if chk==0:
                print('Insufficient quantity ')
                return 
            p=p2
        elif val=="expresso":
            coffee="expresso"
            chk=self.check(2)
            if chk==0:
                print('Insufficient quantity ')
                return 
            p=p1
        elif val=="cappuccino":
            coffee="cappuccino"
            chk=self.check(3)
            if chk==0:
                print('Insufficient quantity ')
                return
            p=p3
        change = total-p
        if change>=0:
            print(f'Here is your ₹ {change}')
            print(f'Here is your {coffee} , Enjoy it !!!')
        else:
            print("Insufficient amount !!!")
        return
    