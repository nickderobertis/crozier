



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_sites_response import CreateSitesResponse
    from .create_sites_response_custom_domains_item import CreateSitesResponseCustomDomainsItem
    from .create_sites_response_data_collection_type import CreateSitesResponseDataCollectionType
    from .create_sites_response_locales import CreateSitesResponseLocales
    from .create_sites_response_locales_primary import CreateSitesResponseLocalesPrimary
    from .create_sites_response_locales_secondary_item import CreateSitesResponseLocalesSecondaryItem
    from .get_custom_domain_sites_response import GetCustomDomainSitesResponse
    from .get_custom_domain_sites_response_custom_domains_item import GetCustomDomainSitesResponseCustomDomainsItem
    from .get_sites_response import GetSitesResponse
    from .get_sites_response_custom_domains_item import GetSitesResponseCustomDomainsItem
    from .get_sites_response_data_collection_type import GetSitesResponseDataCollectionType
    from .get_sites_response_locales import GetSitesResponseLocales
    from .get_sites_response_locales_primary import GetSitesResponseLocalesPrimary
    from .get_sites_response_locales_secondary_item import GetSitesResponseLocalesSecondaryItem
    from .list_sites_response import ListSitesResponse
    from .list_sites_response_sites_item import ListSitesResponseSitesItem
    from .list_sites_response_sites_item_custom_domains_item import ListSitesResponseSitesItemCustomDomainsItem
    from .list_sites_response_sites_item_data_collection_type import ListSitesResponseSitesItemDataCollectionType
    from .list_sites_response_sites_item_locales import ListSitesResponseSitesItemLocales
    from .list_sites_response_sites_item_locales_primary import ListSitesResponseSitesItemLocalesPrimary
    from .list_sites_response_sites_item_locales_secondary_item import ListSitesResponseSitesItemLocalesSecondaryItem
    from .publish_sites_response import PublishSitesResponse
    from .publish_sites_response_custom_domains_item import PublishSitesResponseCustomDomainsItem
    from .publish_sites_response_publish_scope import PublishSitesResponsePublishScope
    from .site_publish_payload import SitePublishPayload
    from .site_publish_payload_payload import SitePublishPayloadPayload
    from .site_publish_payload_payload_publish_scope import SitePublishPayloadPayloadPublishScope
    from .update_sites_response import UpdateSitesResponse
    from .update_sites_response_custom_domains_item import UpdateSitesResponseCustomDomainsItem
    from .update_sites_response_data_collection_type import UpdateSitesResponseDataCollectionType
    from .update_sites_response_locales import UpdateSitesResponseLocales
    from .update_sites_response_locales_primary import UpdateSitesResponseLocalesPrimary
    from .update_sites_response_locales_secondary_item import UpdateSitesResponseLocalesSecondaryItem
_dynamic_imports: typing.Dict[str, str] = {
    "CreateSitesResponse": ".create_sites_response",
    "CreateSitesResponseCustomDomainsItem": ".create_sites_response_custom_domains_item",
    "CreateSitesResponseDataCollectionType": ".create_sites_response_data_collection_type",
    "CreateSitesResponseLocales": ".create_sites_response_locales",
    "CreateSitesResponseLocalesPrimary": ".create_sites_response_locales_primary",
    "CreateSitesResponseLocalesSecondaryItem": ".create_sites_response_locales_secondary_item",
    "GetCustomDomainSitesResponse": ".get_custom_domain_sites_response",
    "GetCustomDomainSitesResponseCustomDomainsItem": ".get_custom_domain_sites_response_custom_domains_item",
    "GetSitesResponse": ".get_sites_response",
    "GetSitesResponseCustomDomainsItem": ".get_sites_response_custom_domains_item",
    "GetSitesResponseDataCollectionType": ".get_sites_response_data_collection_type",
    "GetSitesResponseLocales": ".get_sites_response_locales",
    "GetSitesResponseLocalesPrimary": ".get_sites_response_locales_primary",
    "GetSitesResponseLocalesSecondaryItem": ".get_sites_response_locales_secondary_item",
    "ListSitesResponse": ".list_sites_response",
    "ListSitesResponseSitesItem": ".list_sites_response_sites_item",
    "ListSitesResponseSitesItemCustomDomainsItem": ".list_sites_response_sites_item_custom_domains_item",
    "ListSitesResponseSitesItemDataCollectionType": ".list_sites_response_sites_item_data_collection_type",
    "ListSitesResponseSitesItemLocales": ".list_sites_response_sites_item_locales",
    "ListSitesResponseSitesItemLocalesPrimary": ".list_sites_response_sites_item_locales_primary",
    "ListSitesResponseSitesItemLocalesSecondaryItem": ".list_sites_response_sites_item_locales_secondary_item",
    "PublishSitesResponse": ".publish_sites_response",
    "PublishSitesResponseCustomDomainsItem": ".publish_sites_response_custom_domains_item",
    "PublishSitesResponsePublishScope": ".publish_sites_response_publish_scope",
    "SitePublishPayload": ".site_publish_payload",
    "SitePublishPayloadPayload": ".site_publish_payload_payload",
    "SitePublishPayloadPayloadPublishScope": ".site_publish_payload_payload_publish_scope",
    "UpdateSitesResponse": ".update_sites_response",
    "UpdateSitesResponseCustomDomainsItem": ".update_sites_response_custom_domains_item",
    "UpdateSitesResponseDataCollectionType": ".update_sites_response_data_collection_type",
    "UpdateSitesResponseLocales": ".update_sites_response_locales",
    "UpdateSitesResponseLocalesPrimary": ".update_sites_response_locales_primary",
    "UpdateSitesResponseLocalesSecondaryItem": ".update_sites_response_locales_secondary_item",
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
    "CreateSitesResponse",
    "CreateSitesResponseCustomDomainsItem",
    "CreateSitesResponseDataCollectionType",
    "CreateSitesResponseLocales",
    "CreateSitesResponseLocalesPrimary",
    "CreateSitesResponseLocalesSecondaryItem",
    "GetCustomDomainSitesResponse",
    "GetCustomDomainSitesResponseCustomDomainsItem",
    "GetSitesResponse",
    "GetSitesResponseCustomDomainsItem",
    "GetSitesResponseDataCollectionType",
    "GetSitesResponseLocales",
    "GetSitesResponseLocalesPrimary",
    "GetSitesResponseLocalesSecondaryItem",
    "ListSitesResponse",
    "ListSitesResponseSitesItem",
    "ListSitesResponseSitesItemCustomDomainsItem",
    "ListSitesResponseSitesItemDataCollectionType",
    "ListSitesResponseSitesItemLocales",
    "ListSitesResponseSitesItemLocalesPrimary",
    "ListSitesResponseSitesItemLocalesSecondaryItem",
    "PublishSitesResponse",
    "PublishSitesResponseCustomDomainsItem",
    "PublishSitesResponsePublishScope",
    "SitePublishPayload",
    "SitePublishPayloadPayload",
    "SitePublishPayloadPayloadPublishScope",
    "UpdateSitesResponse",
    "UpdateSitesResponseCustomDomainsItem",
    "UpdateSitesResponseDataCollectionType",
    "UpdateSitesResponseLocales",
    "UpdateSitesResponseLocalesPrimary",
    "UpdateSitesResponseLocalesSecondaryItem",
]
