# PATİKA PROJECT
#1
flatten_list = []
def flatten(list1):
    for i in list1:
        if isinstance(i, list):    #checks if the element is in the list
            flatten(i)
        else:    # if the element is not in the list, appends the element into empty list
            flatten_list.append(i)  
input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten(input_list)
print(flatten_list)

#2
def reverse_list(i):
    i = i[::-1]    #reverses elements in the list
    for k in i:
        i = [k[::-1] for k in i]    #reverses elements sublists 
        return i 
list1 =[[1, 2], [3, 4], [5, 6, 7]]
print(reverse_list(list1))
