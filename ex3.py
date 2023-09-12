nums_list = [10,23,45,70,11,15]
target = 70
#O(N) + O(4*1) => O(N)
def num_search(alist,atarget): #O(1)
    for i, num in enumerate(alist): #O(N)
        if num == atarget: #O(1)
            return f'Your number is in position {i + 1}' #O(1)
    return -1 #O(1)
# If number is not present return -1
num_search(nums_list, target)