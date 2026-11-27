



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BeadRef,
        BeadRef_Glass,
        BeadRef_Wood,
        BlendDye,
        BlendYarn,
        GlassBead,
        Knot,
        PlainPattern,
        TwillPattern,
        WarpThread,
        Weave,
        WeaveFinish,
        WeaveFinishDelivery,
        WeavePlan,
        WeavePlanFinish,
        WeavePlanPattern,
        WeavePlanPattern_Plain,
        WeavePlanPattern_Twill,
        WeavePlanThreadsItem,
        WeavePlanThreadsItem_Warp,
        WeavePlanThreadsItem_Weft,
        WeftThread,
        WoodBead,
    )
    from . import weaves
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BeadRef": ".types",
    "BeadRef_Glass": ".types",
    "BeadRef_Wood": ".types",
    "BlendDye": ".types",
    "BlendYarn": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "GlassBead": ".types",
    "Knot": ".types",
    "PlainPattern": ".types",
    "TwillPattern": ".types",
    "WarpThread": ".types",
    "Weave": ".types",
    "WeaveFinish": ".types",
    "WeaveFinishDelivery": ".types",
    "WeavePlan": ".types",
    "WeavePlanFinish": ".types",
    "WeavePlanPattern": ".types",
    "WeavePlanPattern_Plain": ".types",
    "WeavePlanPattern_Twill": ".types",
    "WeavePlanThreadsItem": ".types",
    "WeavePlanThreadsItem_Warp": ".types",
    "WeavePlanThreadsItem_Weft": ".types",
    "WeftThread": ".types",
    "WoodBead": ".types",
    "__version__": ".version",
    "weaves": ".weaves",
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
    "AsyncFernApi",
    "BeadRef",
    "BeadRef_Glass",
    "BeadRef_Wood",
    "BlendDye",
    "BlendYarn",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "GlassBead",
    "Knot",
    "PlainPattern",
    "TwillPattern",
    "WarpThread",
    "Weave",
    "WeaveFinish",
    "WeaveFinishDelivery",
    "WeavePlan",
    "WeavePlanFinish",
    "WeavePlanPattern",
    "WeavePlanPattern_Plain",
    "WeavePlanPattern_Twill",
    "WeavePlanThreadsItem",
    "WeavePlanThreadsItem_Warp",
    "WeavePlanThreadsItem_Weft",
    "WeftThread",
    "WoodBead",
    "__version__",
    "weaves",
]
