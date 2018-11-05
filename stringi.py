Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> name = input('Enter')
EnterChuck
>>> print(name)
Chuck
>>> letter = fruit[1]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    letter = fruit[1]
NameError: name 'fruit' is not defined
>>> letter = name[1]
>>> print(letter)
h
>>> x = 3
>>> w = Chuck[x - 1]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    w = Chuck[x - 1]
NameError: name 'Chuck' is not defined
>>> w = name[x - 1]
>>> print(w)
u
>>> print(len(name))
5
>>> y = len(name)
>>> print(y)
5
>>> index = 0
>>> while index < len(name):
	z = name[index]
	print(index, letter)
	print(index, z)
	index = index + 1

	
0 h
0 C
1 h
1 h
2 h
2 u
3 h
3 c
4 h
4 k
>>> for z in name:
	print(letter)

	
h
h
h
h
h
>>> for z in name:
	print(z)

	
C
h
u
c
k
>>> word = 'Chuck'
>>> count = 0
>>> for letter in word:
	if letter == 'c':
		count = count + 1
		print(count)

		
1
>>> for letter in 'banana'
SyntaxError: invalid syntax
>>> for letter in 'banana':
	print(letter)

	
b
a
n
a
n
a
>>> s = 'Monty Python'
>>> print(s[0:4])
Mont
>>> print(s[6:7])
P
>>> print(s[6:20])
Python
>>> print(s[:2])
Mo
>>> print(s[8:])
thon
>>> print(s[:])
Monty Python
>>> a = 'Hello'
>>> b = a + 'There'
>>> print(b)
HelloThere
>>> c = a +''+ 'There'
print(c)
SyntaxError: multiple statements found while compiling a single statement
>>> c = a +''+ 'There'
>>> print(c)
HelloThere
>>> c - a +' '+ 'There'
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    c - a +' '+ 'There'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> c = a +' '+ 'There'
>>> print(c)
Hello There
>>> fruit = 'banana'
>>> 'n' in fruit
True
>>> 'm' in fruit
False
>>> 'nan''in fruit
SyntaxError: EOL while scanning string literal
>>> 'nan' in fruit
True
>>> if 'a' in fruit:
	print('Found it!')

	
Found it!
>>> if word =='banana':
	print('All right, bananas,')

	
>>> if word < 'banana':
	print('Your word,''+ word + ',comes before banana.')
	      
SyntaxError: invalid syntax
>>> if word < 'banana':
	print('Your word,''+ word + ', comes before banana.')
	      
SyntaxError: invalid syntax
>>> if word < 'banana':
	print('Your word,'+ word + ', comes before banana.')

	      
Your word,Chuck, comes before banana.
>>> greet = 'Hello Bob'
	      
>>> zap = greet.lower()
	      
>>> print(zap)
	      
hello bob
>>> print(greet)
	      
Hello Bob
>>> print('Hi There'.lower())
	      
hi there
>>> 
