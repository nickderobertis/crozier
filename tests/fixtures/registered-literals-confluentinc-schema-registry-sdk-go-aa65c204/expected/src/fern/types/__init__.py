



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .atlas_attribute_def import AtlasAttributeDef
    from .atlas_attribute_def_cardinality import AtlasAttributeDefCardinality
    from .atlas_attribute_def_index_type import AtlasAttributeDefIndexType
    from .atlas_business_metadata_def import AtlasBusinessMetadataDef
    from .atlas_business_metadata_def_category import AtlasBusinessMetadataDefCategory
    from .atlas_classification import AtlasClassification
    from .atlas_classification_entity_status import AtlasClassificationEntityStatus
    from .atlas_constraint_def import AtlasConstraintDef
    from .atlas_entity import AtlasEntity
    from .atlas_entity_header import AtlasEntityHeader
    from .atlas_entity_header_status import AtlasEntityHeaderStatus
    from .atlas_entity_status import AtlasEntityStatus
    from .atlas_entity_with_ext_info import AtlasEntityWithExtInfo
    from .atlas_term_assignment_header import AtlasTermAssignmentHeader
    from .atlas_term_assignment_header_status import AtlasTermAssignmentHeaderStatus
    from .business_metadata import BusinessMetadata
    from .business_metadata_def_response import BusinessMetadataDefResponse
    from .business_metadata_def_response_category import BusinessMetadataDefResponseCategory
    from .business_metadata_response import BusinessMetadataResponse
    from .compatibility_check_response import CompatibilityCheckResponse
    from .config import Config
    from .config_compatibility_level import ConfigCompatibilityLevel
    from .config_update_request import ConfigUpdateRequest
    from .config_update_request_compatibility import ConfigUpdateRequestCompatibility
    from .create_dek_request import CreateDekRequest
    from .create_dek_request_algorithm import CreateDekRequestAlgorithm
    from .create_exporter_request import CreateExporterRequest
    from .create_exporter_request_context_type import CreateExporterRequestContextType
    from .create_exporter_response import CreateExporterResponse
    from .create_kek_request import CreateKekRequest
    from .dek import Dek
    from .dek_algorithm import DekAlgorithm
    from .delete_dek_version_request_algorithm import DeleteDekVersionRequestAlgorithm
    from .delete_dek_versions_request_algorithm import DeleteDekVersionsRequestAlgorithm
    from .delete_mode_response import DeleteModeResponse
    from .delete_subject_config_response import DeleteSubjectConfigResponse
    from .delete_subject_mode_response import DeleteSubjectModeResponse
    from .delete_top_level_config_response import DeleteTopLevelConfigResponse
    from .error_message import ErrorMessage
    from .exporter_info import ExporterInfo
    from .exporter_info_context_type import ExporterInfoContextType
    from .exporter_status import ExporterStatus
    from .exporter_status_state import ExporterStatusState
    from .get_dek_by_version_request_algorithm import GetDekByVersionRequestAlgorithm
    from .get_dek_request_algorithm import GetDekRequestAlgorithm
    from .get_dek_versions_request_algorithm import GetDekVersionsRequestAlgorithm
    from .get_response_value import GetResponseValue
    from .kek import Kek
    from .metadata import Metadata
    from .mode import Mode
    from .mode_update_request import ModeUpdateRequest
    from .register_schema_request import RegisterSchemaRequest
    from .register_schema_response import RegisterSchemaResponse
    from .rule import Rule
    from .rule_kind import RuleKind
    from .rule_mode import RuleMode
    from .rule_set import RuleSet
    from .rule_set_enable_at import RuleSetEnableAt
    from .schema import Schema
    from .schema_entity import SchemaEntity
    from .schema_entity_entity_type import SchemaEntityEntityType
    from .schema_reference import SchemaReference
    from .schema_registry import SchemaRegistry
    from .schema_string import SchemaString
    from .schema_tags import SchemaTags
    from .search_params import SearchParams
    from .search_result import SearchResult
    from .search_using_attribute_request_sort_order import SearchUsingAttributeRequestSortOrder
    from .search_using_attribute_request_time_range_type import SearchUsingAttributeRequestTimeRangeType
    from .search_using_basic_request_sort_order import SearchUsingBasicRequestSortOrder
    from .search_using_basic_request_time_range_type import SearchUsingBasicRequestTimeRangeType
    from .server_cluster_id import ServerClusterId
    from .server_cluster_id_scope_value import ServerClusterIdScopeValue
    from .subject_version import SubjectVersion
    from .tag import Tag
    from .tag_def import TagDef
    from .tag_def_category import TagDefCategory
    from .tag_def_response import TagDefResponse
    from .tag_def_response_category import TagDefResponseCategory
    from .tag_entity_status import TagEntityStatus
    from .tag_response import TagResponse
    from .tag_response_entity_status import TagResponseEntityStatus
    from .time_boundary import TimeBoundary
    from .undelete_dek_version_request_algorithm import UndeleteDekVersionRequestAlgorithm
    from .undelete_dek_versions_request_algorithm import UndeleteDekVersionsRequestAlgorithm
    from .update_exporter_request import UpdateExporterRequest
    from .update_exporter_request_context_type import UpdateExporterRequestContextType
    from .update_exporter_response import UpdateExporterResponse
    from .update_kek_request import UpdateKekRequest
