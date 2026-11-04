



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .basket import Basket
    from .delivery import Delivery, Delivery_Rail, Delivery_Road
    from .delivery_condition import DeliveryCondition
    from .delivery_rail import DeliveryRail
    from .delivery_road import DeliveryRoad
    from .dispatch import Dispatch
    from .notice import Notice, Notice_Paper, Notice_Radio
    from .notice_condition import NoticeCondition
    from .notice_paper import NoticePaper
    from .notice_radio import NoticeRadio
    from .routing_hint import RoutingHint
    from .routing_hint_code import RoutingHintCode
    from .routing_hint_detail import RoutingHintDetail
    from .spare_basket import SpareBasket
_dynamic_imports: typing.Dict[str, str] = {
    "Basket": ".basket",
    "Delivery": ".delivery",
    "DeliveryCondition": ".delivery_condition",
    "DeliveryRail": ".delivery_rail",
    "DeliveryRoad": ".delivery_road",
    "Delivery_Rail": ".delivery",
    "Delivery_Road": ".delivery",
    "Dispatch": ".dispatch",
    "Notice": ".notice",
    "NoticeCondition": ".notice_condition",
    "NoticePaper": ".notice_paper",
    "NoticeRadio": ".notice_radio",
    "Notice_Paper": ".notice",
    "Notice_Radio": ".notice",
    "RoutingHint": ".routing_hint",
    "RoutingHintCode": ".routing_hint_code",
    "RoutingHintDetail": ".routing_hint_detail",
    "SpareBasket": ".spare_basket",
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
    "Basket",
    "Delivery",
    "DeliveryCondition",
    "DeliveryRail",
    "DeliveryRoad",
    "Delivery_Rail",
    "Delivery_Road",
    "Dispatch",
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
]
