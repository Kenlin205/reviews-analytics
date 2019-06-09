data = []
count = 0
with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count +=1 
		if count % 10000 == 0:
			print(len(data))
print("all data have readed, There were ",len(data), "data")
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print("Every message have average",sum_len/len(data),"length")


