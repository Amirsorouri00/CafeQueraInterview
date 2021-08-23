def calculate(shares):
  finalShare = 0
  maximum = shares[0]
  minimum = shares[0]
  for share in shares:
    if share > maximum:
      if (finalShare < share - maximum):
        minimum = maximum
      maximum = share
      finalShare = maximum - minimum
    elif (share < minimum):
      minimum = share
      maximum = share
      finalShare = 0
      
  print(finalShare)
  return


def start():
    days = int(input())
    sharesPerDay = [int(x) for x in input().split()]
    calculate(sharesPerDay)

start()