



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .preprint_provider_detail_response import PreprintProviderDetailResponse
    from .preprint_provider_detail_response_attributes import PreprintProviderDetailResponseAttributes
    from .preprint_provider_detail_response_links import PreprintProviderDetailResponseLinks
    from .preprint_provider_detail_response_relationships import PreprintProviderDetailResponseRelationships
    from .preprint_provider_licenses_list_response import PreprintProviderLicensesListResponse
    from .preprint_provider_licenses_list_response_attributes import PreprintProviderLicensesListResponseAttributes
    from .preprint_provider_licenses_list_response_links import PreprintProviderLicensesListResponseLinks
    from .preprint_provider_list_response import PreprintProviderListResponse
    from .preprint_provider_list_response_attributes import PreprintProviderListResponseAttributes
    from .preprint_provider_list_response_links import PreprintProviderListResponseLinks
    from .preprint_provider_list_response_relationships import PreprintProviderListResponseRelationships
    from .preprint_provider_taxonomies_list_response import PreprintProviderTaxonomiesListResponse
    from .preprint_provider_taxonomies_list_response_attributes import PreprintProviderTaxonomiesListResponseAttributes
    from .preprint_provider_taxonomies_list_response_links import PreprintProviderTaxonomiesListResponseLinks
    from .preprint_providers_preprints_list_response_item import PreprintProvidersPreprintsListResponseItem
    from .preprint_providers_preprints_list_response_item_attributes import (
        PreprintProvidersPreprintsListResponseItemAttributes,
    )
    from .preprint_providers_preprints_list_response_item_links import PreprintProvidersPreprintsListResponseItemLinks
    from .preprint_providers_preprints_list_response_item_relationships import (
        PreprintProvidersPreprintsListResponseItemRelationships,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PreprintProviderDetailResponse": ".preprint_provider_detail_response",
    "PreprintProviderDetailResponseAttributes": ".preprint_provider_detail_response_attributes",
    "PreprintProviderDetailResponseLinks": ".preprint_provider_detail_response_links",
    "PreprintProviderDetailResponseRelationships": ".preprint_provider_detail_response_relationships",
    "PreprintProviderLicensesListResponse": ".preprint_provider_licenses_list_response",
    "PreprintProviderLicensesListResponseAttributes": ".preprint_provider_licenses_list_response_attributes",
    "PreprintProviderLicensesListResponseLinks": ".preprint_provider_licenses_list_response_links",
    "PreprintProviderListResponse": ".preprint_provider_list_response",
    "PreprintProviderListResponseAttributes": ".preprint_provider_list_response_attributes",
    "PreprintProviderListResponseLinks": ".preprint_provider_list_response_links",
    "PreprintProviderListResponseRelationships": ".preprint_provider_list_response_relationships",
    "PreprintProviderTaxonomiesListResponse": ".preprint_provider_taxonomies_list_response",
    "PreprintProviderTaxonomiesListResponseAttributes": ".preprint_provider_taxonomies_list_response_attributes",
    "PreprintProviderTaxonomiesListResponseLinks": ".preprint_provider_taxonomies_list_response_links",
    "PreprintProvidersPreprintsListResponseItem": ".preprint_providers_preprints_list_response_item",
    "PreprintProvidersPreprintsListResponseItemAttributes": ".preprint_providers_preprints_list_response_item_attributes",
    "PreprintProvidersPreprintsListResponseItemLinks": ".preprint_providers_preprints_list_response_item_links",
    "PreprintProvidersPreprintsListResponseItemRelationships": ".preprint_providers_preprints_list_response_item_relationships",
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
    "PreprintProviderDetailResponse",
    "PreprintProviderDetailResponseAttributes",
    "PreprintProviderDetailResponseLinks",
    "PreprintProviderDetailResponseRelationships",
    "PreprintProviderLicensesListResponse",
    "PreprintProviderLicensesListResponseAttributes",
    "PreprintProviderLicensesListResponseLinks",
    "PreprintProviderListResponse",
    "PreprintProviderListResponseAttributes",
    "PreprintProviderListResponseLinks",
    "PreprintProviderListResponseRelationships",
    "PreprintProviderTaxonomiesListResponse",
    "PreprintProviderTaxonomiesListResponseAttributes",
    "PreprintProviderTaxonomiesListResponseLinks",
    "PreprintProvidersPreprintsListResponseItem",
    "PreprintProvidersPreprintsListResponseItemAttributes",
    "PreprintProvidersPreprintsListResponseItemLinks",
    "PreprintProvidersPreprintsListResponseItemRelationships",
]
