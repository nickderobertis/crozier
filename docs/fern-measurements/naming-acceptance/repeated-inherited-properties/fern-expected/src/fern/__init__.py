



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Folder,
        OligoBase,
        OligoBaseForCreate,
        OligoCreate,
        PlasmidBase,
        PlasmidBaseForCreate,
        PlasmidCopies,
        PlasmidCreate,
        PrimerBase,
        PrimerBaseForCreate,
        PrimerCreate,
        PrimerMeasure,
        RegistryTarget,
        StrainBase,
        StrainBaseForCreate,
        StrainCreate,
        StrainTarget,
        VectorBase,
        VectorBaseForCreate,
        VectorCreate,
        VectorPlacement,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "Folder": ".types",
    "OligoBase": ".types",
    "OligoBaseForCreate": ".types",
    "OligoCreate": ".types",
    "PlasmidBase": ".types",
    "PlasmidBaseForCreate": ".types",
    "PlasmidCopies": ".types",
    "PlasmidCreate": ".types",
    "PrimerBase": ".types",
    "PrimerBaseForCreate": ".types",
    "PrimerCreate": ".types",
    "PrimerMeasure": ".types",
    "RegistryTarget": ".types",
    "StrainBase": ".types",
    "StrainBaseForCreate": ".types",
    "StrainCreate": ".types",
    "StrainTarget": ".types",
    "VectorBase": ".types",
    "VectorBaseForCreate": ".types",
    "VectorCreate": ".types",
    "VectorPlacement": ".types",
    "__version__": ".version",
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
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "Folder",
    "OligoBase",
    "OligoBaseForCreate",
    "OligoCreate",
    "PlasmidBase",
    "PlasmidBaseForCreate",
    "PlasmidCopies",
    "PlasmidCreate",
    "PrimerBase",
    "PrimerBaseForCreate",
    "PrimerCreate",
    "PrimerMeasure",
    "RegistryTarget",
    "StrainBase",
    "StrainBaseForCreate",
    "StrainCreate",
    "StrainTarget",
    "VectorBase",
    "VectorBaseForCreate",
    "VectorCreate",
    "VectorPlacement",
    "__version__",
]
