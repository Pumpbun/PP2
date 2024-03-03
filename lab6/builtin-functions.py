#ex.1
def multiplication(l):
    for i in range(len(l)):
        l[i] = int(l[i])
    c = 1
    for num in l:
        c *= num
    return c
def main():
    l = (input().split())
    print(multiplication(l))
if __name__ == "__main__":
    main()

#ex.2
def counter(string):
    cnt_upper = 0
    cnt_lower = 0
    for i in string:
        if i.isupper():
            cnt_upper += 1
        elif i.islower():
            cnt_lower += 1
    return cnt_upper, cnt_lower
def main():
    string = input()
    upper, lower = counter(string)
    print("Number of upper case letters: ", upper)
    print("Number of lower case letters: ", lower)
if __name__ == "__main__":
    main()

#ex.3
def palindrome(s):
    rs = ''.join(reversed(s))
    if s == rs:
        print("Palindrome")
    else:
        print("Not a palindrome")
def main():
    s = input()
    palindrome(s)
if __name__ == "__main__":
    main()

#ex.4
import math
import time
def square(n, ms):
    time.sleep(ms / 1000.0)
    return math.sqrt(n)
def main():
    n = int(input())
    ms = int(input())
    result = square(n, ms)
    print("Square root of ", n, " after ", ms, " miliseonds is ", result)
if __name__ == "__main__":
    main()

#ex.5
def true(t):
    return all(t)
def main():
    t = input()
    t1 = [eval(char) for char in t.split()]
    print(true(t1))
if __name__ == "__main__":
    main()