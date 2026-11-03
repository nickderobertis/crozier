



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .delivery_choice import DeliveryChoice
    from .delivery_choice_one import DeliveryChoiceOne
    from .delivery_choice_one_method import DeliveryChoiceOneMethod
    from .delivery_choice_zero import DeliveryChoiceZero
    from .delivery_choice_zero_method import DeliveryChoiceZeroMethod
    from .doorstep_choice import DoorstepChoice
    from .locker_choice import LockerChoice
_dynamic_imports: typing.Dict[str, str] = {
    "DeliveryChoice": ".delivery_choice",
    "DeliveryChoiceOne": ".delivery_choice_one",
    "DeliveryChoiceOneMethod": ".delivery_choice_one_method",
    "DeliveryChoiceZero": ".delivery_choice_zero",
    "DeliveryChoiceZeroMethod": ".delivery_choice_zero_method",
    "DoorstepChoice": ".doorstep_choice",
    "LockerChoice": ".locker_choice",
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
    "DeliveryChoice",
    "DeliveryChoiceOne",
    "DeliveryChoiceOneMethod",
    "DeliveryChoiceZero",
    "DeliveryChoiceZeroMethod",
    "DoorstepChoice",
    "LockerChoice",
]
