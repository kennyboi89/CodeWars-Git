def find_outlier(integers):
    oddNumber = 0
    evenNumber = 0
    for index in range(len(integers)):
        if integers[index] % 2 == 0:
            evenNumber += integers.count(integers[index])
            whichEvenNumber = integers[index]
            #print (evenNumber)
        if integers[index] % 2 != 0:
            oddNumber += integers.count(integers[index])
            whichOddNumber = integers[index]
    if evenNumber < oddNumber:
        return whichEvenNumber
    else:
        return whichOddNumber
#def find_outlier(integers):
#    oddNumber = 0
#    evenNumber = 0
#    for index in range(len(integers)):
#        if integers[index] % 2 == 0:
            
#            evenNumber += integers.count(integers[index])
#            whichEvenNumber = integers[index]
#            #print (evenNumber)
#        if integers[index] % 2 != 0:
            
#            oddNumber += integers.count(integers[index])
#            whichOddNumber = integers[index]
#            #print (oddNumber)
#    if evenNumber <= oddNumber:
#        print (whichEvenNumber)
#        return whichEvenNumber
#    else:
#        print (whichOddNumber)
#        return whichOddNumber
        
            
            #whichNumber = integers[index]
            #print (numberCountedAmmount)
            #print (whichNumber)
            #if numberCountedAmmount % 2 != 0:
             #   return whichNumber

find_outlier([160, 3, 1719, 19, 11, 13, -21])