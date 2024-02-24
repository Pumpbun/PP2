#ex.1
def recipe(grams):
    print(28.3495231 * grams)

g = float(input())
recipe(g) 

#ex.2
def to_c(f):  
    return (5 / 9) * (f - 32)
    
a = float(input())
result = to_c(a)
print(result)

#ex.3
def solve(numheads, numlegs):

    for x in range(numheads+1):
        y = numheads - x
        if 2*x + 4*y == numlegs:
            return x, y

result = solve(numheads = 35, numlegs = 94)
if result:
    x, y = result
    print("chickens = ", x)
    print("rabbits = ", y)

#ex.4
def filter_prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:  
            return False
    return True

a = list(input())
result = filter_prime(a)
print(result)

#ex.5
from itertools import permutations
def perm(s):
    a = permutations(s)
    return list(a)
string = input()
print(perm(string))

#ex.6
def reverse(s):
    w = s.split()
    rw = " ".join(reversed(w))
    return rw

sentence = input()
print(reverse(sentence))

#ex.7
def has_33(nums):
    for i in range(len(nums)):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False    

nums = list(map(int, input().split()))

print( has_33(nums))

#ex.8
def spy_game(nums):
    for i in range(len(nums)):
        if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
            return True
    return False    

nums = list(map(int, input().split()))
print(spy_game(nums))

# ex.9 V = 4/3 π r³
def vol(r):
    return 4/3 * 3.14 * (r*r*r)

radius = int(input())
print(vol(radius))


#ex.10
def foo(list):
    unique_elements = []
    for i in list:
        if i not in unique_elements:
            unique_elements.append(i)
    return(unique_elements)

nums = list(map(int, input().split()))
print(foo(nums))

#ex.11
def palindrome(s):
    input_list = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        if input_list[left] != input_list[right]:
            return "NO!"    
        left += 1
        right -= 1    
    return "YES!"

word = input()
print(palindrome(word))
# #another solution:
# def palindrome(s):
#     r = ''.join(reversed(s))
#     if s == r:
#         print("YES")
#     else:
#         print("NO")

# word = input()
# palindrome(word)

#ex.12
def histogram(nums):
    for i in range(len(nums)):
        print("*" * nums[i])

nums = list(map(int, input().split()))
histogram(nums)  

#ex.13
import random
def guess_the_number():
    r = random.randint(1, 20)
    print("Hello! What is your name?")
    name = input()
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    counter = 0
    while True:
        print("Take a guess.")
        n = int(input())
        counter += 1
        if r > n:
            print("Your guess is too low.")

        if r < n:
            print("Your guess is too high.")

        if r == n:
            counter = str(counter)
            print("Good job, " + name + "! You guessed my number in " + counter +   " guesses!")
            break

guess_the_number()

#ex.14
