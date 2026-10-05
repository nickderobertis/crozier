



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .basket import Basket
    from .crate import Crate
    from .harvest import Harvest
    from .harvest_container import HarvestContainer
    from .harvest_container_zero import HarvestContainerZero, HarvestContainerZero_Basket, HarvestContainerZero_Crate
    from .harvest_grade import HarvestGrade
    from .harvest_grade_one import HarvestGradeOne
    from .harvest_holder import HarvestHolder
    from .harvest_holder_one import HarvestHolderOne, HarvestHolderOne_Basket, HarvestHolderOne_Crate
    from .harvest_yield_note import HarvestYieldNote
    from .harvest_yield_note_zero import HarvestYieldNoteZero
_dynamic_imports: typing.Dict[str, str] = {
    "Basket": ".basket",
    "Crate": ".crate",
    "Harvest": ".harvest",
    "HarvestContainer": ".harvest_container",
    "HarvestContainerZero": ".harvest_container_zero",
    "HarvestContainerZero_Basket": ".harvest_container_zero",
    "HarvestContainerZero_Crate": ".harvest_container_zero",
    "HarvestGrade": ".harvest_grade",
    "HarvestGradeOne": ".harvest_grade_one",
    "HarvestHolder": ".harvest_holder",
    "HarvestHolderOne": ".harvest_holder_one",
    "HarvestHolderOne_Basket": ".harvest_holder_one",
    "HarvestHolderOne_Crate": ".harvest_holder_one",
    "HarvestYieldNote": ".harvest_yield_note",
    "HarvestYieldNoteZero": ".harvest_yield_note_zero",
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
    "Basket",
    "Crate",
    "Harvest",
    "HarvestContainer",
    "HarvestContainerZero",
    "HarvestContainerZero_Basket",
    "HarvestContainerZero_Crate",
    "HarvestGrade",
    "HarvestGradeOne",
    "HarvestHolder",
    "HarvestHolderOne",
    "HarvestHolderOne_Basket",
    "HarvestHolderOne_Crate",
    "HarvestYieldNote",
    "HarvestYieldNoteZero",
]
