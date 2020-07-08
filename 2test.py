input1 = 2016
output1 = 2044

input2 = 2000
output2 = 2028

input3 = 50501
output3 = 50507

# input3 = 2000
# output3 = 2028

inputs = [input1,input2,input3]
outputs = [output1, output2, output3]

# val = 2045
val = 999999

def iskabise(i):
    if True == (i % 400 == 0 or i%4 == 0 and i%100!=0):
        return True
    return False

def calculate(input):
    temp = input
    mod = temp%7
    mod2 = mod
    # print(mod)

    for i in range(temp+1, val):
        if True == iskabise(i):
            # kabise
            mod2 = (mod2 + 2)%7
            # print("ddd:",mod2)
        else:
            mod2 = (mod2 + 1)%7
            # print("iii: ", mod2)
        if mod2 == mod and iskabise(i) == iskabise(input):
            return i


def test():
    for k in range(0, len(inputs)):
        k+=1
        i = inputs.pop(0)
        o = outputs.pop(0)
        print("input, valid_output, inputs, outputs:", i, o, inputs, outputs)
        o2 = calculate(i)
        if o != o2:
            print("wrong doing in calculation:", i, o, o2)
    print("all is well")        

test()