_dynamic_imports: typing.Dict[str, str] = {
    "AtlasAttributeDef": ".atlas_attribute_def",
    "AtlasAttributeDefCardinality": ".atlas_attribute_def_cardinality",
    "AtlasAttributeDefIndexType": ".atlas_attribute_def_index_type",
    "AtlasBusinessMetadataDef": ".atlas_business_metadata_def",
    "AtlasBusinessMetadataDefCategory": ".atlas_business_metadata_def_category",
    "AtlasClassification": ".atlas_classification",
    "AtlasClassificationEntityStatus": ".atlas_classification_entity_status",
    "AtlasConstraintDef": ".atlas_constraint_def",
    "AtlasEntity": ".atlas_entity",
    "AtlasEntityHeader": ".atlas_entity_header",
    "AtlasEntityHeaderStatus": ".atlas_entity_header_status",
    "AtlasEntityStatus": ".atlas_entity_status",
    "AtlasEntityWithExtInfo": ".atlas_entity_with_ext_info",
    "AtlasTermAssignmentHeader": ".atlas_term_assignment_header",
    "AtlasTermAssignmentHeaderStatus": ".atlas_term_assignment_header_status",
    "BusinessMetadata": ".business_metadata",
    "BusinessMetadataDefResponse": ".business_metadata_def_response",
    "BusinessMetadataDefResponseCategory": ".business_metadata_def_response_category",
    "BusinessMetadataResponse": ".business_metadata_response",
    "CompatibilityCheckResponse": ".compatibility_check_response",
    "Config": ".config",
    "ConfigCompatibilityLevel": ".config_compatibility_level",
    "ConfigUpdateRequest": ".config_update_request",
    "ConfigUpdateRequestCompatibility": ".config_update_request_compatibility",
    "CreateDekRequest": ".create_dek_request",
    "CreateDekRequestAlgorithm": ".create_dek_request_algorithm",
    "CreateExporterRequest": ".create_exporter_request",
    "CreateExporterRequestContextType": ".create_exporter_request_context_type",
    "CreateExporterResponse": ".create_exporter_response",
    "CreateKekRequest": ".create_kek_request",
    "Dek": ".dek",
    "DekAlgorithm": ".dek_algorithm",
    "DeleteDekVersionRequestAlgorithm": ".delete_dek_version_request_algorithm",
    "DeleteDekVersionsRequestAlgorithm": ".delete_dek_versions_request_algorithm",
    "DeleteModeResponse": ".delete_mode_response",
    "DeleteSubjectConfigResponse": ".delete_subject_config_response",
    "DeleteSubjectModeResponse": ".delete_subject_mode_response",
    "DeleteTopLevelConfigResponse": ".delete_top_level_config_response",
    "ErrorMessage": ".error_message",
    "ExporterInfo": ".exporter_info",
    "ExporterInfoContextType": ".exporter_info_context_type",
    "ExporterStatus": ".exporter_status",
    "ExporterStatusState": ".exporter_status_state",
    "GetDekByVersionRequestAlgorithm": ".get_dek_by_version_request_algorithm",
    "GetDekRequestAlgorithm": ".get_dek_request_algorithm",
    "GetDekVersionsRequestAlgorithm": ".get_dek_versions_request_algorithm",
    "GetResponseValue": ".get_response_value",
    "Kek": ".kek",
    "Metadata": ".metadata",
    "Mode": ".mode",
    "ModeUpdateRequest": ".mode_update_request",
    "RegisterSchemaRequest": ".register_schema_request",
    "RegisterSchemaResponse": ".register_schema_response",
    "Rule": ".rule",
    "RuleKind": ".rule_kind",
    "RuleMode": ".rule_mode",
    "RuleSet": ".rule_set",
    "RuleSetEnableAt": ".rule_set_enable_at",
    "Schema": ".schema",
    "SchemaEntity": ".schema_entity",
    "SchemaEntityEntityType": ".schema_entity_entity_type",
    "SchemaReference": ".schema_reference",
    "SchemaRegistry": ".schema_registry",
    "SchemaString": ".schema_string",
    "SchemaTags": ".schema_tags",
    "SearchParams": ".search_params",
    "SearchResult": ".search_result",
    "SearchUsingAttributeRequestSortOrder": ".search_using_attribute_request_sort_order",
    "SearchUsingAttributeRequestTimeRangeType": ".search_using_attribute_request_time_range_type",
    "SearchUsingBasicRequestSortOrder": ".search_using_basic_request_sort_order",
    "SearchUsingBasicRequestTimeRangeType": ".search_using_basic_request_time_range_type",
    "ServerClusterId": ".server_cluster_id",
    "ServerClusterIdScopeValue": ".server_cluster_id_scope_value",
    "SubjectVersion": ".subject_version",
    "Tag": ".tag",
    "TagDef": ".tag_def",
    "TagDefCategory": ".tag_def_category",
    "TagDefResponse": ".tag_def_response",
    "TagDefResponseCategory": ".tag_def_response_category",
    "TagEntityStatus": ".tag_entity_status",
    "TagResponse": ".tag_response",
    "TagResponseEntityStatus": ".tag_response_entity_status",
    "TimeBoundary": ".time_boundary",
    "UndeleteDekVersionRequestAlgorithm": ".undelete_dek_version_request_algorithm",
    "UndeleteDekVersionsRequestAlgorithm": ".undelete_dek_versions_request_algorithm",
    "UpdateExporterRequest": ".update_exporter_request",
    "UpdateExporterRequestContextType": ".update_exporter_request_context_type",
    "UpdateExporterResponse": ".update_exporter_response",
    "UpdateKekRequest": ".update_kek_request",
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
    "AtlasAttributeDef",
    "AtlasAttributeDefCardinality",
    "AtlasAttributeDefIndexType",
    "AtlasBusinessMetadataDef",
    "AtlasBusinessMetadataDefCategory",
    "AtlasClassification",
    "AtlasClassificationEntityStatus",
    "AtlasConstraintDef",
    "AtlasEntity",
    "AtlasEntityHeader",
    "AtlasEntityHeaderStatus",
    "AtlasEntityStatus",
    "AtlasEntityWithExtInfo",
    "AtlasTermAssignmentHeader",
    "AtlasTermAssignmentHeaderStatus",
    "BusinessMetadata",
    "BusinessMetadataDefResponse",
    "BusinessMetadataDefResponseCategory",
    "BusinessMetadataResponse",
    "CompatibilityCheckResponse",
    "Config",
    "ConfigCompatibilityLevel",
    "ConfigUpdateRequest",
    "ConfigUpdateRequestCompatibility",
    "CreateDekRequest",
    "CreateDekRequestAlgorithm",
    "CreateExporterRequest",
    "CreateExporterRequestContextType",
    "CreateExporterResponse",
    "CreateKekRequest",
    "Dek",
    "DekAlgorithm",
    "DeleteDekVersionRequestAlgorithm",
    "DeleteDekVersionsRequestAlgorithm",
    "DeleteModeResponse",
    "DeleteSubjectConfigResponse",
    "DeleteSubjectModeResponse",
    "DeleteTopLevelConfigResponse",
    "ErrorMessage",
    "ExporterInfo",
    "ExporterInfoContextType",
    "ExporterStatus",
    "ExporterStatusState",
    "GetDekByVersionRequestAlgorithm",
    "GetDekRequestAlgorithm",
    "GetDekVersionsRequestAlgorithm",
    "GetResponseValue",
    "Kek",
    "Metadata",
    "Mode",
    "ModeUpdateRequest",
    "RegisterSchemaRequest",
    "RegisterSchemaResponse",
    "Rule",
    "RuleKind",
    "RuleMode",
    "RuleSet",
    "RuleSetEnableAt",
    "Schema",
    "SchemaEntity",
    "SchemaEntityEntityType",
    "SchemaReference",
    "SchemaRegistry",
    "SchemaString",
    "SchemaTags",
    "SearchParams",
    "SearchResult",
    "SearchUsingAttributeRequestSortOrder",
    "SearchUsingAttributeRequestTimeRangeType",
    "SearchUsingBasicRequestSortOrder",
    "SearchUsingBasicRequestTimeRangeType",
    "ServerClusterId",
    "ServerClusterIdScopeValue",
    "SubjectVersion",
    "Tag",
    "TagDef",
    "TagDefCategory",
    "TagDefResponse",
    "TagDefResponseCategory",
    "TagEntityStatus",
    "TagResponse",
    "TagResponseEntityStatus",
    "TimeBoundary",
    "UndeleteDekVersionRequestAlgorithm",
    "UndeleteDekVersionsRequestAlgorithm",
    "UpdateExporterRequest",
    "UpdateExporterRequestContextType",
    "UpdateExporterResponse",
    "UpdateKekRequest",
]
