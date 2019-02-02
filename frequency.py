name = input("Enter file:")
handle = open(name)
dict = {}
for line in handle:
    for word in line:
        if word not in dict:
            dict[word]=0
        dict[word]+=1
print(dict)
dictr = [(v, k) for (k, v) in dict.items()]
print(dictr)
