def start():
	size = [int(x) for x in input().split()]
	set_one = {int(x) for x in input().split()}
	set_two = {int(x) for x in input().split()}
	res = list(set_one & set_two)
	res.sort()
	if len(res) != 0:
		print(len(res))
		print(*res, sep = " ")
	else:
		print("0\n")
    
start()