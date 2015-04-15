import code
from StringIO import StringIO
import sys

for i in range(1, 10):
    sys.stdin = StringIO("1\n{}".format(i))
    #sys.stdout = result = StringIO()
    #sys.stdout = open("f{}".format(i), 'w')
    sys.stdout = tmp = StringIO()
    code.run()
    
    check_correctness(i, tmp.getvalue())

def check_correctness(length, string):
    sys.stdout = sys.__stdout__
    if len(string) != length:
        sys.stdout.write(
                "ERROR: Length doesn't match. Expected: {} - Result: {}".format(
                    length,
                    len(string)
        ))
    else:
        count5 = 0
        count3 = 0
        for c in string:
            if c == "5":
                count5 += 1
            elif c == "3":
                count3 += 1
            else: 
                sys.stdout.write("ERROR: Unknown character {} for length {}".format(
                    c, i
                ))
                break

