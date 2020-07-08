val = 999999

def iskabise(i):
    if True == (i % 400 == 0 or i%4 == 0 and i%100!=0):
        return True
    return False

def calculate(input):
    temp = input
    mod = temp%7
    mod2 = mod

    for i in range(temp+1, val):
        if True == iskabise(i):
            # kabise
            mod2 = (mod2 + 2)%7
        else:
            mod2 = (mod2 + 1)%7
        if mod2 == mod and iskabise(i) == iskabise(input):
            return i


def start():
    i = input()
    print(calculate(int(i)))


start()