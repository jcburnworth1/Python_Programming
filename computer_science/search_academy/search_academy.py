## Search Academy - CodeAcademy
def sparse_search(data, search_val):
    ## Print the data and what we are looking for
    print("Data: " + str(data))
    print("Search Value: " + str(search_val))

    ## Capture first and last value of input list
    first = 0
    last = len(data) - 1

    ## While loop for iteration over the input list
    while first <= last:
        ## Determine the middle value
        mid = (first + last) // 2

        ## Logic to move left or right based on remaining values
        if not data[mid]:
            left = mid - 1
            right = mid + 1

            while True:
                if left < first and right > last:
                    print("{0} is not in the dataset".format(search_val))
                    return
                elif right <= last and data[right]:
                    mid = right
                    break
                elif left >= first and data[left]:
                    mid = left
                    break

                right += 1
                left -= 1

        ## Determine if we found our value and continued or continue the loop
        if data[mid] == search_val:
            print("{0} found at position {1}".format(search_val, mid))
            return
        elif search_val < data[mid]:
            last = mid - 1
        elif search_val > data[mid]:
            first = mid + 1

    print("{0} is not in the dataset".format(search_val))


#from script import sparse_search

data_one = ["Arthur", "", "", "", "", "",
            "Elise", "", "", "", "Gary",
            "", "Mimi", "", "", "", "Zachary"]
search_one = "Zachary"
print("Calling sparse_search.....")
ret = sparse_search(data_one, search_one)
print("Return Value: " + str(ret))

data_two = ["1", "", "", "2", "", "", "3", "", "5", "", "", "", "9", "12"]
search_two = "2"
print("\n\nCalling sparse_search.....")
ret = sparse_search(data_two, search_two)
print("Return Value: " + str(ret))