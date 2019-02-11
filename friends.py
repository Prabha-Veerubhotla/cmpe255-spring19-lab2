def mean_num_friends(x):
    totalsum = 0
    num_of_friends = len(x)
    for elem in x:
        totalsum = totalsum + elem
    mean = totalsum / num_of_friends
    return mean
    # TODO

def median_num_friends(x):
    x.sort()
    count = len(x)  
    if count%2 == 0:
        median = (x[count// 2] + x[(count//2) +1])/2
    else:
        median = x[count//2]
    return median
    # TODO



num_friends = [100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print("mean={}".format(mean_num_friends(num_friends)))
print("median={}".format(median_num_friends(num_friends)))


