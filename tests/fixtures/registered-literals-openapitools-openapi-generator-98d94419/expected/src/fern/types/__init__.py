



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .cat import Cat
    from .cat_hunting_skill import CatHuntingSkill
    from .cat_pet_type import CatPetType
    from .dog import Dog
    from .dog_pet_type import DogPetType
    from .pet import Pet
_dynamic_imports: typing.Dict[str, str] = {
    "Cat": ".cat",
    "CatHuntingSkill": ".cat_hunting_skill",
    "CatPetType": ".cat_pet_type",
    "Dog": ".dog",
    "DogPetType": ".dog_pet_type",
    "Pet": ".pet",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = ["Cat", "CatHuntingSkill", "CatPetType", "Dog", "DogPetType", "Pet"]
