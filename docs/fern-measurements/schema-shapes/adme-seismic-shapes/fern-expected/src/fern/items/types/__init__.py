



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .items_create_request_data import ItemsCreateRequestData
    from .items_create_request_data_props import ItemsCreateRequestDataProps
    from .items_create_request_info import ItemsCreateRequestInfo
    from .items_create_request_meta_item import ItemsCreateRequestMetaItem
    from .items_create_request_meta_item_crs_id import ItemsCreateRequestMetaItemCrsId
    from .items_create_request_meta_item_crs_id_kind import ItemsCreateRequestMetaItemCrsIdKind
    from .items_create_request_meta_item_unit_id import ItemsCreateRequestMetaItemUnitId
    from .items_create_request_meta_item_unit_id_kind import ItemsCreateRequestMetaItemUnitIdKind
_dynamic_imports: typing.Dict[str, str] = {
    "ItemsCreateRequestData": ".items_create_request_data",
    "ItemsCreateRequestDataProps": ".items_create_request_data_props",
    "ItemsCreateRequestInfo": ".items_create_request_info",
    "ItemsCreateRequestMetaItem": ".items_create_request_meta_item",
    "ItemsCreateRequestMetaItemCrsId": ".items_create_request_meta_item_crs_id",
    "ItemsCreateRequestMetaItemCrsIdKind": ".items_create_request_meta_item_crs_id_kind",
    "ItemsCreateRequestMetaItemUnitId": ".items_create_request_meta_item_unit_id",
    "ItemsCreateRequestMetaItemUnitIdKind": ".items_create_request_meta_item_unit_id_kind",
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
    "ItemsCreateRequestData",
    "ItemsCreateRequestDataProps",
    "ItemsCreateRequestInfo",
    "ItemsCreateRequestMetaItem",
    "ItemsCreateRequestMetaItemCrsId",
    "ItemsCreateRequestMetaItemCrsIdKind",
    "ItemsCreateRequestMetaItemUnitId",
    "ItemsCreateRequestMetaItemUnitIdKind",
]
