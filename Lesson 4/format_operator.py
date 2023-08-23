"""
Format operator %
"""
CAMELS = 42
# pylint: disable=consider-using-f-string
print("I have spotted %d camels." % CAMELS)

# Other format operators
print("In %d years I have spotted %g %s." % (3, 0.1, "camels"))

# COULD ALSO BE USED USING F STRING
print(f"I have spotted {CAMELS} camels.")

NAME = 'giacomo'
NUMBER = 4.3
print('%s %s %d %f %g' % (NAME, NUMBER, NUMBER, NUMBER, NUMBER))

# As you can see %d will trunicate to integer, %s will maintain formatting,
# %f will print as float and %g is used for generic number
