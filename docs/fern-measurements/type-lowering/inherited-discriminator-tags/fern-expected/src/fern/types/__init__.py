



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .cat import Cat
    from .dog import Dog
    from .grooming_task import GroomingTask
    from .grooming_task_all_of import GroomingTaskAllOf
    from .grooming_task_all_of_action import GroomingTaskAllOfAction
    from .pet import Pet
    from .task import Task
    from .walking_task import WalkingTask
    from .walking_task_all_of import WalkingTaskAllOf
    from .walking_task_all_of_action import WalkingTaskAllOfAction
_dynamic_imports: typing.Dict[str, str] = {
    "Cat": ".cat",
    "Dog": ".dog",
    "GroomingTask": ".grooming_task",
    "GroomingTaskAllOf": ".grooming_task_all_of",
    "GroomingTaskAllOfAction": ".grooming_task_all_of_action",
    "Pet": ".pet",
    "Task": ".task",
    "WalkingTask": ".walking_task",
    "WalkingTaskAllOf": ".walking_task_all_of",
    "WalkingTaskAllOfAction": ".walking_task_all_of_action",
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
    "Cat",
    "Dog",
    "GroomingTask",
    "GroomingTaskAllOf",
    "GroomingTaskAllOfAction",
    "Pet",
    "Task",
    "WalkingTask",
    "WalkingTaskAllOf",
    "WalkingTaskAllOfAction",
]
