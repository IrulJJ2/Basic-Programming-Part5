def pow(x, n):
    result = 1
    if x == 0 :
        return 0
    if n > 0 :
        for i in range (1, (n//2)+1) :
            result = result * x
        result = result * result
        if n % 2 != 0 :
            result = result * x
    elif n < 0:
        for i in range (1, ((-n//2)+1)):
            result = result * 1/x
        result = result * result
        if n%2 !=0:
            result = result *1/x
    else:
        pass
    return result

if __name__ == '__main__':
    print(pow(2, 3)) # 8
    print(pow(7, 2)) # 49
    print(pow(10, 5)) # 100000
    print(pow(17, 6)) # 24137569
    print(pow(5, 3)) # 125