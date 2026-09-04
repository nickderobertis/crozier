



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Artifact,
        ArtifactFormat,
        ArtifactType,
        Checksum,
        ChecksumType,
        Cle,
        CleDefinitions,
        CleEvent,
        CleEventType,
        CleSupportDefinition,
        CleVersionSpecifier,
        Collection,
        CollectionBelongsToType,
        CollectionUpdateReason,
        CollectionUpdateReasonType,
        ComplianceDocumentType,
        Component,
        ComponentRef,
        ComponentReleaseWithCollection,
        DateTime,
        DiscoveryInfo,
        ErrorResponse,
        Identifier,
        IdentifierType,
        PaginatedCollectionResponse,
        PaginatedComponentReleaseResponse,
        PaginatedComponentResponse,
        PaginatedProductReleaseResponse,
        PaginatedProductResponse,
        PaginationDetails,
        Product,
        ProductRelease,
        Release,
        ReleaseDistribution,
        TeaServerInfo,
        UnknownErrorType,
        Uuid,
    )
    from .errors import BadRequestError, NotFoundError
    from . import (
        cle,
        tea_artifact,
        tea_component,
        tea_component_release,
        tea_discovery,
        tea_product,
        tea_product_release,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .tea_component import (
        GetReleasesByComponentIdRequestSortField,
        GetReleasesByComponentIdRequestSortOrder,
        QueryTeaComponentsRequestSortField,
        QueryTeaComponentsRequestSortOrder,
    )
    from .tea_component_release import (
        GetCollectionsByReleaseIdRequestSortField,
        GetCollectionsByReleaseIdRequestSortOrder,
        QueryTeaComponentReleasesRequestSortField,
        QueryTeaComponentReleasesRequestSortOrder,
    )
    from .tea_product import QueryTeaProductsRequestSortField, QueryTeaProductsRequestSortOrder
    from .tea_product_release import (
        GetCollectionsByProductReleaseIdRequestSortField,
        GetCollectionsByProductReleaseIdRequestSortOrder,
        GetReleasesByProductIdRequestSortField,
        GetReleasesByProductIdRequestSortOrder,
        QueryTeaProductReleasesRequestSortField,
        QueryTeaProductReleasesRequestSortOrder,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Artifact": ".types",
    "ArtifactFormat": ".types",
    "ArtifactType": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "Checksum": ".types",
    "ChecksumType": ".types",
    "Cle": ".types",
    "CleDefinitions": ".types",
    "CleEvent": ".types",
    "CleEventType": ".types",
    "CleSupportDefinition": ".types",
    "CleVersionSpecifier": ".types",
    "Collection": ".types",
    "CollectionBelongsToType": ".types",
    "CollectionUpdateReason": ".types",
    "CollectionUpdateReasonType": ".types",
    "ComplianceDocumentType": ".types",
    "Component": ".types",
    "ComponentRef": ".types",
    "ComponentReleaseWithCollection": ".types",
    "DateTime": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DiscoveryInfo": ".types",
    "ErrorResponse": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetCollectionsByProductReleaseIdRequestSortField": ".tea_product_release",
    "GetCollectionsByProductReleaseIdRequestSortOrder": ".tea_product_release",
    "GetCollectionsByReleaseIdRequestSortField": ".tea_component_release",
    "GetCollectionsByReleaseIdRequestSortOrder": ".tea_component_release",
    "GetReleasesByComponentIdRequestSortField": ".tea_component",
    "GetReleasesByComponentIdRequestSortOrder": ".tea_component",
    "GetReleasesByProductIdRequestSortField": ".tea_product_release",
    "GetReleasesByProductIdRequestSortOrder": ".tea_product_release",
    "Identifier": ".types",
    "IdentifierType": ".types",
    "NotFoundError": ".errors",
    "PaginatedCollectionResponse": ".types",
    "PaginatedComponentReleaseResponse": ".types",
    "PaginatedComponentResponse": ".types",
    "PaginatedProductReleaseResponse": ".types",
    "PaginatedProductResponse": ".types",
    "PaginationDetails": ".types",
    "Product": ".types",
    "ProductRelease": ".types",
    "QueryTeaComponentReleasesRequestSortField": ".tea_component_release",
    "QueryTeaComponentReleasesRequestSortOrder": ".tea_component_release",
    "QueryTeaComponentsRequestSortField": ".tea_component",
    "QueryTeaComponentsRequestSortOrder": ".tea_component",
    "QueryTeaProductReleasesRequestSortField": ".tea_product_release",
    "QueryTeaProductReleasesRequestSortOrder": ".tea_product_release",
    "QueryTeaProductsRequestSortField": ".tea_product",
    "QueryTeaProductsRequestSortOrder": ".tea_product",
    "Release": ".types",
    "ReleaseDistribution": ".types",
    "TeaServerInfo": ".types",
    "UnknownErrorType": ".types",
    "Uuid": ".types",
    "__version__": ".version",
    "cle": ".cle",
    "tea_artifact": ".tea_artifact",
    "tea_component": ".tea_component",
    "tea_component_release": ".tea_component_release",
    "tea_discovery": ".tea_discovery",
    "tea_product": ".tea_product",
    "tea_product_release": ".tea_product_release",
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
    "Artifact",
    "ArtifactFormat",
    "ArtifactType",
    "AsyncFernApi",
    "BadRequestError",
    "Checksum",
    "ChecksumType",
    "Cle",
    "CleDefinitions",
    "CleEvent",
    "CleEventType",
    "CleSupportDefinition",
    "CleVersionSpecifier",
    "Collection",
    "CollectionBelongsToType",
    "CollectionUpdateReason",
    "CollectionUpdateReasonType",
    "ComplianceDocumentType",
    "Component",
    "ComponentRef",
    "ComponentReleaseWithCollection",
    "DateTime",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DiscoveryInfo",
    "ErrorResponse",
    "FernApi",
    "FernApiEnvironment",
    "GetCollectionsByProductReleaseIdRequestSortField",
    "GetCollectionsByProductReleaseIdRequestSortOrder",
    "GetCollectionsByReleaseIdRequestSortField",
    "GetCollectionsByReleaseIdRequestSortOrder",
    "GetReleasesByComponentIdRequestSortField",
    "GetReleasesByComponentIdRequestSortOrder",
    "GetReleasesByProductIdRequestSortField",
    "GetReleasesByProductIdRequestSortOrder",
    "Identifier",
    "IdentifierType",
    "NotFoundError",
    "PaginatedCollectionResponse",
    "PaginatedComponentReleaseResponse",
    "PaginatedComponentResponse",
    "PaginatedProductReleaseResponse",
    "PaginatedProductResponse",
    "PaginationDetails",
    "Product",
    "ProductRelease",
    "QueryTeaComponentReleasesRequestSortField",
    "QueryTeaComponentReleasesRequestSortOrder",
    "QueryTeaComponentsRequestSortField",
    "QueryTeaComponentsRequestSortOrder",
    "QueryTeaProductReleasesRequestSortField",
    "QueryTeaProductReleasesRequestSortOrder",
    "QueryTeaProductsRequestSortField",
    "QueryTeaProductsRequestSortOrder",
    "Release",
    "ReleaseDistribution",
    "TeaServerInfo",
    "UnknownErrorType",
    "Uuid",
    "__version__",
    "cle",
    "tea_artifact",
    "tea_component",
    "tea_component_release",
    "tea_discovery",
    "tea_product",
    "tea_product_release",
]
