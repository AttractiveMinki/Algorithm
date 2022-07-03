def solution(numbers):
    numbers.sort(key=lambda x: (x[1], x[0]))
    print(numbers)
    ## [[1, 0], [7, 0], [1, 1], [2, 2], [3, 2], [2, 3], [0, 4], [5, 6], [7, 7]]
    numbers.sort(key=lambda x: x[0])
    print(numbers)
    ## [[0, 4], [1, 0], [1, 1], [2, 2], [2, 3], [3, 2], [5, 6], [7, 0], [7, 7]]
    return
    

solution([[1, 0], [2, 3], [3, 2], [0, 4], [5, 6], [7, 0], [1, 1], [2, 2], [7, 7]])
