import os
#ex.1
path = r'C:\Users\Salima\Desktop\python'
print("Only directories:")
print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
print("Only files:")
print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))])
print("All directories and files:")
print([name for name in os.listdir(path)])

#ex.2
path = r'C:\Users\Salima\Desktop\python\lab5\regex.py'
print("Existence: ", os.access(path, os.F_OK))
print("Readability: ", os.access(path, os.R_OK))
print("Writability: ", os.access(path, os.W_OK))
print("Executability: ", os.access(path, os.X_OK))

#ex.3
path = r'C:\Users\Salima\Desktop\python\lab5\regex.py'
if os.path.exists(path):
    print("Yes, it does exist")
    print("Filename: ", os.path.basename(path))
    print("Directory: ", os.path.dirname(path))
else:
    print("No, it does not exist")

#ex.4
def counter(file):
    with open(file) as f:
        for i, n in enumerate(f):
            pass
        return i + 1
def main():
    file =  r'C:\Users\Salima\Desktop\python\lab5\regex.py'
    print("Total number of lines: ", counter(file))
if __name__ == "__main__":
    main()

#ex.5
animals = ['fox', 'bunny', 'bear', 'cat', 'penguin']
with open('file.txt', 'w') as file:
    for i in animals:
        file.write("%s\n" %i)
list = open('file.txt')
print(list.read())

#ex.6
import string
if not os.path.exists("alphabet"):
    os.makedirs("alphabet")
for i in string.ascii_uppercase:
    path = os.path.join("alphabet", i + ".txt")
    with open(path, "w") as f:
        f.writelines(i)
    with open(path, "r") as f:
        txt = f.read()
        print(txt)

#ex.7
with open('file.txt', 'r') as a:
    with open('abc.txt', 'w') as b:
        b.write(a.read())
txt = open('abc.txt')
print(txt.read())

#ex.8
path = r'C:\Users\Salima\Desktop\abc.txt'
if os.path.exists('abc.txt'):
    os.remove('abc.txt')
else:
    print("The file does not exist")