



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .account import Account
    from .accounts_response_dto import AccountsResponseDto
    from .accounts_session_response_dto import AccountsSessionResponseDto
    from .aggregated_dto_item import AggregatedDtoItem
    from .artifact import Artifact
    from .artifact_dto_item import ArtifactDtoItem
    from .balance_response_dto import BalanceResponseDto
    from .common_settings import CommonSettings
    from .compare_documents_dto import CompareDocumentsDto
    from .compare_documents_dtov2 import CompareDocumentsDtov2
    from .compare_modules_dto import CompareModulesDto
    from .compare_policies_dto import ComparePoliciesDto
    from .compare_schemas_dto import CompareSchemasDto
    from .compare_tools_dto import CompareToolsDto
    from .contract import Contract
    from .contract_dto import ContractDto
    from .contract_dto_type import ContractDtoType
    from .credential_subject_dto import CredentialSubjectDto
    from .credentials import Credentials
    from .credentials_dto import CredentialsDto
    from .date import Date
    from .did_document_dto import DidDocumentDto
    from .did_document_status_dto import DidDocumentStatusDto
    from .did_key_dto import DidKeyDto
    from .did_key_status_dto import DidKeyStatusDto
    from .error import Error
    from .export_module import ExportModule
    from .export_policy import ExportPolicy
    from .export_schema import ExportSchema
    from .export_schema_dto import ExportSchemaDto
    from .filter_documents_dto import FilterDocumentsDto
    from .filter_modules_dto import FilterModulesDto
    from .filter_policies_dto import FilterPoliciesDto
    from .filter_schemas_dto import FilterSchemasDto
    from .filter_search_policies_dto import FilterSearchPoliciesDto
    from .filter_tools_dto import FilterToolsDto
    from .hedera_account import HederaAccount
    from .import_schema import ImportSchema
    from .import_schema_schemes_item import ImportSchemaSchemesItem
    from .internal_server_error_dto import InternalServerErrorDto
    from .log import Log
    from .message_schema_dto import MessageSchemaDto
    from .migration_config_dto import MigrationConfigDto
    from .migration_config_policies_dto import MigrationConfigPoliciesDto
    from .module import Module
    from .multi_policy_config import MultiPolicyConfig
    from .notification_dto import NotificationDto
    from .notification_dto_action import NotificationDtoAction
    from .notification_dto_type import NotificationDtoType
    from .object import Object
    from .policy_block import PolicyBlock
    from .policy_block_data import PolicyBlockData
    from .policy_category_dto import PolicyCategoryDto
    from .policy_config import PolicyConfig
    from .policy_config_policy_topics_item import PolicyConfigPolicyTopicsItem
    from .policy_dto import PolicyDto
    from .preview_module import PreviewModule
    from .preview_policy import PreviewPolicy
    from .profile_dto import ProfileDto
    from .progress_dto import ProgressDto
    from .progress_dto_type import ProgressDtoType
    from .project_dto import ProjectDto
    from .proof_dto import ProofDto
    from .properties_dto import PropertiesDto
    from .publish_module import PublishModule
    from .publish_policy import PublishPolicy
    from .record_action_dto import RecordActionDto
    from .record_status_dto import RecordStatusDto
    from .registered_users_dto import RegisteredUsersDto
    from .result_document_dto import ResultDocumentDto
    from .result_info_dto import ResultInfoDto
    from .retire_pool_dto import RetirePoolDto
    from .retire_pool_dto_tokens import RetirePoolDtoTokens
    from .retire_pool_dto_tokens_type import RetirePoolDtoTokensType
    from .retire_request import RetireRequest
    from .retire_request_dto import RetireRequestDto
    from .retire_request_dto_tokens import RetireRequestDtoTokens
    from .retire_request_dto_tokens_type import RetireRequestDtoTokensType
    from .running_details_dto import RunningDetailsDto
    from .running_result_dto import RunningResultDto
    from .schema import Schema
    from .schema_document import SchemaDocument
    from .schema_dto import SchemaDto
    from .search_policies_dto import SearchPoliciesDto
    from .session import Session
    from .settings_dto import SettingsDto
    from .subject_dto import SubjectDto
    from .suggestions_config_dto import SuggestionsConfigDto
    from .suggestions_config_item_dto import SuggestionsConfigItemDto
    from .suggestions_config_item_dto_type import SuggestionsConfigItemDtoType
    from .suggestions_output_dto import SuggestionsOutputDto
    from .system_schema_dto import SystemSchemaDto
    from .tag import Tag
    from .tag_entity import TagEntity
    from .tag_map import TagMap
    from .tag_map_entity import TagMapEntity
    from .tag_operation import TagOperation
    from .tag_status import TagStatus
    from .task import Task
    from .task_dto import TaskDto
    from .task_status import TaskStatus
    from .task_status_statuses_item import TaskStatusStatusesItem
    from .theme import Theme
    from .theme_rules_item import ThemeRulesItem
    from .theme_rules_item_border_width import ThemeRulesItemBorderWidth
    from .theme_rules_item_filter_type import ThemeRulesItemFilterType
    from .theme_rules_item_filter_value import ThemeRulesItemFilterValue
    from .theme_rules_item_shape import ThemeRulesItemShape
    from .token import Token
    from .token_info import TokenInfo
    from .tool_dto import ToolDto
    from .trust_chains import TrustChains
    from .trust_chains_chain_item import TrustChainsChainItem
    from .trust_chains_user_map_item import TrustChainsUserMapItem
    from .user import User
    from .user_dto import UserDto
    from .validate_module import ValidateModule
    from .validate_policy import ValidatePolicy
    from .vc_document_dto import VcDocumentDto
    from .verifiable_presentation import VerifiablePresentation
    from .version_schema_dto import VersionSchemaDto
    from .wiper_request_dto import WiperRequestDto
    from .wizard_config import WizardConfig
    from .wizard_config_policy import WizardConfigPolicy
    from .wizard_config_schemas_item import WizardConfigSchemasItem
    from .wizard_config_schemas_item_mint_options import WizardConfigSchemasItemMintOptions
    from .wizard_config_schemas_item_roles_config_item import WizardConfigSchemasItemRolesConfigItem
    from .wizard_config_schemas_item_roles_config_item_grid_columns_item import (
        WizardConfigSchemasItemRolesConfigItemGridColumnsItem,
    )
    from .wizard_config_trust_chain_item import WizardConfigTrustChainItem
