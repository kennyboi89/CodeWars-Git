def queue_time(customers, n):
    customers2 = customers
    time = 0
    time2 = 0
    if n == 1:
        for x in customers:
            time += x
            return time
    #elif n >= len(customers):
     #   return max(customers)
    #elif not customers:
      #  return 0
    else:
        
        for x in range(len(customers)):
            
            
            print (numbers)
            #queueTime += time
            customers = customers[ : 0 ] + customers[0+1 : ]
            #print (queueTime)
            
        return 0#sum = max(customers)
        


cust = [3],[3],[2],[2],[2],[2]
queue_time(cust, 5)