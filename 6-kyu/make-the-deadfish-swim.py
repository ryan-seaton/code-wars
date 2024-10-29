"""
URL: https://www.codewars.com/kata/51e0007c1f9378fa810002a9/python

Create a parser to interpret and execute the Deadfish language.

Deadfish operates on a single value in memory, which is initially set to 0.

It uses four single-character commands:

i: Increment the value
d: Decrement the value
s: Square the value
o: Output the value to a result array
All other instructions are no-ops and have no effect.
"""

def parse(data: str) -> list[int]:
    """
    Parses input string and outputs array of ints according to Deadfish language.
    """
    val = 0
    res: list[int] = []
    for i in data:
        if i == 'i':
            val += 1
        elif i == 'd':
            val -= 1
        elif i == 's':
            val *= val
        elif i == 'o':
           res.append(val)
    return res