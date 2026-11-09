



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .capabilities import Capabilities
    from .capabilities_extensions import CapabilitiesExtensions
    from .capabilities_tombstone_policy import CapabilitiesTombstonePolicy
    from .conflict_error_body import ConflictErrorBody
    from .conflict_error_body_error import ConflictErrorBodyError
    from .conflict_error_body_error_code import ConflictErrorBodyErrorCode
    from .deposit import Deposit
    from .deposit_capability import DepositCapability
    from .deposit_capability_file_upload_item import DepositCapabilityFileUploadItem
    from .deposit_capability_id_minting import DepositCapabilityIdMinting
    from .deposit_errors_item import DepositErrorsItem
    from .deposit_state import DepositState
    from .entity import Entity
    from .entity_access import EntityAccess
    from .entity_reference import EntityReference
    from .entity_type import EntityType
    from .facet_capability import FacetCapability
    from .file import File
    from .file_access import FileAccess
    from .file_upload_target import FileUploadTarget
    from .filter_capability import FilterCapability
    from .filter_capability_type import FilterCapabilityType
    from .filter_range import FilterRange
    from .filter_range_gte import FilterRangeGte
    from .filter_range_lte import FilterRangeLte
    from .forbidden_error_body import ForbiddenErrorBody
    from .forbidden_error_body_error import ForbiddenErrorBodyError
    from .forbidden_error_body_error_code import ForbiddenErrorBodyErrorCode
    from .id import Id
    from .internal_server_error_body import InternalServerErrorBody
    from .internal_server_error_body_error import InternalServerErrorBodyError
    from .internal_server_error_body_error_code import InternalServerErrorBodyErrorCode
    from .invalid_entity_type_error import InvalidEntityTypeError
    from .invalid_entity_type_error_error import InvalidEntityTypeErrorError
    from .invalid_entity_type_error_error_code import InvalidEntityTypeErrorErrorCode
    from .invalid_entity_type_error_error_details import InvalidEntityTypeErrorErrorDetails
    from .not_found_error_body import NotFoundErrorBody
    from .not_found_error_body_error import NotFoundErrorBodyError
    from .not_found_error_body_error_code import NotFoundErrorBodyErrorCode
    from .oauth_scope import OauthScope
    from .order import Order
    from .page_segment import PageSegment
    from .range_not_satisfiable_error_body import RangeNotSatisfiableErrorBody
    from .range_not_satisfiable_error_body_error import RangeNotSatisfiableErrorBodyError
    from .range_not_satisfiable_error_body_error_code import RangeNotSatisfiableErrorBodyErrorCode
    from .rate_limit_error import RateLimitError
    from .rate_limit_error_error import RateLimitErrorError
    from .rate_limit_error_error_code import RateLimitErrorErrorCode
    from .rate_limit_error_error_details import RateLimitErrorErrorDetails
    from .ro_crate import RoCrate
    from .ro_crate_access import RoCrateAccess
    from .search_capability import SearchCapability
    from .search_entity import SearchEntity
    from .search_entity_search_extra import SearchEntitySearchExtra
    from .segment import Segment, Segment_Page, Segment_TimeAlignedAnnotation
    from .segments_capability import SegmentsCapability
    from .staged_file import StagedFile
    from .staged_file_status import StagedFileStatus
    from .time_aligned_annotation_segment import TimeAlignedAnnotationSegment
    from .tombstone import Tombstone
    from .tombstone_resource_type import TombstoneResourceType
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .unauthorized_error_body_error import UnauthorizedErrorBodyError
    from .unauthorized_error_body_error_code import UnauthorizedErrorBodyErrorCode
    from .validation_error import ValidationError
    from .validation_error_error import ValidationErrorError
    from .validation_error_error_code import ValidationErrorErrorCode
    from .validation_error_error_details import ValidationErrorErrorDetails
    from .validation_error_error_details_violations_item import ValidationErrorErrorDetailsViolationsItem
