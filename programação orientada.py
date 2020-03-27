class Dog(object):
    def __init__(self, breed):
        self.breed = breed

sam= Dog(breed='lab')
frank= Dog(breed='huskie')

print(sam.breed)
print(frank.breed)
