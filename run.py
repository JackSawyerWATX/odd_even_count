def solution(nums):
    # TODO: implement the function to return a tuple (even_count, odd_count)
    even_count = 0
    odd_count = 0
    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)
    
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))