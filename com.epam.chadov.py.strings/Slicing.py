s = 'Hello world'  ##slice notation
print(s[:4]) ## up to 4 index but not including it

print(s[:])  ##grab all string


print(s[-1]) ## loops back around and grabs last letter - 'd'

print(s[:-1]) ## loops back around and grabs whole string without the last letter - 'd'

print(s[::2]) ## grabs and prints any every element from string with two steps by letters

print(s[::3]) ## every 3d element from first

print(s[::-1]) ## reverse string by every element from the end of the string


## String properties

'immutability'

##s[0] = 'x' ## strings are immutable and here is an error

s = s + ' concatinate me!' ## but we can concatinate strings

print(s)


z = 'z'
print (z*10) ## multiple of string

print(s.upper().split('E'))## String to upper case and split by 'E'

