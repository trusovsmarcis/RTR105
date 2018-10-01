Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> a = 20
>>> var()

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    var()
NameError: name 'var' is not defined
>>> var ()

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    var ()
NameError: name 'var' is not defined
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 20, '__package__': None}
>>> __bu

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    __bu
NameError: name '__bu' is not defined
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> print(__builtins__.__doc__)
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> a = 10
>>> a * a
100
>>> b = 1.89
>>> vars()
{'a': 10, 'b': 1.89, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> b * b
3.5721
>>> c = "P"
>>> vars()
{'a': 10, 'c': 'P', 'b': 1.89, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(a)
<type 'int'>
>>> 
