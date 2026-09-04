



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .artifact import Artifact
    from .artifact_format import ArtifactFormat
    from .artifact_type import ArtifactType
    from .checksum import Checksum
    from .checksum_type import ChecksumType
    from .cle import Cle
    from .cle_definitions import CleDefinitions
    from .cle_event import CleEvent
    from .cle_event_type import CleEventType
    from .cle_support_definition import CleSupportDefinition
    from .cle_version_specifier import CleVersionSpecifier
    from .collection import Collection
    from .collection_belongs_to_type import CollectionBelongsToType
    from .collection_update_reason import CollectionUpdateReason
    from .collection_update_reason_type import CollectionUpdateReasonType
    from .compliance_document_type import ComplianceDocumentType
    from .component import Component
    from .component_ref import ComponentRef
    from .component_release_with_collection import ComponentReleaseWithCollection
    from .date_time import DateTime
    from .discovery_info import DiscoveryInfo
    from .error_response import ErrorResponse
    from .identifier import Identifier
    from .identifier_type import IdentifierType
    from .paginated_collection_response import PaginatedCollectionResponse
    from .paginated_component_release_response import PaginatedComponentReleaseResponse
    from .paginated_component_response import PaginatedComponentResponse
    from .paginated_product_release_response import PaginatedProductReleaseResponse
    from .paginated_product_response import PaginatedProductResponse
    from .pagination_details import PaginationDetails
    from .product import Product
    from .product_release import ProductRelease
    from .release import Release
    from .release_distribution import ReleaseDistribution
    from .tea_server_info import TeaServerInfo
    from .unknown_error_type import UnknownErrorType
    from .uuid_ import Uuid
_dynamic_imports: typing.Dict[str, str] = {
    "Artifact": ".artifact",
    "ArtifactFormat": ".artifact_format",
    "ArtifactType": ".artifact_type",
    "Checksum": ".checksum",
    "ChecksumType": ".checksum_type",
    "Cle": ".cle",
    "CleDefinitions": ".cle_definitions",
    "CleEvent": ".cle_event",
    "CleEventType": ".cle_event_type",
    "CleSupportDefinition": ".cle_support_definition",
    "CleVersionSpecifier": ".cle_version_specifier",
    "Collection": ".collection",
    "CollectionBelongsToType": ".collection_belongs_to_type",
    "CollectionUpdateReason": ".collection_update_reason",
    "CollectionUpdateReasonType": ".collection_update_reason_type",
    "ComplianceDocumentType": ".compliance_document_type",
    "Component": ".component",
    "ComponentRef": ".component_ref",
    "ComponentReleaseWithCollection": ".component_release_with_collection",
    "DateTime": ".date_time",
    "DiscoveryInfo": ".discovery_info",
    "ErrorResponse": ".error_response",
    "Identifier": ".identifier",
    "IdentifierType": ".identifier_type",
    "PaginatedCollectionResponse": ".paginated_collection_response",
    "PaginatedComponentReleaseResponse": ".paginated_component_release_response",
    "PaginatedComponentResponse": ".paginated_component_response",
    "PaginatedProductReleaseResponse": ".paginated_product_release_response",
    "PaginatedProductResponse": ".paginated_product_response",
    "PaginationDetails": ".pagination_details",
    "Product": ".product",
    "ProductRelease": ".product_release",
    "Release": ".release",
    "ReleaseDistribution": ".release_distribution",
    "TeaServerInfo": ".tea_server_info",
    "UnknownErrorType": ".unknown_error_type",
    "Uuid": ".uuid_",
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
    "DiscoveryInfo",
    "ErrorResponse",
    "Identifier",
    "IdentifierType",
    "PaginatedCollectionResponse",
    "PaginatedComponentReleaseResponse",
    "PaginatedComponentResponse",
    "PaginatedProductReleaseResponse",
    "PaginatedProductResponse",
    "PaginationDetails",
    "Product",
    "ProductRelease",
    "Release",
    "ReleaseDistribution",
    "TeaServerInfo",
    "UnknownErrorType",
    "Uuid",
]
