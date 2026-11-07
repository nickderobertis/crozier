



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .after_date import AfterDate
    from .attribute_definition import AttributeDefinition
    from .attribute_filter import AttributeFilter
    from .before_date import BeforeDate
    from .build_info import BuildInfo
    from .ccdl import Ccdl
    from .codeable_concept_bulk_search_result import CodeableConceptBulkSearchResult
    from .codeable_concept_entry import CodeableConceptEntry
    from .codeable_concept_search_result import CodeableConceptSearchResult
    from .contextualized_term_code import ContextualizedTermCode
    from .contextualized_term_code_list import ContextualizedTermCodeList
    from .criteria_profile_data import CriteriaProfileData
    from .criterion import Criterion
    from .criterion_list import CriterionList
    from .crtdl import Crtdl
    from .data_extraction_query import DataExtractionQuery
    from .data_extraction_query_attribute_groups_item import DataExtractionQueryAttributeGroupsItem
    from .data_extraction_query_attribute_groups_item_attributes_item import (
        DataExtractionQueryAttributeGroupsItemAttributesItem,
    )
    from .data_extraction_query_attribute_groups_item_filter_item import (
        DataExtractionQueryAttributeGroupsItemFilterItem,
    )
    from .data_extraction_query_attribute_groups_item_filter_item_codes_item import (
        DataExtractionQueryAttributeGroupsItemFilterItemCodesItem,
    )
    from .data_query_list_entry import DataQueryListEntry
    from .data_query_list_entry_ccdl import DataQueryListEntryCcdl
    from .data_query_list_entry_data_extraction import DataQueryListEntryDataExtraction
    from .data_query_slots import DataQuerySlots
    from .dataquery import Dataquery
    from .display_entry import DisplayEntry
    from .elastic_search_bulk_result import ElasticSearchBulkResult
    from .elastic_search_relation_entry import ElasticSearchRelationEntry
    from .elastic_search_result import ElasticSearchResult
    from .elastic_search_result_entry import ElasticSearchResultEntry
    from .elastic_search_result_entry_extended import ElasticSearchResultEntryExtended
    from .elastic_search_translation_entry import ElasticSearchTranslationEntry
    from .filter import Filter
    from .filter_value import FilterValue
    from .git_info import GitInfo
    from .git_info_build import GitInfoBuild
    from .git_info_commit import GitInfoCommit
    from .git_info_commit_id import GitInfoCommitId
    from .localized_value import LocalizedValue
    from .oauth_scope import OauthScope
    from .profile_data_entry import ProfileDataEntry
    from .profile_data_field import ProfileDataField
    from .profile_data_filter import ProfileDataFilter
    from .profile_data_list import ProfileDataList
    from .profile_display_entry import ProfileDisplayEntry
    from .profile_entry import ProfileEntry
    from .profile_filter import ProfileFilter
    from .profile_filter_value import ProfileFilterValue
    from .profile_relative_entry import ProfileRelativeEntry
    from .profile_search_entry import ProfileSearchEntry
    from .profile_search_result import ProfileSearchResult
    from .query import Query
    from .query_quota import QueryQuota
    from .query_quota_entry import QueryQuotaEntry
    from .query_result import QueryResult
    from .query_result_line import QueryResultLine
    from .query_result_line_obfuscated import QueryResultLineObfuscated
    from .query_result_obfuscated import QueryResultObfuscated
    from .query_result_rate_limit import QueryResultRateLimit
    from .relations_entry import RelationsEntry
    from .settings_info import SettingsInfo
    from .system_info import SystemInfo
    from .term_code import TermCode
    from .terminology import Terminology
    from .terminology_systems import TerminologySystems
    from .terminology_systems_item import TerminologySystemsItem
    from .time_restriction import TimeRestriction
    from .translation_entry import TranslationEntry
    from .ui_profile_entry import UiProfileEntry
    from .ui_profile_list import UiProfileList
    from .unit import Unit
    from .upgrade_issue import UpgradeIssue
    from .upgrade_issue_value import UpgradeIssueValue
    from .upgrade_wrapper import UpgradeWrapper
    from .validation_issue import ValidationIssue
    from .validation_issue_value import ValidationIssueValue
    from .value_filter import ValueFilter
    from .value_filter_comparator import ValueFilterComparator
    from .value_filter_type import ValueFilterType
