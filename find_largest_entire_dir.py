import sys, os, pprint

if sys.platform[:3] == 'win':
    dirname = r'C:\Users\Przemek\AppData\Local\Programs\Python\Python36\Lib'
else:
    dirname = 'usr/lib/python'

allsizes = []
for (thisDir, subsHere, fileHere) in os.walk(dirname):
    for filename in fileHere:
        if filename.endswith('.py'):
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))
allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
