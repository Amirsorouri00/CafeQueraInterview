# def difference(first, second):
#     if first-second >=2:
#         return True
#     return False

# def countIterations(boxes, boxNum):
#     iterations = 0
#     for i, j in zip(range(boxNum), reversed(range(boxNum))):
#         # print(i, j)
#         if difference(boxes[i], boxes[j]):
#             iters = (boxes[i]-boxes[j])//2
#             boxes[i]-=iters
#             boxes[j]+=iters
#             iterations+=iters*2
#     return iterations


boxNum = int(input())
boxes = [int(x) for x in input().split()]
mx = max(boxes)
mn = min(boxes)
diff = 0
cnt = 0
for i in range(boxNum-1):
    if abs(boxes[i]-boxes[i+1]) > 0:
        diff+= abs(boxes[i]-boxes[i+1])
        cnt+=1
    
const = mx - diff//cnt
carry = 0
iterations = 0
for i in range(boxNum):
    boxes[i]+=carry
    carry=0
    if boxes[i] > const:
        carry = boxes[i] - const
        iterations+=carry
        boxes[i] = const
    elif boxes[i] < const:
        carry = boxes[i] - const
        iterations+=carry
        boxes[i] = const
    else:
        continue

if carry == 0:
    print(abs(iterations))
else:
    print(-1)