#import numpy

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def bubble_sort(array, cnt):
    for i in range(0, cnt - 1):
        for j in range(0, cnt - 1 - i):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)

if __name__ == "__main__":

    num = int(input().strip())
    print("%d numbers will be input and sorted:" % num)
    
    use list:

    array = []
    for n in range(num):
        array.append(int(input().strip()))

    input("start sorted:").strip()

    bubble_sort(array, num)

    for n in range(num):
        print(array[n])
