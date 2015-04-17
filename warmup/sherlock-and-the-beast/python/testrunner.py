import code
from StringIO import StringIO
import sys

def check_correctness(length, string):
    sys.stdout = sys.__stdout__
    string = string.rstrip('\r\n')

    if len(string) != length and string != "-1":
        sys.stdout.write(
                "ERROR: Length doesn't match. Expected: {} - Result: {}\n"
                .format(
                    length,
                    len(string)
        ))
    elif string == "-1":
            sys.stdout.write("-1: No string for length {}\n".format(length))
    else:
        count5 = 0
        count3 = 0
        for c in string:
            if c == "5":
                count5 += 1
            elif c == "3":
                count3 += 1
            else: 
                sys.stdout.write("ERROR: Unknown character {} for length {}\n"
                    .format(
                        c, length
                ))
                break
        if count5 % 3 != 0:
            sys.stdout.write("ERROR 5 NO MULT OF 3: for length {} - #5: {}\n"
                .format(
                    length, count5
            ))
        if count3 % 5 != 0:
            sys.stdout.write("ERROR 3 NO MULT OF 5: for length {} - #5: {}\n"
                .format(
                    length, count3
            ))


for i in range(1, 100):
    sys.stdout.write("Progress: {}   \r".format(i*100.0/100000))
    sys.stdout.flush()
    sys.stdin = StringIO("1\n{}".format(i))
    #sys.stdout = result = StringIO()
    #sys.stdout = open("f{}".format(i), 'w')
    sys.stdout = tmp = StringIO()
    code.run()
    
    check_correctness(i, tmp.getvalue())

