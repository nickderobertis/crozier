



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Currency,
        CurrencyDetail,
        CurrencyDetailPeg,
        GetCurrenciesRequestScope,
        GetRatesRequestExpand,
        GetRatesRequestGroup,
        NotFoundErrorBody,
        Provider,
        ProviderPublishCadence,
        Rate,
        RateProvidersItem,
        UnprocessableEntityErrorBody,
    )
    from .errors import NotFoundError, UnprocessableEntityError
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "Currency": ".types",
    "CurrencyDetail": ".types",
    "CurrencyDetailPeg": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetCurrenciesRequestScope": ".types",
    "GetRatesRequestExpand": ".types",
    "GetRatesRequestGroup": ".types",
    "NotFoundError": ".errors",
    "NotFoundErrorBody": ".types",
    "Provider": ".types",
    "ProviderPublishCadence": ".types",
    "Rate": ".types",
    "RateProvidersItem": ".types",
    "UnprocessableEntityError": ".errors",
    "UnprocessableEntityErrorBody": ".types",
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
    "Currency",
    "CurrencyDetail",
    "CurrencyDetailPeg",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "GetCurrenciesRequestScope",
    "GetRatesRequestExpand",
    "GetRatesRequestGroup",
    "NotFoundError",
    "NotFoundErrorBody",
    "Provider",
    "ProviderPublishCadence",
    "Rate",
    "RateProvidersItem",
    "UnprocessableEntityError",
    "UnprocessableEntityErrorBody",
    "__version__",
]
