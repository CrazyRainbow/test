

def quick_sort(array):
    '''
    should kick out the mid, index still start from 0
    '''
    length = len(array)
    left = []
    right = []

    if length < 2:
        return array
    else:
        mid = array.pop(0)

        for i in range(0, length - 1):
            if array[i] < mid:
                left.append(array[i])
            else:
                right.append(array[i])

        return quick_sort(left) + [mid] + quick_sort(right)


if __name__ == "__main__":
    array = [int(x) for x in input("enter numbers separated by whitespace:").split()]
    
    array = quick_sort(array)

    print(array)