
def functhree():
    print("Three")

def functwo():
    functhree()
    print("Two")

def funcone():
    functwo()
    print("One")


funcone()