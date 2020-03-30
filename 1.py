class Calculator:
    def __init__(self):
        try:
            self.a = int(input("Enter first number:"))
        except:
            print("You must Enter Integar")
            self.a = int(input("Enter first number:"))

        try:
            self.b = int(input("Enter Second number:"))
        except:
            print("You must Enter Integar")
            self.b = int(input("Enter Second number:"))

        try:
            self.c = input("Enter oprator:")
            if self.c != '+' or '-' or '*' or '/':
                print("Invalid oprator")
        except:
            if self.c != '+' or '-' or '*' or '/':
                print("Invalid oprator")
            self.c = input("Enter oprator:")

    def addition(self):
        print(self.a + self.b)
    def subtraction(self):
        print(self.a - self.b)
    def multiplication(self):
        print(self.a * self.b)
    def division(self):
       try:
           print(self.a / self.b)
       except:
           print("cannot divide by zero")
       else:
           print(self.a / self.b)
    def aaa(self):
        if self.c == '+':
            print(obj.addition())
        elif self.c == '-':
            print(obj.subtraction())
        elif self.c == '*':
            print(obj.multiplication())
        elif self.c == '/':
            print(obj.division())
obj = Calculator()
obj.aaa()