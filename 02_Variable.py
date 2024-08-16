Python 3.12.4 (main, Jun  6 2024, 18:26:44) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 18
>>> x + 15
33
>>> x ** 3
5832
>>> y = 54
>>> x + y
72
>>> g = input("Enter number here: ")
Enter number here: 43
>>> g + 32
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> g = input("Enter number here: ")
Enter number here: 43
>>> g = int(g)
>>> g + 32
75
>>> g = int(input("Enter number here: "))
Enter number here: 43
>>> g + 32
75
>>> int("000001")
1
>>> int("1b")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '1b'
>>> int("1")
1
>>> g = int(input("Enter number here: "))
Enter number here: 2134
>>> g
2134
>>> g = input("Enter number here: ")
Enter number here: 2134
>>> g
'2134'
>>> g = input("Enter number here: ")
Enter number here: 43
>>> g = int(g)
>>> g + 32
75
>>> g ** 3
79507
