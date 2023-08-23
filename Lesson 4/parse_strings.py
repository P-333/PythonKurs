"""
Parse string to get host from data
"""

DATA = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

ATPOS = DATA.find("@")
print(ATPOS)

SPPOS = DATA.find(" ", ATPOS)
print(SPPOS)

HOST = DATA[ATPOS+1:SPPOS]
print(HOST)
