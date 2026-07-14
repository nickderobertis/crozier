



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .artifact_description import ArtifactDescription
    from .artifact_id import ArtifactId
    from .artifact_meta_data import ArtifactMetaData
    from .artifact_name import ArtifactName
    from .artifact_owner import ArtifactOwner
    from .artifact_reference import ArtifactReference
    from .artifact_search_results import ArtifactSearchResults
    from .artifact_state import ArtifactState
    from .artifact_type import ArtifactType
    from .artifact_type_info import ArtifactTypeInfo
    from .configuration_property import ConfigurationProperty
    from .content_create_request import ContentCreateRequest
    from .download_ref import DownloadRef
    from .editable_meta_data import EditableMetaData
    from .encoded_artifact_description import EncodedArtifactDescription
    from .encoded_artifact_name import EncodedArtifactName
    from .error import Error
    from .file_content import FileContent
    from .group_id import GroupId
    from .group_meta_data import GroupMetaData
    from .group_search_results import GroupSearchResults
    from .if_exists import IfExists
    from .limits import Limits
    from .log_configuration import LogConfiguration
    from .log_level import LogLevel
    from .named_log_configuration import NamedLogConfiguration
    from .properties import Properties
    from .role_mapping import RoleMapping
    from .role_type import RoleType
    from .rule import Rule
    from .rule_type import RuleType
    from .rule_violation_cause import RuleViolationCause
    from .rule_violation_error import RuleViolationError
    from .searched_artifact import SearchedArtifact
    from .searched_group import SearchedGroup
    from .searched_version import SearchedVersion
    from .sort_by import SortBy
    from .sort_order import SortOrder
    from .system_info import SystemInfo
    from .update_state import UpdateState
    from .user_info import UserInfo
    from .version import Version
    from .version_meta_data import VersionMetaData
    from .version_search_results import VersionSearchResults
_dynamic_imports: typing.Dict[str, str] = {
    "ArtifactDescription": ".artifact_description",
    "ArtifactId": ".artifact_id",
    "ArtifactMetaData": ".artifact_meta_data",
    "ArtifactName": ".artifact_name",
    "ArtifactOwner": ".artifact_owner",
    "ArtifactReference": ".artifact_reference",
    "ArtifactSearchResults": ".artifact_search_results",
    "ArtifactState": ".artifact_state",
    "ArtifactType": ".artifact_type",
    "ArtifactTypeInfo": ".artifact_type_info",
    "ConfigurationProperty": ".configuration_property",
    "ContentCreateRequest": ".content_create_request",
    "DownloadRef": ".download_ref",
    "EditableMetaData": ".editable_meta_data",
    "EncodedArtifactDescription": ".encoded_artifact_description",
    "EncodedArtifactName": ".encoded_artifact_name",
    "Error": ".error",
    "FileContent": ".file_content",
    "GroupId": ".group_id",
    "GroupMetaData": ".group_meta_data",
    "GroupSearchResults": ".group_search_results",
    "IfExists": ".if_exists",
    "Limits": ".limits",
    "LogConfiguration": ".log_configuration",
    "LogLevel": ".log_level",
    "NamedLogConfiguration": ".named_log_configuration",
    "Properties": ".properties",
    "RoleMapping": ".role_mapping",
    "RoleType": ".role_type",
    "Rule": ".rule",
    "RuleType": ".rule_type",
    "RuleViolationCause": ".rule_violation_cause",
    "RuleViolationError": ".rule_violation_error",
    "SearchedArtifact": ".searched_artifact",
    "SearchedGroup": ".searched_group",
    "SearchedVersion": ".searched_version",
    "SortBy": ".sort_by",
    "SortOrder": ".sort_order",
    "SystemInfo": ".system_info",
    "UpdateState": ".update_state",
    "UserInfo": ".user_info",
    "Version": ".version",
    "VersionMetaData": ".version_meta_data",
    "VersionSearchResults": ".version_search_results",
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
    "ArtifactDescription",
    "ArtifactId",
    "ArtifactMetaData",
    "ArtifactName",
    "ArtifactOwner",
    "ArtifactReference",
    "ArtifactSearchResults",
    "ArtifactState",
    "ArtifactType",
    "ArtifactTypeInfo",
    "ConfigurationProperty",
    "ContentCreateRequest",
    "DownloadRef",
    "EditableMetaData",
    "EncodedArtifactDescription",
    "EncodedArtifactName",
    "Error",
    "FileContent",
    "GroupId",
    "GroupMetaData",
    "GroupSearchResults",
    "IfExists",
    "Limits",
    "LogConfiguration",
    "LogLevel",
    "NamedLogConfiguration",
    "Properties",
    "RoleMapping",
    "RoleType",
    "Rule",
    "RuleType",
    "RuleViolationCause",
    "RuleViolationError",
    "SearchedArtifact",
    "SearchedGroup",
    "SearchedVersion",
    "SortBy",
    "SortOrder",
    "SystemInfo",
    "UpdateState",
    "UserInfo",
    "Version",
    "VersionMetaData",
    "VersionSearchResults",
]
