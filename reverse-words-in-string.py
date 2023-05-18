"""
Given a string as an input. Reverse all the words in the string and return the new string with the words in reversed order.
Example: "A Wild Bat" ---> reverseString("A Wild Bat") ---> "Bat Wild A"

>>> reverseString("A Big Dog Sat On The Roof")
'Roof The On Sat Dog Big A'
"""

def reverseString(s):
    " ".join(s.strip().split()[::-1])
