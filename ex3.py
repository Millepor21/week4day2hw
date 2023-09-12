nums_list = [10,23,45,70,11,15]
target = 70

def num_search(alist,atarget):
    for i, num in enumerate(alist):
        if num == atarget:
            return f'Your number is in position {i + 1}'
    return -1
# If number is not present return -1
num_search(nums_list, target)