'''
Input: list of elements and a block size k or some other
 variable of your choice
Output: return the list of elements with every block of
 k elements reversed, starting from the beginning of the 
 list.
For instance, given the list 12, 24, 32, 44, 55, 66 
and the block size 2, 
the result is 24, 12, 44, 32, 66, 55
'''
elements = raw_input("Elements, space separated: ")
data = map(int, elements.split())
k = input("Block Size: ")
p = list(data[x:x+k] for x in range(0, len(data), k))
l = []
for i in p:
	l += (list(reversed(i)))
print(', '.join(map(str, l)))