x = 1

def nester():
    x=2
    print(x)
    class C:
        x=3
        print(x)
        def method1(self):
            print(x)
            print(self.x)
        def method2(self):
            x=4
            print(x)
            self.x=5
            print(self.x)
    i=C()
    i.method1()
    i.method2()

print(x)
nester()
print('-'*40)
