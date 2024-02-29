# """
# Python Data Types:
#         str , int , float , bool , complex ,list , tuple , set , dict  , bytes , ...
# """

# s = 'amin'
# print(type(s))      # str


# print('--------------------------------')


# i = 2
# print(type(i))      # int


# print('--------------------------------')


# f = 2.5
# print(type(f))      # float


# print('--------------------------------')


# c = 2 + 3j          # 2 is the real part and 3 is imaginary
# print(type(c))      # complex


# print('--------------------------------')


# b = True
# print(type(b))      # bool

# print(bool(5))      # True
# print(bool(-2))     # True
# print(bool('ali'))  # True

# print(bool(0))      # False
# print(bool(''))     # False


# print('--------------------------------')


# print(bool([]))     # False (empty list)
# print(bool({}))     # False (empty dictionary)
# print(bool(()))     # False (empty tuple)


# print('--------------------------------')


# print('--variable names---')
# """
#     All identifiers must start with a letter or underscore (_), 
#     you can't use digits.
#     Identifiers can contain letters, digits and underscores (_). 
#     Identifiers can't be a keyword. 
#     They can be of any length.
#  """

# print('a2'.isidentifier())      # True
# print('2a'.isidentifier())      # False
# print('_myvar'.isidentifier())  # True
# print('my_var'.isidentifier())  # True
# print('my-var'.isidentifier())  # False
# print('my var'.isidentifier())  # False
# print('my$'.isidentifier())     # False
# print('my#'.isidentifier())     # False


# print('--------------------------------')


# # You cannot use reserved words as variable names

# """
# False 	class 	return	is 		finally 
# None 	if		for 	lambda 	continue 
# True 	def 	from 	while	nonlocal
# and 	del 	global 	not 	with
# as  	elif 	try		or 		yield
# assert 	else 	import 	pass
# break 	except 	in 		raise
# """
# from keyword import iskeyword
# print( iskeyword('if'))   # True

# print('--------------------------------')


# print('---Python Casting---')

# i = 5
# print(float(i))     # 5.0


# print('--------------------------------')


# s ='12'
# print(int(s) + 1)   # 13

