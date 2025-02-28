#binary search works with an already sorted list to find a specific value

#takes to parameters, the list itself and the item that user is looking for
def binary_search(list, item):
    beginIndex = 0 #starting of list
    endIndex = len(list) - 1 #ending of list, -1 because python starts it from 0

    #while loop to keep searching till list ends
    while beginIndex <= endIndex:
        midpoint = beginIndex + (endIndex - beginIndex) // 2 #to find midpoint, need to add beginIndex to get the midpoint rather than distance of begin to mid
        midpointValue = list[midpoint] #index list with value of midpoint, returns value rather than position of midpoint

        #need 3 conditions. 1. if midpoint itself is the item, 
        if item == midpointValue:
            return midpoint
        
        #2. if item is less than the midpoint, move left of midpoint
        elif item < midpointValue:
            endIndex = midpoint - 1

        #3. if item is bigger than the midpoint, move right of midpoint
        else:
            beginIndex = midpoint + 1

    return None #if item does not exist in list


list1 = [30, 31, 41, 43, 49, 52, 59, 91]
item1 = 43
print(binary_search(list1, item1))