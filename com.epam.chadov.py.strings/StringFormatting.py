s = 'String'
x= 12.3

print('place my variable here : %s' %(s)) ## place variable 's' to % sign
print('place my variable here : %s' %(x))## place variable 'x' to % sign

print('Floating point number : %1.10f' %(13.145)) #### place number  to % sign and round to 10 signs after dot


print('Convert to string %r' %(123)) ## just convdert to string (it could be s or r functions)

print('First: %s, Second: %s, Third: %s' %('hi!', 'two', 3)) ##multiple format of string

print('First : %s, Second: %s' %(2,3))##multiple format of string


print('First: {x} Second: {y} Third: {x}'.format(x= 'inserted', y = 'two')) ## string formatting


print('One : {x}'.format(x = 'INSERT!')) ## string formatting