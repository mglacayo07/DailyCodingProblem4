# Daily Coding Problem: Problem #4 [Hard]

# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.


def first_positive(list):

    list.sort()
    indx = list[0]
    for i in range(1, len(list)):
        if indx > 0 & indx < list[i]:
            if (list[i]-1) != indx and list[i] != indx:
                return (list[i]-1)
        indx = list[i]
    return (indx+1)

if __name__ == '__main__':

    integers = [3, 4, -1, 1,1]
    print("List: ",integers)
    print("Value:",first_positive(integers))

    integers = [1, 2, 0, -1]
    print("List: ", integers)
    print("Value:",first_positive(integers))


