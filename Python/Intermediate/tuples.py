

# tuples are immutable, but it is like lists,

x = ('2', 46, 62, True)

print(x)

# traceback TypeError: 'tuple' object does not support item assignment
print(x[1])
# x[1] = 47

(x, y, z) = ('hello', 'tuple', 'Im immutable ')

print(x, y, z)

# tuples comparison if different, if one element in the tupes is true it returns rather checking whole thing

print('tuples comparions ', (1, 5, 90) < (9, 2, 0))

tup = tuple()

tup = []


