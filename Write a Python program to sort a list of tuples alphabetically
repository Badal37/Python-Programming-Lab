def SortTuple(tup):
    n = len(tup)
     
    for i in range(n):
        for j in range(n-i-1):
             
            if tup[j][0] > tup[j + 1][0]:
                tup[j], tup[j + 1] = tup[j + 1], tup[j]
    return tup
 
tup = [("Amaruta", 20), ("Zoe", 32), ("Akshay", 25),
        ("Nilesh", 21), ("C", "D"), ("Penny", 22)]
print(SortTuple(tup))
