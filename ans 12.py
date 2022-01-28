import re

word=input("Please provide a word ")
word = word.upper()

def check_freq(x):
    freq = {}
    for c in set(x):
       freq[c] = len(re.findall(re.compile(c,re.IGNORECASE),x))
    return freq
dict=check_freq(word)
#print(dict)

sort_orders = sorted(dict.items(), key=lambda x: x[1], reverse=True)
#print(sort_orders)
if sort_orders[0][1]==sort_orders[1][1]:
    print ("?")
elif sort_orders[0][1]>sort_orders[1][1]:
    print(sort_orders[0][0])

# for i in sort_orders:
# 	print(i[0], i[1])
# print(dict.values())
# sorted_list=dict.values()
# #for i in range(len(dict)+1):
#     #sorted_list=sorted_list.append(dict[i][i])
# print(sorted_list)
# final_list=sorted_list.sort(reverse=True)
# print(final_list)


# # string = "hello"
# # abc = string.split()
# # print(abc)