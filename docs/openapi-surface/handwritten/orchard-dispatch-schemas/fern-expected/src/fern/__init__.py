



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Basket,
        Delivery,
        DeliveryCondition,
        DeliveryRail,
        DeliveryRoad,
        Delivery_Rail,
        Delivery_Road,
        Dispatch,
        Notice,
        NoticeCondition,
        NoticePaper,
        NoticeRadio,
        Notice_Paper,
        Notice_Radio,
        RoutingHint,
        RoutingHintCode,
        RoutingHintDetail,
        SpareBasket,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "Basket": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Delivery": ".types",
    "DeliveryCondition": ".types",
    "DeliveryRail": ".types",
    "DeliveryRoad": ".types",
    "Delivery_Rail": ".types",
    "Delivery_Road": ".types",
    "Dispatch": ".types",
    "FernApi": ".client",
    "Notice": ".types",
    "NoticeCondition": ".types",
    "NoticePaper": ".types",
    "NoticeRadio": ".types",
    "Notice_Paper": ".types",
    "Notice_Radio": ".types",
    "RoutingHint": ".types",
    "RoutingHintCode": ".types",
    "RoutingHintDetail": ".types",
    "SpareBasket": ".types",
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
    "Basket",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Delivery",
    "DeliveryCondition",
    "DeliveryRail",
    "DeliveryRoad",
    "Delivery_Rail",
    "Delivery_Road",
    "Dispatch",
    "FernApi",
    "Notice",
    "NoticeCondition",
    "NoticePaper",
    "NoticeRadio",
    "Notice_Paper",
    "Notice_Radio",
    "RoutingHint",
    "RoutingHintCode",
    "RoutingHintDetail",
    "SpareBasket",
    "__version__",
]
