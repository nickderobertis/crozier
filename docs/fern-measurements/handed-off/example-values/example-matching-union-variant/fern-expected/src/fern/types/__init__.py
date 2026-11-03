



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .charm_seal import CharmSeal
    from .copper_badge import CopperBadge
    from .copper_kind import CopperKind
    from .entry_v1 import EntryV1
    from .entry_v2 import EntryV2
    from .page_v1 import PageV1
    from .page_v2 import PageV2
    from .page_v2edition import PageV2Edition
    from .stamp_seal import StampSeal
    from .tin_badge import TinBadge
    from .tin_kind import TinKind
    from .wax_seal import WaxSeal
_dynamic_imports: typing.Dict[str, str] = {
    "CharmSeal": ".charm_seal",
    "CopperBadge": ".copper_badge",
    "CopperKind": ".copper_kind",
    "EntryV1": ".entry_v1",
    "EntryV2": ".entry_v2",
    "PageV1": ".page_v1",
    "PageV2": ".page_v2",
    "PageV2Edition": ".page_v2edition",
    "StampSeal": ".stamp_seal",
    "TinBadge": ".tin_badge",
    "TinKind": ".tin_kind",
    "WaxSeal": ".wax_seal",
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
    "CharmSeal",
    "CopperBadge",
    "CopperKind",
    "EntryV1",
    "EntryV2",
    "PageV1",
    "PageV2",
    "PageV2Edition",
    "StampSeal",
    "TinBadge",
    "TinKind",
    "WaxSeal",
]
