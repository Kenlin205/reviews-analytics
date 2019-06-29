data = []
count = 0
with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        count +=1 
        if count % 10000 == 0:
            print(len(data))
print("all data have readed, There were ",len(data), "datas")

# um_len = 0
# for d in data:
# 	sum_len = sum_len + len(d)
# print("Every message have average",sum_len/len(data),"length")


# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print("There were ",len(new), "data less than 100")
# print("-------------------------below are message")
# print(new[0])
# print(new[1])

# good = []
# for d in data:
# 	if "good" in d:
# 		good.append(d)
# print("There are",len(good), "good message")
# print("-------------------------below are good message")
# print(good[0])

#print(data[0])

# counting word


wc = {} #word count
count = 0
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # adding new key to dictionary
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
print(len(wc))
print(wc["Ken"])
while True:
    word = input ("What word would you want to check? ")
    if word == "q":
        break
    if word in wc:
        print(word, "Appear times: ", wc[word])
    else:
        print("The word have not appeared before yet! ")
print("Thanks your support this soft")



