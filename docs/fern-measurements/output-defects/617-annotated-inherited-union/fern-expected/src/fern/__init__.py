



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Coat,
        Coat_Gloss,
        Coat_Matte,
        GlossCoat,
        MatteCoat,
        Pot,
        PotOuterCoat,
        PotOuterCoat_Gloss,
        PotOuterCoat_Matte,
    )
    from . import pots
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .pots import RecoatPotRequestCoat, RecoatPotRequestCoat_Gloss, RecoatPotRequestCoat_Matte
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "Coat": ".types",
    "Coat_Gloss": ".types",
    "Coat_Matte": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GlossCoat": ".types",
    "MatteCoat": ".types",
    "Pot": ".types",
    "PotOuterCoat": ".types",
    "PotOuterCoat_Gloss": ".types",
    "PotOuterCoat_Matte": ".types",
    "RecoatPotRequestCoat": ".pots",
    "RecoatPotRequestCoat_Gloss": ".pots",
    "RecoatPotRequestCoat_Matte": ".pots",
    "__version__": ".version",
    "pots": ".pots",
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
    "Coat",
    "Coat_Gloss",
    "Coat_Matte",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "GlossCoat",
    "MatteCoat",
    "Pot",
    "PotOuterCoat",
    "PotOuterCoat_Gloss",
    "PotOuterCoat_Matte",
    "RecoatPotRequestCoat",
    "RecoatPotRequestCoat_Gloss",
    "RecoatPotRequestCoat_Matte",
    "__version__",
    "pots",
]
