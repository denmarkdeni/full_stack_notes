def armstrong(num):  # 134 
    temp = num
    digit_count = 0
    while num > 0 :
        num = num // 10  # 134 -> 13 -> 1 -> 0
        digit_count = digit_count + 1
    num = temp
    sum = 0
    while num > 0 :
        digit = num % 10  # 134 % 10 
        value = digit ** digit_count
        print("loop value" , value)
        sum = sum + value
        num = num // 10
    print("digit" , digit_count)
    print("sum" , sum)
    if temp == sum :
        print("this is armstrong")
    else: 
        print("not an armstrong")

armstrong(153)

def odd_even(num):
    if num % 2 == 0 :
        print("even")
    else:
        print("odd")
odd_even(21)    

