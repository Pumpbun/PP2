import datetime
from datetime import date, timedelta, datetime, time

#ex.1
def main():
    x = date.today() - timedelta(5)
    return x
print(main())

#ex.2
def days():
    x = date.today() - timedelta(1)
    y = date.today()
    z = date.today() + timedelta(1)
    print("Yesterday: ", x)
    print("Today: ", y)
    print("Tomorrow: ", z)
days()

#ex.3
def main():
    x = datetime.datetime.today().replace(microsecond = 0)
    print(x)
if __name__ == "__main__":
    main()

#ex.4
def difference(x, y):
    timedelta = x - y
    return timedelta.days * 24 * 3600 + timedelta.seconds
def main():
    x = datetime.strptime(input(), '%Y-%m-%d')
    y = datetime.strptime(input(), '%Y-%m-%d')
    print(difference(x, y))
if __name__ == "__main__":
    main()