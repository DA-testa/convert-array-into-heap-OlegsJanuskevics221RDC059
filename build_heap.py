# python3
from math import floor

def build_heap(data):
    count=0
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    size = n-1
    for i in range (floor(n/2), -1, -1):
        swaps = sift_down(i, size, data, swaps, count)
    return swaps, count

def sift_down(i, size, data, swaps):
    minIndex = i
    l = LeftChild(i+1)
    if l <= size and data[l] < data[minIndex]:
        minIndex = l
    r = RightChild(i+1)
    if r <= size and data[r] < data[minIndex]:
        minIndex = r
    if i != minIndex:
        data[i], data[minIndex] = data[minIndex], data[i]
        count = count+1
        swaps.append((i,minIndex))
        swaps, count, data = sift_down(minIndex, size,data, swaps, count)
    return swaps, count, data

def LeftChild(i):
    return 2*i-1

def RightChild(i):
    return 2*i


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
