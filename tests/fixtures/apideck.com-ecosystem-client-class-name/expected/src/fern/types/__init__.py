



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .card_settings import CardSettings
    from .category import Category
    from .collection import Collection
    from .contact import Contact
    from .cta_settings import CtaSettings
    from .custom_settings import CustomSettings
    from .ecosystem import Ecosystem
    from .ecosystem_menu_position import EcosystemMenuPosition
    from .ecosystem_menu_style import EcosystemMenuStyle
    from .ecosystem_navigation_mobile_menu_type import EcosystemNavigationMobileMenuType
    from .file import File
    from .file_type import FileType
    from .get_categories_response import GetCategoriesResponse
    from .get_category_response import GetCategoryResponse
    from .get_collection_response import GetCollectionResponse
    from .get_collections_response import GetCollectionsResponse
    from .get_ecosystem_response import GetEcosystemResponse
    from .get_listing_response import GetListingResponse
    from .get_listings_response import GetListingsResponse
    from .get_product_response import GetProductResponse
    from .get_products_response import GetProductsResponse
    from .integration_settings import IntegrationSettings
    from .lead_form_settings import LeadFormSettings
    from .links import Links
    from .listing import Listing
    from .listing_settings import ListingSettings
    from .listing_settings_naming import ListingSettingsNaming
    from .listing_settings_sidebar_position import ListingSettingsSidebarPosition
    from .logo import Logo
    from .logo_type import LogoType
    from .masthead_settings import MastheadSettings
    from .media import Media
    from .media_type import MediaType
    from .meta import Meta
    from .meta_cursors import MetaCursors
    from .meta_tag_settings import MetaTagSettings
    from .partner import Partner
    from .product import Product
    from .screenshot import Screenshot
    from .translation import Translation
    from .translations import Translations
_dynamic_imports: typing.Dict[str, str] = {
    "CardSettings": ".card_settings",
    "Category": ".category",
    "Collection": ".collection",
    "Contact": ".contact",
    "CtaSettings": ".cta_settings",
    "CustomSettings": ".custom_settings",
    "Ecosystem": ".ecosystem",
    "EcosystemMenuPosition": ".ecosystem_menu_position",
    "EcosystemMenuStyle": ".ecosystem_menu_style",
    "EcosystemNavigationMobileMenuType": ".ecosystem_navigation_mobile_menu_type",
    "File": ".file",
    "FileType": ".file_type",
    "GetCategoriesResponse": ".get_categories_response",
    "GetCategoryResponse": ".get_category_response",
    "GetCollectionResponse": ".get_collection_response",
    "GetCollectionsResponse": ".get_collections_response",
    "GetEcosystemResponse": ".get_ecosystem_response",
    "GetListingResponse": ".get_listing_response",
    "GetListingsResponse": ".get_listings_response",
    "GetProductResponse": ".get_product_response",
    "GetProductsResponse": ".get_products_response",
    "IntegrationSettings": ".integration_settings",
    "LeadFormSettings": ".lead_form_settings",
    "Links": ".links",
    "Listing": ".listing",
    "ListingSettings": ".listing_settings",
    "ListingSettingsNaming": ".listing_settings_naming",
    "ListingSettingsSidebarPosition": ".listing_settings_sidebar_position",
    "Logo": ".logo",
    "LogoType": ".logo_type",
    "MastheadSettings": ".masthead_settings",
    "Media": ".media",
    "MediaType": ".media_type",
    "Meta": ".meta",
    "MetaCursors": ".meta_cursors",
    "MetaTagSettings": ".meta_tag_settings",
    "Partner": ".partner",
    "Product": ".product",
    "Screenshot": ".screenshot",
    "Translation": ".translation",
    "Translations": ".translations",
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
]
