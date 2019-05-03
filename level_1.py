# 평균 구하기

def average(list):
    
    return (sum(list) / len(list))

list = [5,3,4] 
print("average : {}".format(average(list)));


# 두 정수 사이의 합

def adder(a, b):

    if a > b: 
        a, b = b, a

    return sum(range(a, b+1))

print(adder(3, 5))

