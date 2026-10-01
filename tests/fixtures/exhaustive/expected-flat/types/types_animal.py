

import typing

from .types_animal_one import TypesAnimalOne
from .types_animal_zero import TypesAnimalZero

TypesAnimal = typing.Union[TypesAnimalZero, TypesAnimalOne]
