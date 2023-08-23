"""
Syntax error
"""
s = input('Ge två tal, x och y:')

# pylint: disable=undefined-variable
s = q.split() # Felet ligger här, ska inte vara "q" utan "s"

x = int(s[0])

y = int(s[1])

print('x/(x-y)=', x/(x-y))
