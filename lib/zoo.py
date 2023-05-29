from lib.animal import Animal

class Zoo:

    all = []

    def __init__(self, name, location):
        self.name = name
        self.location = location
        type(self).add_to_all_zoos(self)
    
    # Class methods

    @classmethod
    def add_to_all_zoos(cls, new_zoo):
        if isinstance(new_zoo, cls):
            cls.all.append(new_zoo)
        else: 
            raise TypeError("New zoo must be an instance of Zoo!")
    
    @classmethod
    def find_by_location(cls, location):
        results = [zoo for zoo in Zoo.all 
                    if zoo.location.lower() == location.lower()]
        if results: return results
        return "No zoos at that location!"
    
    # Instance methods

    def animals(self):
        results = [animal for animal in Animal.all if animal.zoo == self]
        if results: return results
        return "No animals at that zoo yet!"
    
    def animal_species(self):
        if type(self.animals()) != str: 
            return {animal._species for animal in self.animals()}
        return "No animal species at that zoo yet!"
    
    def animal_nicknames(self):
        if type(self.animals()) != str:
            return {animal._nickname for animal in self.animals()}
        return "No animals to nickname at that zoo yet!"

    # Properties
    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, name):
        if type(name) == str:
            self._name = name 
        else: 
            raise TypeError("Name must be a string!")
        
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        if type(location) == str:
            self._location = location
        else: 
            raise TypeError("Location must be a string!")
        

