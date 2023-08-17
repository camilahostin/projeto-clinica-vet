from src.entities.owner import Owner


class Animal:

    def __init__(self, name: str, species: str, weight: str, age: str, owner: Owner) -> None:
        self.name = name
        self.species = species
        self.weight = weight
        self.age = age
        self.owner = owner
