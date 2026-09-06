



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .delete_link_country_link_id_country_request_country import DeleteLinkCountryLinkIdCountryRequestCountry
    from .delete_link_region_link_id_country_region_request_country import (
        DeleteLinkRegionLinkIdCountryRegionRequestCountry,
    )
    from .get_link_region_list_country_request_country import GetLinkRegionListCountryRequestCountry
    from .post_link_country_bulk_link_id_request_body_item import PostLinkCountryBulkLinkIdRequestBodyItem
    from .post_link_country_bulk_link_id_request_body_item_country import (
        PostLinkCountryBulkLinkIdRequestBodyItemCountry,
    )
    from .post_link_country_link_id_request_country import PostLinkCountryLinkIdRequestCountry
    from .post_link_region_bulk_link_id_request_body_item import PostLinkRegionBulkLinkIdRequestBodyItem
    from .post_link_region_bulk_link_id_request_body_item_country import PostLinkRegionBulkLinkIdRequestBodyItemCountry
    from .post_link_region_link_id_request_country import PostLinkRegionLinkIdRequestCountry
_dynamic_imports: typing.Dict[str, str] = {
    "DeleteLinkCountryLinkIdCountryRequestCountry": ".delete_link_country_link_id_country_request_country",
    "DeleteLinkRegionLinkIdCountryRegionRequestCountry": ".delete_link_region_link_id_country_region_request_country",
    "GetLinkRegionListCountryRequestCountry": ".get_link_region_list_country_request_country",
    "PostLinkCountryBulkLinkIdRequestBodyItem": ".post_link_country_bulk_link_id_request_body_item",
    "PostLinkCountryBulkLinkIdRequestBodyItemCountry": ".post_link_country_bulk_link_id_request_body_item_country",
    "PostLinkCountryLinkIdRequestCountry": ".post_link_country_link_id_request_country",
    "PostLinkRegionBulkLinkIdRequestBodyItem": ".post_link_region_bulk_link_id_request_body_item",
    "PostLinkRegionBulkLinkIdRequestBodyItemCountry": ".post_link_region_bulk_link_id_request_body_item_country",
    "PostLinkRegionLinkIdRequestCountry": ".post_link_region_link_id_request_country",
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
    "DeleteLinkCountryLinkIdCountryRequestCountry",
    "DeleteLinkRegionLinkIdCountryRegionRequestCountry",
    "GetLinkRegionListCountryRequestCountry",
    "PostLinkCountryBulkLinkIdRequestBodyItem",
    "PostLinkCountryBulkLinkIdRequestBodyItemCountry",
    "PostLinkCountryLinkIdRequestCountry",
    "PostLinkRegionBulkLinkIdRequestBodyItem",
    "PostLinkRegionBulkLinkIdRequestBodyItemCountry",
    "PostLinkRegionLinkIdRequestCountry",
]