_dynamic_imports: typing.Dict[str, str] = {
    "AfterDate": ".after_date",
    "AttributeDefinition": ".attribute_definition",
    "AttributeFilter": ".attribute_filter",
    "BeforeDate": ".before_date",
    "BuildInfo": ".build_info",
    "Ccdl": ".ccdl",
    "CodeableConceptBulkSearchResult": ".codeable_concept_bulk_search_result",
    "CodeableConceptEntry": ".codeable_concept_entry",
    "CodeableConceptSearchResult": ".codeable_concept_search_result",
    "ContextualizedTermCode": ".contextualized_term_code",
    "ContextualizedTermCodeList": ".contextualized_term_code_list",
    "CriteriaProfileData": ".criteria_profile_data",
    "Criterion": ".criterion",
    "CriterionList": ".criterion_list",
    "Crtdl": ".crtdl",
    "DataExtractionQuery": ".data_extraction_query",
    "DataExtractionQueryAttributeGroupsItem": ".data_extraction_query_attribute_groups_item",
    "DataExtractionQueryAttributeGroupsItemAttributesItem": ".data_extraction_query_attribute_groups_item_attributes_item",
    "DataExtractionQueryAttributeGroupsItemFilterItem": ".data_extraction_query_attribute_groups_item_filter_item",
    "DataExtractionQueryAttributeGroupsItemFilterItemCodesItem": ".data_extraction_query_attribute_groups_item_filter_item_codes_item",
    "DataQueryListEntry": ".data_query_list_entry",
    "DataQueryListEntryCcdl": ".data_query_list_entry_ccdl",
    "DataQueryListEntryDataExtraction": ".data_query_list_entry_data_extraction",
    "DataQuerySlots": ".data_query_slots",
    "Dataquery": ".dataquery",
    "DisplayEntry": ".display_entry",
    "ElasticSearchBulkResult": ".elastic_search_bulk_result",
    "ElasticSearchRelationEntry": ".elastic_search_relation_entry",
    "ElasticSearchResult": ".elastic_search_result",
    "ElasticSearchResultEntry": ".elastic_search_result_entry",
    "ElasticSearchResultEntryExtended": ".elastic_search_result_entry_extended",
    "ElasticSearchTranslationEntry": ".elastic_search_translation_entry",
    "Filter": ".filter",
    "FilterValue": ".filter_value",
    "GitInfo": ".git_info",
    "GitInfoBuild": ".git_info_build",
    "GitInfoCommit": ".git_info_commit",
    "GitInfoCommitId": ".git_info_commit_id",
    "LocalizedValue": ".localized_value",
    "OauthScope": ".oauth_scope",
    "ProfileDataEntry": ".profile_data_entry",
    "ProfileDataField": ".profile_data_field",
    "ProfileDataFilter": ".profile_data_filter",
    "ProfileDataList": ".profile_data_list",
    "ProfileDisplayEntry": ".profile_display_entry",
    "ProfileEntry": ".profile_entry",
    "ProfileFilter": ".profile_filter",
    "ProfileFilterValue": ".profile_filter_value",
    "ProfileRelativeEntry": ".profile_relative_entry",
    "ProfileSearchEntry": ".profile_search_entry",
    "ProfileSearchResult": ".profile_search_result",
    "Query": ".query",
    "QueryQuota": ".query_quota",
    "QueryQuotaEntry": ".query_quota_entry",
    "QueryResult": ".query_result",
    "QueryResultLine": ".query_result_line",
    "QueryResultLineObfuscated": ".query_result_line_obfuscated",
    "QueryResultObfuscated": ".query_result_obfuscated",
    "QueryResultRateLimit": ".query_result_rate_limit",
    "RelationsEntry": ".relations_entry",
    "SettingsInfo": ".settings_info",
    "SystemInfo": ".system_info",
    "TermCode": ".term_code",
    "Terminology": ".terminology",
    "TerminologySystems": ".terminology_systems",
    "TerminologySystemsItem": ".terminology_systems_item",
    "TimeRestriction": ".time_restriction",
    "TranslationEntry": ".translation_entry",
    "UiProfileEntry": ".ui_profile_entry",
    "UiProfileList": ".ui_profile_list",
    "Unit": ".unit",
    "UpgradeIssue": ".upgrade_issue",
    "UpgradeIssueValue": ".upgrade_issue_value",
    "UpgradeWrapper": ".upgrade_wrapper",
    "ValidationIssue": ".validation_issue",
    "ValidationIssueValue": ".validation_issue_value",
    "ValueFilter": ".value_filter",
    "ValueFilterComparator": ".value_filter_comparator",
    "ValueFilterType": ".value_filter_type",
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
    "AfterDate",
    "AttributeDefinition",
    "AttributeFilter",
    "BeforeDate",
    "BuildInfo",
    "Ccdl",
    "CodeableConceptBulkSearchResult",
    "CodeableConceptEntry",
    "CodeableConceptSearchResult",
    "ContextualizedTermCode",
    "ContextualizedTermCodeList",
    "CriteriaProfileData",
    "Criterion",
    "CriterionList",
    "Crtdl",
    "DataExtractionQuery",
    "DataExtractionQueryAttributeGroupsItem",
    "DataExtractionQueryAttributeGroupsItemAttributesItem",
    "DataExtractionQueryAttributeGroupsItemFilterItem",
    "DataExtractionQueryAttributeGroupsItemFilterItemCodesItem",
    "DataQueryListEntry",
    "DataQueryListEntryCcdl",
    "DataQueryListEntryDataExtraction",
    "DataQuerySlots",
    "Dataquery",
    "DisplayEntry",
    "ElasticSearchBulkResult",
    "ElasticSearchRelationEntry",
    "ElasticSearchResult",
    "ElasticSearchResultEntry",
    "ElasticSearchResultEntryExtended",
    "ElasticSearchTranslationEntry",
    "Filter",
    "FilterValue",
    "GitInfo",
    "GitInfoBuild",
    "GitInfoCommit",
    "GitInfoCommitId",
    "LocalizedValue",
    "OauthScope",
    "ProfileDataEntry",
    "ProfileDataField",
    "ProfileDataFilter",
    "ProfileDataList",
    "ProfileDisplayEntry",
    "ProfileEntry",
    "ProfileFilter",
    "ProfileFilterValue",
    "ProfileRelativeEntry",
    "ProfileSearchEntry",
    "ProfileSearchResult",
    "Query",
    "QueryQuota",
    "QueryQuotaEntry",
    "QueryResult",
    "QueryResultLine",
    "QueryResultLineObfuscated",
    "QueryResultObfuscated",
    "QueryResultRateLimit",
    "RelationsEntry",
    "SettingsInfo",
    "SystemInfo",
    "TermCode",
    "Terminology",
    "TerminologySystems",
    "TerminologySystemsItem",
    "TimeRestriction",
    "TranslationEntry",
    "UiProfileEntry",
    "UiProfileList",
    "Unit",
    "UpgradeIssue",
    "UpgradeIssueValue",
    "UpgradeWrapper",
    "ValidationIssue",
    "ValidationIssueValue",
    "ValueFilter",
    "ValueFilterComparator",
    "ValueFilterType",
]
