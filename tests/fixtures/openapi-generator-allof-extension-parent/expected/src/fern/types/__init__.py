



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .adult import Adult
    from .all_of_with_properties import AllOfWithProperties
    from .all_of_with_single_item import AllOfWithSingleItem
    from .ancestor import Ancestor
    from .another_child import AnotherChild
    from .another_parent import AnotherParent
    from .another_person import AnotherPerson
    from .child import Child
    from .offspring import Offspring
    from .person import Person
    from .person_a import PersonA
    from .person_a_explicit_parent import PersonAExplicitParent
    from .person_b import PersonB
    from .schema_with_two_all_of_refs import SchemaWithTwoAllOfRefs
    from .schema_with_two_all_of_refs_one_is_marked_as_parent import SchemaWithTwoAllOfRefsOneIsMarkedAsParent
_dynamic_imports: typing.Dict[str, str] = {
    "Adult": ".adult",
    "AllOfWithProperties": ".all_of_with_properties",
    "AllOfWithSingleItem": ".all_of_with_single_item",
    "Ancestor": ".ancestor",
    "AnotherChild": ".another_child",
    "AnotherParent": ".another_parent",
    "AnotherPerson": ".another_person",
    "Child": ".child",
    "Offspring": ".offspring",
    "Person": ".person",
    "PersonA": ".person_a",
    "PersonAExplicitParent": ".person_a_explicit_parent",
    "PersonB": ".person_b",
    "SchemaWithTwoAllOfRefs": ".schema_with_two_all_of_refs",
    "SchemaWithTwoAllOfRefsOneIsMarkedAsParent": ".schema_with_two_all_of_refs_one_is_marked_as_parent",
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


__all__ = [
    "Adult",
    "AllOfWithProperties",
    "AllOfWithSingleItem",
    "Ancestor",
    "AnotherChild",
    "AnotherParent",
    "AnotherPerson",
    "Child",
    "Offspring",
    "Person",
    "PersonA",
    "PersonAExplicitParent",
    "PersonB",
    "SchemaWithTwoAllOfRefs",
    "SchemaWithTwoAllOfRefsOneIsMarkedAsParent",
]
