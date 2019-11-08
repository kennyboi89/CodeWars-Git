def queue_time(customers, n):
    time = 0
    time2 = 0
    if n == 1:
        for x in customers:
            time += x
    elif n >= len(customers):
        return max(customers)
    elif not customers:
        return False