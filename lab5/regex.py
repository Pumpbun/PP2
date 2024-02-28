import re
#ex.1
def matches(txt):
    p = re.compile('a{1}b*')
    return p.findall(txt)
def main():
    txt = input()
    print(matches(txt))
if __name__ == "__main__":
    main()

#ex.2
def matches(txt):
    p = re.compile('a{1}b{2,3}')
    return p.findall(txt)
def main():
    txt = input()
    print(matches(txt))
if __name__ == "__main__":
    main()

#ex.3
def find_seq(txt):
    p = re.compile('[a-z]+[_]+')
    return p.findall(txt)
def main():
    txt = input()
    print(find_seq(txt))
if __name__ == "__main__":
    main()

#ex.4
def find_seq(txt):
    p = re.compile('[A-Z]{1}[a-z]+')
    return p.findall(txt)
def main():
    txt = input()
    print(find_seq(txt))
if __name__ == "__main__":
    main()

#ex.5
def matches(txt):
    p = re.compile(r'a+[\w.-]+b+')
    return p.findall(txt)
def main():
    txt = input()
    print(matches(txt))
if __name__ == "__main__":
    main()

#ex.6
def colon(txt):
    p = re.sub(r'[\s,.]', ':', txt)
    return p
def main():
    txt = input()
    print(colon(txt))
if __name__ == "__main__":
    main()

#ex.7
def convert(txt):
    p = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), txt)
    return p
def main():
    txt = input()
    print(convert(txt))
if __name__ == "__main__":
    main()

#ex.8
def split(txt):
    p = re.split(r'(?=[A-Z])', txt)
    return p
def main():
    txt = input()
    print(split(txt))
if __name__ == "__main__":
    main()

#ex.9
def insert(txt):
    p = re.sub(r'([a-z])([A-Z])', r'\1 \2', txt)
    return p
def main():
    txt = input()
    print(insert(txt))
if __name__ == "__main__":
    main()

#ex.10
def convert(txt):
    p = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', txt)
    p = p.lower()
    return p
def main():
    txt = input()
    print(convert(txt))
if __name__ == "__main__":
    main()