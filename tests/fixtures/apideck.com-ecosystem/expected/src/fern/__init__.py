



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CardSettings,
        Category,
        Collection,
        Contact,
        CtaSettings,
        CustomSettings,
        Ecosystem,
        EcosystemMenuPosition,
        EcosystemMenuStyle,
        EcosystemNavigationMobileMenuType,
        File,
        FileType,
        GetCategoriesResponse,
        GetCategoryResponse,
        GetCollectionResponse,
        GetCollectionsResponse,
        GetEcosystemResponse,
        GetListingResponse,
        GetListingsResponse,
        GetProductResponse,
        GetProductsResponse,
        IntegrationSettings,
        LeadFormSettings,
        Links,
        Listing,
        ListingSettings,
        ListingSettingsNaming,
        ListingSettingsSidebarPosition,
        Logo,
        LogoType,
        MastheadSettings,
        Media,
        MediaType,
        Meta,
        MetaCursors,
        MetaTagSettings,
        Partner,
        Product,
        Screenshot,
        Translation,
        Translations,
    )
    from . import category, collection, ecosystem, listing, product
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "CardSettings": ".types",
    "Category": ".types",
    "Collection": ".types",
    "Contact": ".types",
    "CtaSettings": ".types",
    "CustomSettings": ".types",
    "Ecosystem": ".types",
    "EcosystemMenuPosition": ".types",
    "EcosystemMenuStyle": ".types",
    "EcosystemNavigationMobileMenuType": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "File": ".types",
    "FileType": ".types",
    "GetCategoriesResponse": ".types",
    "GetCategoryResponse": ".types",
    "GetCollectionResponse": ".types",
    "GetCollectionsResponse": ".types",
    "GetEcosystemResponse": ".types",
    "GetListingResponse": ".types",
    "GetListingsResponse": ".types",
    "GetProductResponse": ".types",
    "GetProductsResponse": ".types",
    "IntegrationSettings": ".types",
    "LeadFormSettings": ".types",
    "Links": ".types",
    "Listing": ".types",
    "ListingSettings": ".types",
    "ListingSettingsNaming": ".types",
    "ListingSettingsSidebarPosition": ".types",
    "Logo": ".types",
    "LogoType": ".types",
    "MastheadSettings": ".types",
    "Media": ".types",
    "MediaType": ".types",
    "Meta": ".types",
    "MetaCursors": ".types",
    "MetaTagSettings": ".types",
    "Partner": ".types",
    "Product": ".types",
    "Screenshot": ".types",
    "Translation": ".types",
    "Translations": ".types",
    "__version__": ".version",
    "category": ".category",
    "collection": ".collection",
    "ecosystem": ".ecosystem",
    "listing": ".listing",
    "product": ".product",
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
    "CardSettings",
    "Category",
    "Collection",
    "Contact",
    "CtaSettings",
    "CustomSettings",
    "Ecosystem",
    "EcosystemMenuPosition",
    "EcosystemMenuStyle",
    "EcosystemNavigationMobileMenuType",
    "FernApi",
    "FernApiEnvironment",
    "File",
    "FileType",
    "GetCategoriesResponse",
    "GetCategoryResponse",
    "GetCollectionResponse",
    "GetCollectionsResponse",
    "GetEcosystemResponse",
    "GetListingResponse",
    "GetListingsResponse",
    "GetProductResponse",
    "GetProductsResponse",
    "IntegrationSettings",
    "LeadFormSettings",
    "Links",
    "Listing",
    "ListingSettings",
    "ListingSettingsNaming",
    "ListingSettingsSidebarPosition",
    "Logo",
    "LogoType",
    "MastheadSettings",
    "Media",
    "MediaType",
    "Meta",
    "MetaCursors",
    "MetaTagSettings",
    "Partner",
    "Product",
    "Screenshot",
    "Translation",
    "Translations",
    "__version__",
    "category",
    "collection",
    "ecosystem",
    "listing",
    "product",
]
