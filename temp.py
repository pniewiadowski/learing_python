import timeit
print(min(timeit.repeat(number=10000, repeat=3, stmt="l=[1,2,3,4,5]\nfor i in range(len(l)): l[i] +=1")))
print(min(timeit.repeat(number=10000, repeat=3, stmt="l=[1,2,3,4,5]\ni=0\nwhile i < len(l):\n\tl[i] += 1\n\ti += 1")))
print(min(timeit.repeat(number=10000, repeat=3, stmt="l=[1,2,3,4,5]\nm=[x+1 for x in l]")))
