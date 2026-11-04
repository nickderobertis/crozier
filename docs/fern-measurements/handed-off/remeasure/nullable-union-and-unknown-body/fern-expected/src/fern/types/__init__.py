



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .dispatch import Dispatch
    from .get_shipment_response import GetShipmentResponse, GetShipmentResponse_Notice, GetShipmentResponse_Parcel
    from .get_shipment_response_notice import GetShipmentResponseNotice
    from .get_shipment_response_parcel import GetShipmentResponseParcel
    from .notice import Notice
    from .notice_kind import NoticeKind
    from .parcel import Parcel
    from .parcel_kind import ParcelKind
_dynamic_imports: typing.Dict[str, str] = {
    "Dispatch": ".dispatch",
    "GetShipmentResponse": ".get_shipment_response",
    "GetShipmentResponseNotice": ".get_shipment_response_notice",
    "GetShipmentResponseParcel": ".get_shipment_response_parcel",
    "GetShipmentResponse_Notice": ".get_shipment_response",
    "GetShipmentResponse_Parcel": ".get_shipment_response",
    "Notice": ".notice",
    "NoticeKind": ".notice_kind",
    "Parcel": ".parcel",
    "ParcelKind": ".parcel_kind",
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
    "Dispatch",
    "GetShipmentResponse",
    "GetShipmentResponseNotice",
    "GetShipmentResponseParcel",
    "GetShipmentResponse_Notice",
    "GetShipmentResponse_Parcel",
    "Notice",
    "NoticeKind",
    "Parcel",
    "ParcelKind",
]
