def binary_search(list_,target,low,high):
    if low <= high:
        mid = (low+high)//2
    
        if target == list_[mid]:
            return mid
        elif target > list_[mid]:
            return binary_search(list_,target,mid+1,high)
        elif target < list_[mid]:
            return binary_search(list_,target,low,mid-1)
    else:
        return -1
    

list_ = [22,45,32,65,87,98,90,62,11,58]
target = 45
list_.sort()
print(binary_search(list_,target,0,len(list_)-1))