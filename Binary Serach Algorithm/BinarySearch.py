# a function that takes a list and a target parameter
# multiple variables: middle, start,end,steps
# recursion or while loop
# increase the steps each time a split is done
# conditions to track target position

def binary_search(list,element):
    mid=0
    start=0
    end=len(list)
    steps=0

    while(start<=end):
        print("Steps",steps, ":" ,str(list[start:end+1]))

        steps+=1
        mid=(start+end)//2
        if element == list[mid]:
            return mid
        if element< list[mid]:
            end = mid-1
        else:
            start=  mid+1
    return -1

my_list=  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,22]
target = 11
binary_search(my_list,target)
