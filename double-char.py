"""
8 kyu - Double Char

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
"""
def double_char(s):
    res = ""
    k = 0
    while k < len(s):
        res += 2 * s[k]
        k += 1
    return res
