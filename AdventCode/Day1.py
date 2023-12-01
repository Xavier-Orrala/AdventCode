def getValue():
    '''
    Will obtain the first and last number of the hidden combination
    and add it to the overall code needed by the Elves
    '''
    combo = open('Day1ElfCode.txt', 'r')
    code = combo.readlines()
    total = 0
    first = ""
    second = ""
    for line in code:
       values = ""
       for num in line:
           if num.isdigit() == True:
                 values = values + num
       if len(values) > 2:
           first,second = values[0], values[-1]
           values = first + second

       if len(values) == 1:
           first,second = values[0], values[0]
           values = first + second
       total += int(values)   
    combo.close()
    return total
elfCode = getValue()
print(elfCode)
