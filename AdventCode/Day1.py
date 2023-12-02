def getValue():
    '''
    Will obtain the first and last number of the hidden combination
    and add it to the overall code needed by the Elves
    '''
    key = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    combo = open('Day1ElfCode.txt', 'r')
    code = combo.readlines()
    total = 0
    first = ""
    second = ""
    for line in code:
       values = ""
       test = ""
       x = -1
       for num in line:
           x += 1
           if num.isdigit() == True:
                 values = values + num
                 #print("h",num)
                 # For loop, goes through key array, checks if there are keywords in the num array
           else:
               for i in range(0,len(key)):
                   length = int(len(key[i]))
                   if(line[x:length+x] == key[i]):
                       values = values + str(i)
                       #print("x",num)
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