_dynamic_imports: typing.Dict[str, str] = {
    "Capabilities": ".capabilities",
    "CapabilitiesExtensions": ".capabilities_extensions",
    "CapabilitiesTombstonePolicy": ".capabilities_tombstone_policy",
    "ConflictErrorBody": ".conflict_error_body",
    "ConflictErrorBodyError": ".conflict_error_body_error",
    "ConflictErrorBodyErrorCode": ".conflict_error_body_error_code",
    "Deposit": ".deposit",
    "DepositCapability": ".deposit_capability",
    "DepositCapabilityFileUploadItem": ".deposit_capability_file_upload_item",
    "DepositCapabilityIdMinting": ".deposit_capability_id_minting",
    "DepositErrorsItem": ".deposit_errors_item",
    "DepositState": ".deposit_state",
    "Entity": ".entity",
    "EntityAccess": ".entity_access",
    "EntityReference": ".entity_reference",
    "EntityType": ".entity_type",
    "FacetCapability": ".facet_capability",
    "File": ".file",
    "FileAccess": ".file_access",
    "FileUploadTarget": ".file_upload_target",
    "FilterCapability": ".filter_capability",
    "FilterCapabilityType": ".filter_capability_type",
    "FilterRange": ".filter_range",
    "FilterRangeGte": ".filter_range_gte",
    "FilterRangeLte": ".filter_range_lte",
    "ForbiddenErrorBody": ".forbidden_error_body",
    "ForbiddenErrorBodyError": ".forbidden_error_body_error",
    "ForbiddenErrorBodyErrorCode": ".forbidden_error_body_error_code",
    "Id": ".id",
    "InternalServerErrorBody": ".internal_server_error_body",
    "InternalServerErrorBodyError": ".internal_server_error_body_error",
    "InternalServerErrorBodyErrorCode": ".internal_server_error_body_error_code",
    "InvalidEntityTypeError": ".invalid_entity_type_error",
    "InvalidEntityTypeErrorError": ".invalid_entity_type_error_error",
    "InvalidEntityTypeErrorErrorCode": ".invalid_entity_type_error_error_code",
    "InvalidEntityTypeErrorErrorDetails": ".invalid_entity_type_error_error_details",
    "NotFoundErrorBody": ".not_found_error_body",
    "NotFoundErrorBodyError": ".not_found_error_body_error",
    "NotFoundErrorBodyErrorCode": ".not_found_error_body_error_code",
    "OauthScope": ".oauth_scope",
    "Order": ".order",
    "PageSegment": ".page_segment",
    "RangeNotSatisfiableErrorBody": ".range_not_satisfiable_error_body",
    "RangeNotSatisfiableErrorBodyError": ".range_not_satisfiable_error_body_error",
    "RangeNotSatisfiableErrorBodyErrorCode": ".range_not_satisfiable_error_body_error_code",
    "RateLimitError": ".rate_limit_error",
    "RateLimitErrorError": ".rate_limit_error_error",
    "RateLimitErrorErrorCode": ".rate_limit_error_error_code",
    "RateLimitErrorErrorDetails": ".rate_limit_error_error_details",
    "RoCrate": ".ro_crate",
    "RoCrateAccess": ".ro_crate_access",
    "SearchCapability": ".search_capability",
    "SearchEntity": ".search_entity",
    "SearchEntitySearchExtra": ".search_entity_search_extra",
    "Segment": ".segment",
    "Segment_Page": ".segment",
    "Segment_TimeAlignedAnnotation": ".segment",
    "SegmentsCapability": ".segments_capability",
    "StagedFile": ".staged_file",
    "StagedFileStatus": ".staged_file_status",
    "TimeAlignedAnnotationSegment": ".time_aligned_annotation_segment",
    "Tombstone": ".tombstone",
    "TombstoneResourceType": ".tombstone_resource_type",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "UnauthorizedErrorBodyError": ".unauthorized_error_body_error",
    "UnauthorizedErrorBodyErrorCode": ".unauthorized_error_body_error_code",
    "ValidationError": ".validation_error",
    "ValidationErrorError": ".validation_error_error",
    "ValidationErrorErrorCode": ".validation_error_error_code",
    "ValidationErrorErrorDetails": ".validation_error_error_details",
    "ValidationErrorErrorDetailsViolationsItem": ".validation_error_error_details_violations_item",
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
    "Capabilities",
    "CapabilitiesExtensions",
    "CapabilitiesTombstonePolicy",
    "ConflictErrorBody",
    "ConflictErrorBodyError",
    "ConflictErrorBodyErrorCode",
    "Deposit",
    "DepositCapability",
    "DepositCapabilityFileUploadItem",
    "DepositCapabilityIdMinting",
    "DepositErrorsItem",
    "DepositState",
    "Entity",
    "EntityAccess",
    "EntityReference",
    "EntityType",
    "FacetCapability",
    "File",
    "FileAccess",
    "FileUploadTarget",
    "FilterCapability",
    "FilterCapabilityType",
    "FilterRange",
    "FilterRangeGte",
    "FilterRangeLte",
    "ForbiddenErrorBody",
    "ForbiddenErrorBodyError",
    "ForbiddenErrorBodyErrorCode",
    "Id",
    "InternalServerErrorBody",
    "InternalServerErrorBodyError",
    "InternalServerErrorBodyErrorCode",
    "InvalidEntityTypeError",
    "InvalidEntityTypeErrorError",
    "InvalidEntityTypeErrorErrorCode",
    "InvalidEntityTypeErrorErrorDetails",
    "NotFoundErrorBody",
    "NotFoundErrorBodyError",
    "NotFoundErrorBodyErrorCode",
    "OauthScope",
    "Order",
    "PageSegment",
    "RangeNotSatisfiableErrorBody",
    "RangeNotSatisfiableErrorBodyError",
    "RangeNotSatisfiableErrorBodyErrorCode",
    "RateLimitError",
    "RateLimitErrorError",
    "RateLimitErrorErrorCode",
    "RateLimitErrorErrorDetails",
    "RoCrate",
    "RoCrateAccess",
    "SearchCapability",
    "SearchEntity",
    "SearchEntitySearchExtra",
    "Segment",
    "Segment_Page",
    "Segment_TimeAlignedAnnotation",
    "SegmentsCapability",
    "StagedFile",
    "StagedFileStatus",
    "TimeAlignedAnnotationSegment",
    "Tombstone",
    "TombstoneResourceType",
    "UnauthorizedErrorBody",
    "UnauthorizedErrorBodyError",
    "UnauthorizedErrorBodyErrorCode",
    "ValidationError",
    "ValidationErrorError",
    "ValidationErrorErrorCode",
    "ValidationErrorErrorDetails",
    "ValidationErrorErrorDetailsViolationsItem",
]
