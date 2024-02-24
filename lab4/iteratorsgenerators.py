#ex.1
def squares(n):
    for i in range(1, n):
        yield i**2
def main():
    n = int(input())
    for i in squares(n+1):
        print(i)
if __name__ == "__main__":
    main()

#ex.2
def genEvens(n):
    for i in range(0, n):
        if i % 2 == 0:
            yield i
        else:
            StopIteration
def main():
    n = int(input())
    for i in genEvens(n+1):
        print(i, end = ", ") 
if __name__ == "__main__":
    main()

#ex.3
def g(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
        else:
            StopIteration
n = int(input())
for i in g(n):
    print(i)

#ex.4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2
def main():
    a = int(input())
    b = int(input())
    for i in squares(a, b):
        print(i)
if __name__ == "__main__":
    main()

#ex.5
def nums(n):
    for i in range(n+1)[::-1]:
        yield i 
def main():
    n = int(input())
    for i in nums(n):
        print(i)
if __name__ == "__main__":
    main()