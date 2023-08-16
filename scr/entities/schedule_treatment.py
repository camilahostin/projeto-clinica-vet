import datetime
from scr.entities.animal import Animal
from scr.entities.veterinarian import Veterinarian


class ScheduleTreatment:

    def __init__(self, animal: Animal, veterinarian: Veterinarian,
                datetime_: datetime,  notes: str) -> None:
        self.animal = animal
        self.veterinarian = veterinarian
        self.datetime_ = datetime_
        self.notes = notes
