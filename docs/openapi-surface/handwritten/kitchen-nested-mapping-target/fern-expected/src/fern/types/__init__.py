



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .course import Course, Course_Grill, Course_Pastry
    from .grill_course import GrillCourse
    from .pastry_course import PastryCourse
    from .skewer_order import SkewerOrder
    from .skewer_order_station import SkewerOrderStation
    from .steak_order import SteakOrder
    from .steak_order_station import SteakOrderStation
_dynamic_imports: typing.Dict[str, str] = {
    "Course": ".course",
    "Course_Grill": ".course",
    "Course_Pastry": ".course",
    "GrillCourse": ".grill_course",
    "PastryCourse": ".pastry_course",
    "SkewerOrder": ".skewer_order",
    "SkewerOrderStation": ".skewer_order_station",
    "SteakOrder": ".steak_order",
    "SteakOrderStation": ".steak_order_station",
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
    "Course",
    "Course_Grill",
    "Course_Pastry",
    "GrillCourse",
    "PastryCourse",
    "SkewerOrder",
    "SkewerOrderStation",
    "SteakOrder",
    "SteakOrderStation",
]
