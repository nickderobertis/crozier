



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .hash_d31b2f251c984df5575331831c174f719158747bfcbc58788d44da87badfa415 import (
        HashD31B2F251C984Df5575331831C174F719158747Bfcbc58788D44Da87Badfa415,
    )
    from .obj1 import Obj1
    from .obj2 import Obj2
    from .obj3 import Obj3
    from .obj3stuff import Obj3Stuff
    from .obj3stuff_zero import Obj3StuffZero
_dynamic_imports: typing.Dict[str, str] = {
    "HashD31B2F251C984Df5575331831C174F719158747Bfcbc58788D44Da87Badfa415": ".hash_d31b2f251c984df5575331831c174f719158747bfcbc58788d44da87badfa415",
    "Obj1": ".obj1",
    "Obj2": ".obj2",
    "Obj3": ".obj3",
    "Obj3Stuff": ".obj3stuff",
    "Obj3StuffZero": ".obj3stuff_zero",
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
    "HashD31B2F251C984Df5575331831C174F719158747Bfcbc58788D44Da87Badfa415",
    "Obj1",
    "Obj2",
    "Obj3",
    "Obj3Stuff",
    "Obj3StuffZero",
]
