



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .thread import Thread, Thread_Plain, Thread_Woven
    from .thread_plain import ThreadPlain
    from .thread_woven import ThreadWoven
    from .weave import Weave, Weave_Joined, Weave_Loose
    from .weave_joined import WeaveJoined
    from .weave_loose import WeaveLoose
_dynamic_imports: typing.Dict[str, str] = {
    "Thread": ".thread",
    "ThreadPlain": ".thread_plain",
    "ThreadWoven": ".thread_woven",
    "Thread_Plain": ".thread",
    "Thread_Woven": ".thread",
    "Weave": ".weave",
    "WeaveJoined": ".weave_joined",
    "WeaveLoose": ".weave_loose",
    "Weave_Joined": ".weave",
    "Weave_Loose": ".weave",
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
    "Thread",
    "ThreadPlain",
    "ThreadWoven",
    "Thread_Plain",
    "Thread_Woven",
    "Weave",
    "WeaveJoined",
    "WeaveLoose",
    "Weave_Joined",
    "Weave_Loose",
]
