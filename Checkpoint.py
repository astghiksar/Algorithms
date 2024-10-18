def merge_sort(array):
    if len(array) > 1:
        # find the middle of the array
        middle = len(array) // 2

        # divide the array
        left = array[:middle]
        right = array[middle:]

        # sort both halves
        merge_sort(left)
        merge_sort(right)

        # i(left) j(right) k(merged)
        i = j = k = 0

        #merge the halves
        while i < len(left) and j<len(right):
            if left[i] < right[i]:
                array[k] = left[i]
                i+=1
            else:
                array[k] = right[j]
                j+=1
            k+=1

        # add the remaining elements of the right half
        while j < len(right):
            array[k] = right[j]
            j+=1
            k+=1

        # add the remaining elements of the left half
        while i < len(left):
            array[k] = left[i]
            i+=1
            k+=1

array = [ 120, 2, 23, 54, 68]
merge_sort(array)
print("The sorted array is:", array)