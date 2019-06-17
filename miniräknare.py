import math

def addition(x, y):
    print(x+y)
def subtraktion(x, y):
    print(x-y)
def multiplikation(x, y):
    print(x*y)
def division(x, y):
    print(x/y)

def addition3(x, y, a):
    print(x+y+a)
def subtraktion3(x, y, a):
    print(x-y-a)
def multiplikation3(x, y, a):
    print(x*y*a)
def division3(x, y, a):
    print(x/y/a)

def upphöjt(x, y):




    print(x**y)
def roten(z):
    print(math.sqrt(z))


while True:
    print("Välj vad du vill göra")
    print("1. addition")
    print("2. subtrakrion")
    print("3. multiplikation")
    print("4. division")
    print("5. upphöjt")
    print("6. roten ur")
    val = input("Skriv in val, 1,2,3,4,5 eller 6 ")

    if val == "6":
        z = int(input("skriv talet "))
        if z < 0:
            print("Skriv in ett positivt tal!")
        else:
            roten(z)
            
    else:
        x = int(input("Skriv tal 1 "))
        y = int(input("Skriv tal 2 "))
        tredje_tal = input("Vill du ha ett till tal? ")
        if tredje_tal == "ja" or tredje_tal == "Ja":
            a = int(input("Skriv tal 3 "))
            if val == "1":
                addition3(x, y, a)
            elif val == "2":
                subtraktion3(x, y, a)
            elif val == "3":
                multiplikation3(x, y, a)
            elif val == "4":
                if y or a == 0:
                    print("Man kan inte dividera med noll")
                else:
                    division3(x, y, a)
            elif val > "4":
                print("Man kan inte använda 3 tal i upphöjt med!")

        else:
            if val == "1":
                addition(x, y)
            elif val == "2":
                subtraktion(x, y)
            elif val == "3":
                multiplikation(x, y)
            elif val == "4":
                if y == 0:
                    print("Man kan inte dividera med noll")
                else:
                    division(x, y)
            elif val == "5":
                upphöjt(x, y)


        print("----------------------------------")



