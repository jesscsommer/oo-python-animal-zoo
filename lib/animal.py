class Animal:

    all = []

    def __init__( self, species, weight, nickname, zoo ):
        self._species = species 
        self.weight = weight
        self._nickname = nickname
        self.zoo = zoo
        type(self).add_to_all_animals(self)

    @classmethod
    def add_to_all_animals(cls, new_animal):
        if isinstance(new_animal, cls):
            cls.all.append(new_animal)
        else: 
            raise TypeError("New animal must be an instance of Animal!")
        
    @classmethod
    def find_by_species(cls, species):
        results = [animal for animal in cls.all if animal._species == species]
        if results: return results
        return "No animals of that species!"

    # Properties 
    @property
    def weight(self):
        return self._weight
    
    @weight.setter 
    def weight(self, weight):
        if type(weight) == float or type(weight) == int: 
            self._weight = weight 
        else: 
            raise TypeError("Weight must be a number!")
        
