words = ["hello","python","welcome","Garv","Prajapat"]

max_index = 0

for i in range(len(words)):
    if len(words[i]) >= len(words[max_index]):
        max_index = i

print(f"longest world in list is : {words[max_index]}")

