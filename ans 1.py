numbers = [ 386, 562, 47, 498, 807, 344, 230, 377, 754, 484, 597, 876, 353, 615, 953, 345, 399,
162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 379, 843, 831,
 445]
new_list = []
for i in range(len(numbers)):
    if (numbers[i]%6==0):
        new_list.append(numbers[i])
print(new_list)
new_list.append(949)
print(new_list)
