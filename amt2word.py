words = {1 : "one",
         2 : "two",
         3 : "three",
         4 : "four",
         5 : "five",
         6 : "six",
         7 : "seven",
         8 : "eight",
         9 : "nine",
         10 : "ten",
         11 : "eleven",
         12 : "twelve",
         13 : "thirteen",
         14 : "fourteen",
         15 : "fifteen",
         16 : "sixteen",
         17 : "seventeen",
         18 : "eighteen",
         19 : "nineteen",
         20 : "twenty",
         30 : "thirty",
         40 : "forty",
         50 : "fifty",
         60 : "sixty",
         70 : "seventy",
         80 : "eighty",
         90 : "ninety"
             }

def amt2word(num):
    if type(num) is int:
        print("Number - ", num)
    else:
        raise ValueError(str.format("Value {0} passed is not an integer.  It is {1}", num, type(num)))
    
    numstr = str(num)
    n1 = 0
    n2 = 0
    unit = ""

    if num in words:
        return words[num]
    elif len(numstr) == 2:
        n1 = int( numstr[:1]) * 10
        n2 = int( numstr[1:])
        unit = " "
    elif len(numstr) == 3:
        n1 = int(numstr[:1])
        n2 = int(numstr[1:])
        unit = " hundred "
    elif len(numstr) == 4:
        n1 = int(numstr[:1])
        n2 = int(numstr[1:])
        unit = " thousand "
    elif len(numstr) == 5:
        n1 = int(numstr[:2])
        n2 = int(numstr[2:])
        unit = " thousand "
    elif len(numstr) == 6:
        n1 = int(numstr[:1])
        n2 = int(int(numstr[1:]))
        unit = " lac "
    elif len(numstr) == 7:
        n1 = int(numstr[:2])
        n2 = int(numstr[2:])
        unit = " lac "
    elif len(numstr) == 8:
        n1 = int(numstr[:1])
        n2 = int(numstr[1:])
        unit = " crore "
    elif len(numstr) == 9:
        n1 = int(numstr[:2])
        n2 = int(numstr[2:])
        unit = " crore "
    elif num == 0:
        return ""
    else:
        raise ValueError(str.format("Amount {0} not supported.", num))

    return amt2word(n1) + unit + amt2word(n2)


print amt2word(1234)
