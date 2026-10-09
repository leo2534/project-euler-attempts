greatest = 0
greatestx = 0
greatesty = 0
for x in range(100,1000):
    for y in range(100,1000):
        number = x*y
        strNumber = str(number)
        reverseStrNumber = ""
        for i in range(len(strNumber)-1,-1,-1):
            reverseStrNumber += strNumber[i]

        if reverseStrNumber == strNumber:
            if number > greatest:
                greatest = number
                greatestx = x
                greatesty = y
print(greatest)
print(greatestx)
print(greatesty)
