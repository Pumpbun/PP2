import math

#ex.1
def to_radians(d):
    return math.radians(d)
def main():
    d = int(input())
    print(to_radians(d))

if __name__ == "__main__":
    main()

#ex.2
def trapezoid(h, a, b):
    area = ((a + b) * h) * 1/2
    return area

def main():
    h = int(input())
    a = int(input())
    b = int(input())
    print(trapezoid(h, a, b))

if __name__ == "__main__":
    main()

#ex.3
def polygon(n, s):
    area = n * (s**2) / (4 * math.tan(math.pi / n))
    return area

def main():
    n = int(input())
    s = int(input())
    print(polygon(n, s))
    
if __name__ == "__main__":
    main()

#ex.4
def parallelogram(a, b):
    area = a * b
    return area

def main():
    a = int(input())
    b = int(input())
    print(parallelogram(a, b))

if __name__ == "__main__":
    main()