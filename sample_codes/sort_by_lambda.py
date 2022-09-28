def solution(numbers):
    numbers.sort(key=lambda x: (x[1], x[0]))
    print(numbers)
    ## [[1, 0], [7, 0], [1, 1], [2, 2], [3, 2], [2, 3], [0, 4], [5, 6], [7, 7]]
    numbers.sort(key=lambda x: x[0])
    print(numbers)
    ## [[0, 4], [1, 0], [1, 1], [2, 2], [2, 3], [3, 2], [5, 6], [7, 0], [7, 7]]
    return
    

solution([[1, 0], [2, 3], [3, 2], [0, 4], [5, 6], [7, 0], [1, 1], [2, 2], [7, 7]])


### dictionary 정렬하기 ###
# dictionary 정렬시 sorted 안에서 items() 사용하면 쉽게 정렬 가능.

my_dict = {1: 3, 2: 5, 3: 1, 4: 3}
print(my_dict) # {1: 3, 2: 5, 3: 1, 4: 3}

my_dict = sorted(my_dict.items(), key=lambda x: (x[1], x[0]))
print(my_dict) # [(3, 1), (1, 3), (4, 3), (2, 5)]