_dynamic_imports: typing.Dict[str, str] = {
    "Account": ".account",
    "AccountsResponseDto": ".accounts_response_dto",
    "AccountsSessionResponseDto": ".accounts_session_response_dto",
    "AggregatedDtoItem": ".aggregated_dto_item",
    "Artifact": ".artifact",
    "ArtifactDtoItem": ".artifact_dto_item",
    "BalanceResponseDto": ".balance_response_dto",
    "CommonSettings": ".common_settings",
    "CompareDocumentsDto": ".compare_documents_dto",
    "CompareDocumentsDtov2": ".compare_documents_dtov2",
    "CompareModulesDto": ".compare_modules_dto",
    "ComparePoliciesDto": ".compare_policies_dto",
    "CompareSchemasDto": ".compare_schemas_dto",
    "CompareToolsDto": ".compare_tools_dto",
    "Contract": ".contract",
    "ContractDto": ".contract_dto",
    "ContractDtoType": ".contract_dto_type",
    "CredentialSubjectDto": ".credential_subject_dto",
    "Credentials": ".credentials",
    "CredentialsDto": ".credentials_dto",
    "Date": ".date",
    "DidDocumentDto": ".did_document_dto",
    "DidDocumentStatusDto": ".did_document_status_dto",
    "DidKeyDto": ".did_key_dto",
    "DidKeyStatusDto": ".did_key_status_dto",
    "Error": ".error",
    "ExportModule": ".export_module",
    "ExportPolicy": ".export_policy",
    "ExportSchema": ".export_schema",
    "ExportSchemaDto": ".export_schema_dto",
    "FilterDocumentsDto": ".filter_documents_dto",
    "FilterModulesDto": ".filter_modules_dto",
    "FilterPoliciesDto": ".filter_policies_dto",
    "FilterSchemasDto": ".filter_schemas_dto",
    "FilterSearchPoliciesDto": ".filter_search_policies_dto",
    "FilterToolsDto": ".filter_tools_dto",
    "HederaAccount": ".hedera_account",
    "ImportSchema": ".import_schema",
    "ImportSchemaSchemesItem": ".import_schema_schemes_item",
    "InternalServerErrorDto": ".internal_server_error_dto",
    "Log": ".log",
    "MessageSchemaDto": ".message_schema_dto",
    "MigrationConfigDto": ".migration_config_dto",
    "MigrationConfigPoliciesDto": ".migration_config_policies_dto",
    "Module": ".module",
    "MultiPolicyConfig": ".multi_policy_config",
    "NotificationDto": ".notification_dto",
    "NotificationDtoAction": ".notification_dto_action",
    "NotificationDtoType": ".notification_dto_type",
    "Object": ".object",
    "PolicyBlock": ".policy_block",
    "PolicyBlockData": ".policy_block_data",
    "PolicyCategoryDto": ".policy_category_dto",
    "PolicyConfig": ".policy_config",
    "PolicyConfigPolicyTopicsItem": ".policy_config_policy_topics_item",
    "PolicyDto": ".policy_dto",
    "PreviewModule": ".preview_module",
    "PreviewPolicy": ".preview_policy",
    "ProfileDto": ".profile_dto",
    "ProgressDto": ".progress_dto",
    "ProgressDtoType": ".progress_dto_type",
    "ProjectDto": ".project_dto",
    "ProofDto": ".proof_dto",
    "PropertiesDto": ".properties_dto",
    "PublishModule": ".publish_module",
    "PublishPolicy": ".publish_policy",
    "RecordActionDto": ".record_action_dto",
    "RecordStatusDto": ".record_status_dto",
    "RegisteredUsersDto": ".registered_users_dto",
    "ResultDocumentDto": ".result_document_dto",
    "ResultInfoDto": ".result_info_dto",
    "RetirePoolDto": ".retire_pool_dto",
    "RetirePoolDtoTokens": ".retire_pool_dto_tokens",
    "RetirePoolDtoTokensType": ".retire_pool_dto_tokens_type",
    "RetireRequest": ".retire_request",
    "RetireRequestDto": ".retire_request_dto",
    "RetireRequestDtoTokens": ".retire_request_dto_tokens",
    "RetireRequestDtoTokensType": ".retire_request_dto_tokens_type",
    "RunningDetailsDto": ".running_details_dto",
    "RunningResultDto": ".running_result_dto",
    "Schema": ".schema",
    "SchemaDocument": ".schema_document",
    "SchemaDto": ".schema_dto",
    "SearchPoliciesDto": ".search_policies_dto",
    "Session": ".session",
    "SettingsDto": ".settings_dto",
    "SubjectDto": ".subject_dto",
    "SuggestionsConfigDto": ".suggestions_config_dto",
    "SuggestionsConfigItemDto": ".suggestions_config_item_dto",
    "SuggestionsConfigItemDtoType": ".suggestions_config_item_dto_type",
    "SuggestionsOutputDto": ".suggestions_output_dto",
    "SystemSchemaDto": ".system_schema_dto",
    "Tag": ".tag",
    "TagEntity": ".tag_entity",
    "TagMap": ".tag_map",
    "TagMapEntity": ".tag_map_entity",
    "TagOperation": ".tag_operation",
    "TagStatus": ".tag_status",
    "Task": ".task",
    "TaskDto": ".task_dto",
    "TaskStatus": ".task_status",
    "TaskStatusStatusesItem": ".task_status_statuses_item",
    "Theme": ".theme",
    "ThemeRulesItem": ".theme_rules_item",
    "ThemeRulesItemBorderWidth": ".theme_rules_item_border_width",
    "ThemeRulesItemFilterType": ".theme_rules_item_filter_type",
    "ThemeRulesItemFilterValue": ".theme_rules_item_filter_value",
    "ThemeRulesItemShape": ".theme_rules_item_shape",
    "Token": ".token",
    "TokenInfo": ".token_info",
    "ToolDto": ".tool_dto",
    "TrustChains": ".trust_chains",
    "TrustChainsChainItem": ".trust_chains_chain_item",
    "TrustChainsUserMapItem": ".trust_chains_user_map_item",
    "User": ".user",
    "UserDto": ".user_dto",
    "ValidateModule": ".validate_module",
    "ValidatePolicy": ".validate_policy",
    "VcDocumentDto": ".vc_document_dto",
    "VerifiablePresentation": ".verifiable_presentation",
    "VersionSchemaDto": ".version_schema_dto",
    "WiperRequestDto": ".wiper_request_dto",
    "WizardConfig": ".wizard_config",
    "WizardConfigPolicy": ".wizard_config_policy",
    "WizardConfigSchemasItem": ".wizard_config_schemas_item",
    "WizardConfigSchemasItemMintOptions": ".wizard_config_schemas_item_mint_options",
    "WizardConfigSchemasItemRolesConfigItem": ".wizard_config_schemas_item_roles_config_item",
    "WizardConfigSchemasItemRolesConfigItemGridColumnsItem": ".wizard_config_schemas_item_roles_config_item_grid_columns_item",
    "WizardConfigTrustChainItem": ".wizard_config_trust_chain_item",
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
    "Account",
    "AccountsResponseDto",
    "AccountsSessionResponseDto",
    "AggregatedDtoItem",
    "Artifact",
    "ArtifactDtoItem",
    "BalanceResponseDto",
    "CommonSettings",
    "CompareDocumentsDto",
    "CompareDocumentsDtov2",
    "CompareModulesDto",
    "ComparePoliciesDto",
    "CompareSchemasDto",
    "CompareToolsDto",
    "Contract",
    "ContractDto",
    "ContractDtoType",
    "CredentialSubjectDto",
    "Credentials",
    "CredentialsDto",
    "Date",
    "DidDocumentDto",
    "DidDocumentStatusDto",
    "DidKeyDto",
    "DidKeyStatusDto",
    "Error",
    "ExportModule",
    "ExportPolicy",
    "ExportSchema",
    "ExportSchemaDto",
    "FilterDocumentsDto",
    "FilterModulesDto",
    "FilterPoliciesDto",
    "FilterSchemasDto",
    "FilterSearchPoliciesDto",
    "FilterToolsDto",
    "HederaAccount",
    "ImportSchema",
    "ImportSchemaSchemesItem",
    "InternalServerErrorDto",
    "Log",
    "MessageSchemaDto",
    "MigrationConfigDto",
    "MigrationConfigPoliciesDto",
    "Module",
    "MultiPolicyConfig",
    "NotificationDto",
    "NotificationDtoAction",
    "NotificationDtoType",
    "Object",
    "PolicyBlock",
    "PolicyBlockData",
    "PolicyCategoryDto",
    "PolicyConfig",
    "PolicyConfigPolicyTopicsItem",
    "PolicyDto",
    "PreviewModule",
    "PreviewPolicy",
    "ProfileDto",
    "ProgressDto",
    "ProgressDtoType",
    "ProjectDto",
    "ProofDto",
    "PropertiesDto",
    "PublishModule",
    "PublishPolicy",
    "RecordActionDto",
    "RecordStatusDto",
    "RegisteredUsersDto",
    "ResultDocumentDto",
    "ResultInfoDto",
    "RetirePoolDto",
    "RetirePoolDtoTokens",
    "RetirePoolDtoTokensType",
    "RetireRequest",
    "RetireRequestDto",
    "RetireRequestDtoTokens",
    "RetireRequestDtoTokensType",
    "RunningDetailsDto",
    "RunningResultDto",
    "Schema",
    "SchemaDocument",
    "SchemaDto",
    "SearchPoliciesDto",
    "Session",
    "SettingsDto",
    "SubjectDto",
    "SuggestionsConfigDto",
    "SuggestionsConfigItemDto",
    "SuggestionsConfigItemDtoType",
    "SuggestionsOutputDto",
    "SystemSchemaDto",
    "Tag",
    "TagEntity",
    "TagMap",
    "TagMapEntity",
    "TagOperation",
    "TagStatus",
    "Task",
    "TaskDto",
    "TaskStatus",
    "TaskStatusStatusesItem",
    "Theme",
    "ThemeRulesItem",
    "ThemeRulesItemBorderWidth",
    "ThemeRulesItemFilterType",
    "ThemeRulesItemFilterValue",
    "ThemeRulesItemShape",
    "Token",
    "TokenInfo",
    "ToolDto",
    "TrustChains",
    "TrustChainsChainItem",
    "TrustChainsUserMapItem",
    "User",
    "UserDto",
    "ValidateModule",
    "ValidatePolicy",
    "VcDocumentDto",
    "VerifiablePresentation",
    "VersionSchemaDto",
    "WiperRequestDto",
    "WizardConfig",
    "WizardConfigPolicy",
    "WizardConfigSchemasItem",
    "WizardConfigSchemasItemMintOptions",
    "WizardConfigSchemasItemRolesConfigItem",
    "WizardConfigSchemasItemRolesConfigItemGridColumnsItem",
    "WizardConfigTrustChainItem",
]
