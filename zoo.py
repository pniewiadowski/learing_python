class Animal:
    def reply(self):
        self.speak()

    def speak(self):
        print('spma')


class Mammal(Animal):
    def speak(self):
        print('huh?')


class Cat(Mammal):
    def speak(self):
        print('meow')


class Dog(Mammal):
    def speak(self):
        print('bark')


class Priamte(Mammal):
    def speak(self):
        print('Hello world!')


class Hacker(Priamte):
    pass
