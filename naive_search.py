def naive_search(list_,target):
    for i in range(len(list_)-1):
        if list_[i] == target:
            return i
        
    return -1
        


list_ = [22,45,32,65,87,98,90,62,11,58]
target = 45
list_.sort()
print(naive_search(list_,target))