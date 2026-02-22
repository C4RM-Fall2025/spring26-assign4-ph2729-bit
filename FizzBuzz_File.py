

def FizzBuzz(start, finish):
    outlist = []
    for i in range(start, finish + 1):
        if i % 3 == 0 and i % 5 == 0:
            v = 'fizzbuzz'
        elif i % 3 == 0:
            v = 'fizz'
        elif i % 5 == 0:
            v = 'buzz'
        else:
            v = i
        outlist.append(v)

    return(outlist)


