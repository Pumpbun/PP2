#ex.1
class Cl():
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())

b = Cl()
b.getString()
b.printString()

#ex.2
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length * self.length
    
if __name__ == "__main__":
    square = Square(int(input()))
    print(square.area())

#ex.3
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.width = width
        self.length = length
    def area(self):
        return self.length * self.width

slength = float(input())
s = Square(sL)
print(s.area())

rlength = float(input())
rwidth = float(input())
r = Rectangle(rlength, rwidth)
print(r.area())

#ex.4
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def show(self):
        print("coordinates: (" + self.x + ";" + self.y + ")")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = (dx**2 + dy**2)**0.5
        return distance

p1 = input()
p2 = input()
p1.show()
p2.show()
p1.move()
p1.show()
dist(p1, p2)

#ex.5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit of " + amount + " successful. New balance: " + self.balance)
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawal of " + amount + " successful. New balance: " + self.balance)

#ex.6
class PrimeFilter:
    def is_prime(self, num):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def filter_primes(self, numbers):
        return list(filter(lambda x: self.is_prime(x), numbers))