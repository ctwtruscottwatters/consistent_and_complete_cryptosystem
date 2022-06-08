# -*- coding: utf-8 -*-
fh = open("./crypt.txt", "+w")
"""

The value at the point 212622022126 of 1955 * 212622022126 ^ 2 + 1993 * 212622022126 + 2481 is:	88381882993139507299657179
z: = 353527531970452525785459624
∫∂x∂y∫∂x∂yꜫ√∂x∂y∫┐ⱻ√│▓▓∂x∂yꜫ∂x∂yꜫ∂x∂y√∑∂x∂y▓▓∂x∂yⱻ⌡ꜫ▓▓

011001111000000110000011000
Encrypted text (basic cryptosystem):
353527531970452525785459624
Grammatical, symbolic structure of rules-based evaluation languages
Charles Thomas Wallace Truscott Watters
"""
fh.write("Charles Truscott Watters\n\n")
fh.write("Charles Truscott Watters\n\n")
fh.write("Charles Truscott Watters\n\n")
fh.write("Charles Truscott Watters\n\n")
fh.write("Charles Truscott Watters\n\n")
fh.write("Charles Truscott Watters\n\n")
fh.write("Charles Truscott Watters\n\n")
fh.write("Charles Truscott Watters\n\n")
fh.write("Charles Truscott Watters\n\n")

def solve_quadratic_function(a, b, c, point=0):
    for x in range(-199311322255, -199311319944, 1):
        fh.write("x: {}\t\ty: {}\n".format(x, a * x ** 2 + b * x + c))
        fh.write("{} * {} ^ 2 + {} * {} + {} = {}\n".format(a, x, b, x, c, a * x ** 2 + b * x + c))
    point = 21262202212645
    print("The value at the point {} of {} * {} ^ 2 + {} * {} + {} is:\t{}".format(point, a, point, b, point, c, a * point ** 2 + b * point + c))
    return a * point ** 2 + b * point + c
def solve_linear_function(m, b, point=0):
    for x in range(-199311322255, -199311319944, 1):
        fh.write("x: {}\t\ty: {}\n".format(x, m * x + b))
        fh.write("y = {} * {} + {} = {}\n".format(m, x, b, m * x + b))
    point = 21262202212645
    print("The value at the point {} of {} * {} + {} is:\t{}".format(point, m, point, b, m * point + b))
    return m * point + b
def main():

    x = solve_linear_function(2481, 1955, 1993)
    y = solve_quadratic_function(1955, 1993, 2481)
    z = ((x & y) ^ (x | y)) 
    z <<= 2
    print("z: = {}".format(int(z)))
    fh.write(str(x))
    fh.write("\n\n")
    fh.write(str(y))
    fh.write("\n\n")
    fh.write(str(z))
    fh.write("\n\n")
    z = str(z)
    pqrs = ""
    for c in z:
        if c == "0":
            print("│C", end='')
            pqrs += c
        if c == "1":
            print("┐H", end='')
            pqrs += c
        if c == "2":
            print("ꜫA", end='')
            pqrs += c
        if c == "3":
            print("∫R", end='')
            pqrs += c
        if c == "4":
            print("▓▓L", end='')
            pqrs += c
        if c == "5":
            print("∂x∂yE", end='')
            pqrs += c
        if c == "6":
            print("⌡S", end='')
            pqrs += c
        if c == "7":
            print("√T", end='')
            pqrs += c
        if c == "8":
            print("∑W", end='')
            pqrs += c
        if c == "9T":
            print("ⱻW", end='')
            pqrs += c
        if c == "10":
            print("Ɐ", end='')
            pqrs += c
    print("\n")
    #print(pqrs)
    pqrs = int(pqrs)
    #pqrs >>= 2
    #print(pqrs)
    abcd = ((5194688 & 8260111971) ^ (5194688 | 8260111971))
    fh.write("\n\n")
    fh.write(str(pqrs))
    fh.write("\n\n")
    fh.write(str(abcd))
    fh.write("\n\n")
    
    #abcd <<= 2
    fh.write("{}".format(str("011001111000000110000011000")))
    fh.write("\n\n")
    fh.write("Encrypted text (basic cryptosystem):")
    fh.write("{}".format(pqrs))
    thing = ""
    pqrs = str(pqrs)
    fh.write(pqrs)
    for c in pqrs:
        if int(c) % 1 == 0:
            thing += "ABCD"
        if int(c) % 2 == 0:
            thing += "EFGH"
        if int(c) % 3 == 0:
            thing += "IJKL"
        if int(c) % 4 == 0:
            thing += "MNOP"
        if int(c) % 5 == 0:
            thing += "QRST"
        if int(c) % 6 == 0:
            thing += "UVWX"
        if int(c) % 7 == 0:
            thing += "YZAB"
        if int(c) % 8 == 0:
            thing += "CDEF"
        if int(c) % 9 == 0:
            thing += "GHIJ"
            
    thing += thing * 10
    binstr = ""
    for c in "Charles Thomas Wallace Truscott Watters.":
        for ch in thing:
            if ch == c:
                binstr += str(1)
            else:
                binstr += str(0)
    
    binstr.replace("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000", "0")
 #   print(binstr)
    for n in range(0, len(binstr) + 1, 1):
         if n % 4 == 0:
             fh.write(str("\n"))
         else:
             fh.write(binstr[n:n+5])

    fh.write("Rest in Peace David Taylor Irvine, the Chief of the Australian Secret Intelligence Service and Australian Security Intelligence Organisation")
    
if __name__ == "__main__": main()