# add= lambda a,b:a+b

# #function_name = lambda <parameters> : expression

# print(add(4,5))

def isOdd(num):
    return num % 2 == 1


# map(function,iterable)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# square=[1,4,9,16,25]
square = map(lambda x: x**2, my_list)
print(list(square))

# filter(function_that_returns_true_or_false,iterable)
odd_list = filter(isOdd(), my_list)
print(list(odd_list))


def fibo(n):
    if n <= 1:  # Base Case
        return n
    else:
        return fibo(n-1) + fibo(n-2)  # Recursive Case


for i in range(10):  # 0->6
    print(fibo(i))


# # 0,1,1,2,3,5,8
# # 0,1,1,
# i = 3

# fibo(0) = 0
# fibo(1) = 1
# fibo(2) = fibo(1)+fibo(0) = 1+0 == 1
# fibo(3) = fibo(2)+fibo(1) = 1+1 == 2
# fibo(4) = fibo(3)+fibo(2) = 2+1 == 3
