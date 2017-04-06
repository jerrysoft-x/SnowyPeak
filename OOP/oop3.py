class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')

    def eat(self):
        print('Eating meat...')


def run_twice(x):
    x.run()
    x.run()



dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()
cat.eat()

print(isinstance(dog, Dog))
print(isinstance(dog, Cat))
print(isinstance(dog, Animal))

run_twice(dog)
run_twice(cat)
run_twice(Animal())
