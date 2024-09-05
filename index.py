# maximum profit in trading stock

'''prices = [9, 1, 3, 6, 4, 8, 3, 5, 5] 
min_price=prices[0]
max_profit=0
for i in prices:
    max_profit=max(max_profit,i-min_price)
    min_price=min(min_price,i)
print('maximum profit: ',max_profit)'''

# factorial zeroes trail
'''def factorial(n):
    a=0
    b=5
    while n>=b:
        a+=n//b
        b*=5
    return ('number of zeroes in factoral:',a)
print(factorial(5))
'''

# find missing number in list

num=[0,1,3,5,8]
input_set=set(num)
c=len(input_set)+int(input('how many missiing number you want to find: '))
for i in range (c):
    if i  not in  input_set:
        print(i)

