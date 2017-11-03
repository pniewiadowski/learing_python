import os, glob

dirname = r'C:\Users\Przemek\AppData\Local\Programs\Python\Python36\Lib'

allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filsize = os.path.getsize(filename)
    allsizes.append((filsize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])
