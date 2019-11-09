def find_it(seq):
    for index in range(len(seq)):
        if seq.count(seq[index]) > 0:
            numberCountedAmmount = seq.count(seq[index])
            whichNumber = seq[index]
            if numberCountedAmmount % 2 != 0:
                return whichNumber




#numbers = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
#for index in range(len(numbers)):
#   #print ('Current number :', numbers[index])
#   #print (numbers.count(numbers[index]))
#   #print (numbers[index]+"\n")
#   if numbers.count(numbers[index]) > 0:
#   #ny forløkke for å legge til like tall
#       numberCountedAmmount = numbers.count(numbers[index])
#       whichNumber = numbers[index]
#       if numberCountedAmmount % 2 != 0:
#           #print (numberCountedAmmount)
#           print (whichNumber) 

#           #for sameNumber in numbers[index]:
#               #oddnumberoftimes = 0
#               #numbers[0].count() = oddnumberoftimes
#               #if numbers.count(numbers[index]) == len(numbers):
#                   #print (numbers[index])


   

