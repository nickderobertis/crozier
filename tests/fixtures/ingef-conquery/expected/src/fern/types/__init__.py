



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .absolute_form_query import AbsoluteFormQuery
    from .and_condition import AndCondition
    from .array_concept_query import ArrayConceptQuery
    from .array_concept_query_type import ArrayConceptQueryType
    from .big_multi_select_filter import BigMultiSelectFilter
    from .column import Column
    from .column_config import ColumnConfig
    from .column_description import ColumnDescription
    from .column_equal_condition import ColumnEqualCondition
    from .column_id import ColumnId
    from .column_type import ColumnType
    from .compound_date_range_output import CompoundDateRangeOutput
    from .concept import Concept
    from .concept_additional_infos_item import ConceptAdditionalInfosItem
    from .concept_column_select import ConceptColumnSelect
    from .concept_condition import (
        ConceptCondition,
        ConceptCondition_And,
        ConceptCondition_ColumnEqual,
        ConceptCondition_Equal,
        ConceptCondition_Groovy,
        ConceptCondition_Not,
        ConceptCondition_Or,
        ConceptCondition_Prefix,
        ConceptCondition_PrefixRange,
        ConceptCondition_Present,
    )
    from .concept_element_id import ConceptElementId
    from .concept_id import ConceptId
    from .concept_query import ConceptQuery
    from .concept_query_type import ConceptQueryType
    from .concept_tree_child import ConceptTreeChild
    from .concept_tree_child_additional_infos_item import ConceptTreeChildAdditionalInfosItem
    from .connector import Connector
    from .connector_condition import (
        ConnectorCondition,
        ConnectorCondition_And,
        ConnectorCondition_ColumnEqual,
        ConnectorCondition_Equal,
        ConnectorCondition_Groovy,
        ConnectorCondition_Not,
        ConnectorCondition_Or,
        ConnectorCondition_Prefix,
        ConnectorCondition_PrefixRange,
        ConnectorCondition_Present,
    )
    from .connector_id import ConnectorId
    from .connector_selects_item import ConnectorSelectsItem
    from .copy_output import CopyOutput
    from .count_filter import CountFilter
    from .count_quarters_filter import CountQuartersFilter
    from .count_quarters_filter_type import CountQuartersFilterType
    from .count_quarters_select import CountQuartersSelect
    from .count_select import CountSelect
    from .cq_and import CqAnd
    from .cq_before import CqBefore
    from .cq_before_or_same import CqBeforeOrSame
    from .cq_concept import CqConcept
    from .cq_concept_tables import CqConceptTables
    from .cq_concept_tables_date_column import CqConceptTablesDateColumn
    from .cq_concept_type import CqConceptType
    from .cq_date_restriction import CqDateRestriction
    from .cq_days_before import CqDaysBefore
    from .cq_days_before_days import CqDaysBeforeDays
    from .cq_days_before_or_never import CqDaysBeforeOrNever
    from .cq_element import (
        CqElement,
        CqElement_And,
        CqElement_Before,
        CqElement_BeforeOrNever,
        CqElement_BeforeOrSame,
        CqElement_Concept,
        CqElement_DateRestriction,
        CqElement_DaysBefore,
        CqElement_External,
        CqElement_Negation,
        CqElement_Or,
        CqElement_ResultInfoDecorator,
        CqElement_Same,
        CqElement_SavedQuery,
    )
    from .cq_element_base import CqElementBase
    from .cq_external import CqExternal
    from .cq_external_format_item import CqExternalFormatItem
    from .cq_external_format_item_one import CqExternalFormatItemOne
    from .cq_negation import CqNegation
    from .cq_or import CqOr
    from .cq_result_info_decorator import CqResultInfoDecorator
    from .cq_reused_query import CqReusedQuery
    from .cq_same import CqSame
    from .cq_sampled import CqSampled
    from .currency_config import CurrencyConfig
    from .dataset_id import DatasetId
    from .date import Date
    from .date_aggregation_mode import DateAggregationMode
    from .date_distance_filter import DateDistanceFilter
    from .date_distance_filter_time_unit import DateDistanceFilterTimeUnit
    from .date_distance_select import DateDistanceSelect
    from .date_distance_select_time_unit import DateDistanceSelectTimeUnit
    from .date_range import DateRange
    from .date_range_output import DateRangeOutput
    from .date_time import DateTime
    from .date_union_select import DateUnionSelect
    from .distinct_select import DistinctSelect
    from .duration_sum_filter import DurationSumFilter
    from .duration_sum_select import DurationSumSelect
    from .entity_date_query import EntityDateQuery
    from .entity_history_execution_status import EntityHistoryExecutionStatus
    from .entity_history_execution_status_infos_item import EntityHistoryExecutionStatusInfosItem
    from .entity_history_execution_status_time_stratified_infos_item import (
        EntityHistoryExecutionStatusTimeStratifiedInfosItem,
    )
    from .entity_history_execution_status_time_stratified_infos_item_columns import (
        EntityHistoryExecutionStatusTimeStratifiedInfosItemColumns,
    )
    from .entity_history_execution_status_time_stratified_infos_item_years_item import (
        EntityHistoryExecutionStatusTimeStratifiedInfosItemYearsItem,
    )
    from .entity_history_execution_status_time_stratified_infos_item_years_item_quarters_item import (
        EntityHistoryExecutionStatusTimeStratifiedInfosItemYearsItemQuartersItem,
    )
    from .entity_preview_config import EntityPreviewConfig
    from .entity_preview_config_all_item import EntityPreviewConfigAllItem
    from .entity_preview_config_default_item import EntityPreviewConfigDefaultItem
    from .epoch_date_range_output import EpochDateRangeOutput
    from .epoch_output import EpochOutput
    from .equal_condition import EqualCondition
    from .error import Error
    from .error_info import ErrorInfo
    from .event_date_union_select import EventDateUnionSelect
    from .event_duration_sum_select import EventDurationSumSelect
    from .execution_id import ExecutionId
    from .exists_select import ExistsSelect
    from .filter import (
        Filter,
        Filter_BigMultiSelect,
        Filter_Count,
        Filter_DateDistance,
        Filter_DurationSum,
        Filter_Flags,
        Filter_MultiSelect,
        Filter_Number,
        Filter_QuartersInYear,
        Filter_SingleSelect,
        Filter_Sum,
    )
    from .filter_base import FilterBase
    from .filter_id import FilterId
    from .filter_value import (
        FilterValue,
        FilterValue_BigMultiSelect,
        FilterValue_DecimalRange,
        FilterValue_Integer,
        FilterValue_IntegerRange,
        FilterValue_MoneyRange,
        FilterValue_MultiSelect,
        FilterValue_RealRange,
        FilterValue_Select,
        FilterValue_String,
    )
    from .filter_value_base import FilterValueBase
    from .filter_value_big_multi_select import FilterValueBigMultiSelect
    from .filter_value_integer import FilterValueInteger
    from .filter_value_integer_range import FilterValueIntegerRange
    from .filter_value_integer_range_value import FilterValueIntegerRangeValue
    from .filter_value_multi_select import FilterValueMultiSelect
    from .filter_value_number_range import FilterValueNumberRange
    from .filter_value_number_range_value import FilterValueNumberRangeValue
    from .filter_value_single_select import FilterValueSingleSelect
    from .filter_value_string import FilterValueString
    from .first_value_select import FirstValueSelect
    from .flag_filter import FlagFilter
    from .flag_select import FlagSelect
    from .frontend_config import FrontendConfig
    from .frontend_dataset_id import FrontendDatasetId
    from .full_execution_status import FullExecutionStatus
    from .groovy_condition import GroovyCondition
    from .group_filter_value import GroupFilterValue
    from .id import Id
    from .import_ import Import
    from .import_inputs_item import ImportInputsItem
    from .is_present_condition import IsPresentCondition
    from .labeled import Labeled
    from .last_value_select import LastValueSelect
    from .line_output import LineOutput
    from .mail import Mail
    from .major_type import MajorType
    from .mapping_id import MappingId
    from .me import Me
    from .me_dataset_abilities_value import MeDatasetAbilitiesValue
    from .me_groups_item import MeGroupsItem
    from .multi_select_filter import MultiSelectFilter
    from .not_condition import NotCondition
    from .null_output import NullOutput
    from .number_filter import NumberFilter
    from .or_condition import OrCondition
    from .output_description import (
        OutputDescription,
        OutputDescription_CompoundDateRange,
        OutputDescription_Copy,
        OutputDescription_DateRange,
        OutputDescription_Epoch,
        OutputDescription_EpochDateRange,
        OutputDescription_Line,
        OutputDescription_Null,
    )
    from .output_description_base import OutputDescriptionBase
    from .prefix_condition import PrefixCondition
    from .prefix_range_condition import PrefixRangeCondition
    from .preview_config import PreviewConfig
    from .preview_config_info_card_selects_item import PreviewConfigInfoCardSelectsItem
    from .preview_config_time_stratified_selects_item import PreviewConfigTimeStratifiedSelectsItem
    from .preview_config_time_stratified_selects_item_selects_item import (
        PreviewConfigTimeStratifiedSelectsItemSelectsItem,
    )
    from .quarter_select import QuarterSelect
    from .quarters_in_year_filter import QuartersInYearFilter
    from .quarters_in_year_select import QuartersInYearSelect
    from .query import (
        Query,
        Query_AbsoluteFormQuery,
        Query_ArrayConceptQuery,
        Query_ConceptQuery,
        Query_EntityDateQuery,
        Query_RelativeFormQuery,
        Query_SecondaryIdQuery,
        Query_TableExport,
    )
    from .query_state import QueryState
    from .query_status import QueryStatus
    from .random_value_select import RandomValueSelect
    from .relative_form_query import RelativeFormQuery
    from .relative_form_query_index_placement import RelativeFormQueryIndexPlacement
    from .relative_form_query_time_unit import RelativeFormQueryTimeUnit
    from .resolution_and_alignment import ResolutionAndAlignment
    from .resolution_and_alignment_alignment import ResolutionAndAlignmentAlignment
    from .resolution_and_alignment_resolution import ResolutionAndAlignmentResolution
    from .resolved_concepts_result import ResolvedConceptsResult
    from .resolved_concepts_result_resolved_filter import ResolvedConceptsResultResolvedFilter
    from .resolved_concepts_result_resolved_filter_value_item import ResolvedConceptsResultResolvedFilterValueItem
    from .result_asset import ResultAsset
    from .searchable import Searchable
    from .secondary_id_id import SecondaryIdId
    from .secondary_id_query import SecondaryIdQuery
    from .secondary_id_query_type import SecondaryIdQueryType
    from .select import (
        Select,
        Select_Count,
        Select_CountQuarters,
        Select_DateDistance,
        Select_DateUnion,
        Select_Distinct,
        Select_DurationSum,
        Select_First,
        Select_Flags,
        Select_Last,
        Select_Quarter,
        Select_QuartersInYear,
        Select_Random,
        Select_Sum,
    )
    from .select_base import SelectBase
    from .select_filter_base import SelectFilterBase
    from .select_id import SelectId
    from .semantics import (
        Semantics,
        Semantics_Categorical,
        Semantics_Column,
        Semantics_ConceptColumn,
        Semantics_EventDate,
        Semantics_Group,
        Semantics_Hidden,
        Semantics_Id,
        Semantics_SecondaryId,
        Semantics_Select,
        Semantics_Sources,
    )
    from .semantics_base import SemanticsBase
    from .semantics_categorical import SemanticsCategorical
    from .semantics_column import SemanticsColumn
    from .semantics_concept_column import SemanticsConceptColumn
    from .semantics_event_date import SemanticsEventDate
    from .semantics_group import SemanticsGroup
    from .semantics_hidden import SemanticsHidden
    from .semantics_id import SemanticsId
    from .semantics_secondary_id import SemanticsSecondaryId
    from .semantics_select import SemanticsSelect
    from .semantics_sources import SemanticsSources
    from .single_select_filter import SingleSelectFilter
    from .sum_filter import SumFilter
    from .sum_select import SumSelect
    from .table import Table
    from .table_export_query import TableExportQuery
    from .table_id import TableId
    from .template_id import TemplateId
    from .temporal_sampler import TemporalSampler
    from .universal_select import (
        UniversalSelect,
        UniversalSelect_ConceptColumn,
        UniversalSelect_CountQuarters,
        UniversalSelect_EventDateUnion,
        UniversalSelect_EventDurationSum,
        UniversalSelect_Exists,
        UniversalSelect_Quarter,
    )
    from .upload_config import UploadConfig
    from .user_id import UserId
    from .validity_date import ValidityDate
    from .validity_date_id import ValidityDateId
    from .version_container import VersionContainer
_dynamic_imports: typing.Dict[str, str] = {
    "AbsoluteFormQuery": ".absolute_form_query",
    "AndCondition": ".and_condition",
    "ArrayConceptQuery": ".array_concept_query",
    "ArrayConceptQueryType": ".array_concept_query_type",
    "BigMultiSelectFilter": ".big_multi_select_filter",
    "Column": ".column",
    "ColumnConfig": ".column_config",
    "ColumnDescription": ".column_description",
    "ColumnEqualCondition": ".column_equal_condition",
    "ColumnId": ".column_id",
    "ColumnType": ".column_type",
    "CompoundDateRangeOutput": ".compound_date_range_output",
    "Concept": ".concept",
    "ConceptAdditionalInfosItem": ".concept_additional_infos_item",
    "ConceptColumnSelect": ".concept_column_select",
    "ConceptCondition": ".concept_condition",
    "ConceptCondition_And": ".concept_condition",
    "ConceptCondition_ColumnEqual": ".concept_condition",
    "ConceptCondition_Equal": ".concept_condition",
    "ConceptCondition_Groovy": ".concept_condition",
    "ConceptCondition_Not": ".concept_condition",
    "ConceptCondition_Or": ".concept_condition",
    "ConceptCondition_Prefix": ".concept_condition",
    "ConceptCondition_PrefixRange": ".concept_condition",
    "ConceptCondition_Present": ".concept_condition",
    "ConceptElementId": ".concept_element_id",
    "ConceptId": ".concept_id",
    "ConceptQuery": ".concept_query",
    "ConceptQueryType": ".concept_query_type",
    "ConceptTreeChild": ".concept_tree_child",
    "ConceptTreeChildAdditionalInfosItem": ".concept_tree_child_additional_infos_item",
    "Connector": ".connector",
    "ConnectorCondition": ".connector_condition",
    "ConnectorCondition_And": ".connector_condition",
    "ConnectorCondition_ColumnEqual": ".connector_condition",
    "ConnectorCondition_Equal": ".connector_condition",
    "ConnectorCondition_Groovy": ".connector_condition",
    "ConnectorCondition_Not": ".connector_condition",
    "ConnectorCondition_Or": ".connector_condition",
    "ConnectorCondition_Prefix": ".connector_condition",
    "ConnectorCondition_PrefixRange": ".connector_condition",
    "ConnectorCondition_Present": ".connector_condition",
    "ConnectorId": ".connector_id",
    "ConnectorSelectsItem": ".connector_selects_item",
    "CopyOutput": ".copy_output",
    "CountFilter": ".count_filter",
    "CountQuartersFilter": ".count_quarters_filter",
    "CountQuartersFilterType": ".count_quarters_filter_type",
    "CountQuartersSelect": ".count_quarters_select",
    "CountSelect": ".count_select",
    "CqAnd": ".cq_and",
    "CqBefore": ".cq_before",
    "CqBeforeOrSame": ".cq_before_or_same",
    "CqConcept": ".cq_concept",
    "CqConceptTables": ".cq_concept_tables",
    "CqConceptTablesDateColumn": ".cq_concept_tables_date_column",
    "CqConceptType": ".cq_concept_type",
    "CqDateRestriction": ".cq_date_restriction",
    "CqDaysBefore": ".cq_days_before",
    "CqDaysBeforeDays": ".cq_days_before_days",
    "CqDaysBeforeOrNever": ".cq_days_before_or_never",
    "CqElement": ".cq_element",
    "CqElementBase": ".cq_element_base",
    "CqElement_And": ".cq_element",
    "CqElement_Before": ".cq_element",
    "CqElement_BeforeOrNever": ".cq_element",
    "CqElement_BeforeOrSame": ".cq_element",
    "CqElement_Concept": ".cq_element",
    "CqElement_DateRestriction": ".cq_element",
    "CqElement_DaysBefore": ".cq_element",
    "CqElement_External": ".cq_element",
    "CqElement_Negation": ".cq_element",
    "CqElement_Or": ".cq_element",
    "CqElement_ResultInfoDecorator": ".cq_element",
    "CqElement_Same": ".cq_element",
    "CqElement_SavedQuery": ".cq_element",
    "CqExternal": ".cq_external",
    "CqExternalFormatItem": ".cq_external_format_item",
    "CqExternalFormatItemOne": ".cq_external_format_item_one",
    "CqNegation": ".cq_negation",
    "CqOr": ".cq_or",
    "CqResultInfoDecorator": ".cq_result_info_decorator",
    "CqReusedQuery": ".cq_reused_query",
    "CqSame": ".cq_same",
    "CqSampled": ".cq_sampled",
    "CurrencyConfig": ".currency_config",
    "DatasetId": ".dataset_id",
    "Date": ".date",
    "DateAggregationMode": ".date_aggregation_mode",
    "DateDistanceFilter": ".date_distance_filter",
    "DateDistanceFilterTimeUnit": ".date_distance_filter_time_unit",
    "DateDistanceSelect": ".date_distance_select",
    "DateDistanceSelectTimeUnit": ".date_distance_select_time_unit",
    "DateRange": ".date_range",
    "DateRangeOutput": ".date_range_output",
    "DateTime": ".date_time",
    "DateUnionSelect": ".date_union_select",
    "DistinctSelect": ".distinct_select",
    "DurationSumFilter": ".duration_sum_filter",
    "DurationSumSelect": ".duration_sum_select",
    "EntityDateQuery": ".entity_date_query",
    "EntityHistoryExecutionStatus": ".entity_history_execution_status",
    "EntityHistoryExecutionStatusInfosItem": ".entity_history_execution_status_infos_item",
    "EntityHistoryExecutionStatusTimeStratifiedInfosItem": ".entity_history_execution_status_time_stratified_infos_item",
    "EntityHistoryExecutionStatusTimeStratifiedInfosItemColumns": ".entity_history_execution_status_time_stratified_infos_item_columns",
    "EntityHistoryExecutionStatusTimeStratifiedInfosItemYearsItem": ".entity_history_execution_status_time_stratified_infos_item_years_item",
    "EntityHistoryExecutionStatusTimeStratifiedInfosItemYearsItemQuartersItem": ".entity_history_execution_status_time_stratified_infos_item_years_item_quarters_item",
    "EntityPreviewConfig": ".entity_preview_config",
    "EntityPreviewConfigAllItem": ".entity_preview_config_all_item",
    "EntityPreviewConfigDefaultItem": ".entity_preview_config_default_item",
    "EpochDateRangeOutput": ".epoch_date_range_output",
    "EpochOutput": ".epoch_output",
    "EqualCondition": ".equal_condition",
    "Error": ".error",
    "ErrorInfo": ".error_info",
    "EventDateUnionSelect": ".event_date_union_select",
    "EventDurationSumSelect": ".event_duration_sum_select",
    "ExecutionId": ".execution_id",
    "ExistsSelect": ".exists_select",
    "Filter": ".filter",
    "FilterBase": ".filter_base",
    "FilterId": ".filter_id",
    "FilterValue": ".filter_value",
    "FilterValueBase": ".filter_value_base",
    "FilterValueBigMultiSelect": ".filter_value_big_multi_select",
    "FilterValueInteger": ".filter_value_integer",
    "FilterValueIntegerRange": ".filter_value_integer_range",
    "FilterValueIntegerRangeValue": ".filter_value_integer_range_value",
    "FilterValueMultiSelect": ".filter_value_multi_select",
    "FilterValueNumberRange": ".filter_value_number_range",
    "FilterValueNumberRangeValue": ".filter_value_number_range_value",
    "FilterValueSingleSelect": ".filter_value_single_select",
    "FilterValueString": ".filter_value_string",
    "FilterValue_BigMultiSelect": ".filter_value",
    "FilterValue_DecimalRange": ".filter_value",
    "FilterValue_Integer": ".filter_value",
    "FilterValue_IntegerRange": ".filter_value",
    "FilterValue_MoneyRange": ".filter_value",
    "FilterValue_MultiSelect": ".filter_value",
    "FilterValue_RealRange": ".filter_value",
    "FilterValue_Select": ".filter_value",
    "FilterValue_String": ".filter_value",
    "Filter_BigMultiSelect": ".filter",
    "Filter_Count": ".filter",
    "Filter_DateDistance": ".filter",
    "Filter_DurationSum": ".filter",
    "Filter_Flags": ".filter",
    "Filter_MultiSelect": ".filter",
    "Filter_Number": ".filter",
    "Filter_QuartersInYear": ".filter",
    "Filter_SingleSelect": ".filter",
    "Filter_Sum": ".filter",
    "FirstValueSelect": ".first_value_select",
    "FlagFilter": ".flag_filter",
    "FlagSelect": ".flag_select",
    "FrontendConfig": ".frontend_config",
    "FrontendDatasetId": ".frontend_dataset_id",
    "FullExecutionStatus": ".full_execution_status",
    "GroovyCondition": ".groovy_condition",
    "GroupFilterValue": ".group_filter_value",
    "Id": ".id",
    "Import": ".import_",
    "ImportInputsItem": ".import_inputs_item",
    "IsPresentCondition": ".is_present_condition",
    "Labeled": ".labeled",
    "LastValueSelect": ".last_value_select",
    "LineOutput": ".line_output",
    "Mail": ".mail",
    "MajorType": ".major_type",
    "MappingId": ".mapping_id",
    "Me": ".me",
    "MeDatasetAbilitiesValue": ".me_dataset_abilities_value",
    "MeGroupsItem": ".me_groups_item",
    "MultiSelectFilter": ".multi_select_filter",
    "NotCondition": ".not_condition",
    "NullOutput": ".null_output",
    "NumberFilter": ".number_filter",
    "OrCondition": ".or_condition",
    "OutputDescription": ".output_description",
    "OutputDescriptionBase": ".output_description_base",
    "OutputDescription_CompoundDateRange": ".output_description",
    "OutputDescription_Copy": ".output_description",
    "OutputDescription_DateRange": ".output_description",
    "OutputDescription_Epoch": ".output_description",
    "OutputDescription_EpochDateRange": ".output_description",
    "OutputDescription_Line": ".output_description",
    "OutputDescription_Null": ".output_description",
    "PrefixCondition": ".prefix_condition",
    "PrefixRangeCondition": ".prefix_range_condition",
    "PreviewConfig": ".preview_config",
    "PreviewConfigInfoCardSelectsItem": ".preview_config_info_card_selects_item",
    "PreviewConfigTimeStratifiedSelectsItem": ".preview_config_time_stratified_selects_item",
    "PreviewConfigTimeStratifiedSelectsItemSelectsItem": ".preview_config_time_stratified_selects_item_selects_item",
    "QuarterSelect": ".quarter_select",
    "QuartersInYearFilter": ".quarters_in_year_filter",
    "QuartersInYearSelect": ".quarters_in_year_select",
    "Query": ".query",
    "QueryState": ".query_state",
    "QueryStatus": ".query_status",
    "Query_AbsoluteFormQuery": ".query",
    "Query_ArrayConceptQuery": ".query",
    "Query_ConceptQuery": ".query",
    "Query_EntityDateQuery": ".query",
    "Query_RelativeFormQuery": ".query",
    "Query_SecondaryIdQuery": ".query",
    "Query_TableExport": ".query",
    "RandomValueSelect": ".random_value_select",
    "RelativeFormQuery": ".relative_form_query",
    "RelativeFormQueryIndexPlacement": ".relative_form_query_index_placement",
    "RelativeFormQueryTimeUnit": ".relative_form_query_time_unit",
    "ResolutionAndAlignment": ".resolution_and_alignment",
    "ResolutionAndAlignmentAlignment": ".resolution_and_alignment_alignment",
    "ResolutionAndAlignmentResolution": ".resolution_and_alignment_resolution",
    "ResolvedConceptsResult": ".resolved_concepts_result",
    "ResolvedConceptsResultResolvedFilter": ".resolved_concepts_result_resolved_filter",
    "ResolvedConceptsResultResolvedFilterValueItem": ".resolved_concepts_result_resolved_filter_value_item",
    "ResultAsset": ".result_asset",
    "Searchable": ".searchable",
    "SecondaryIdId": ".secondary_id_id",
    "SecondaryIdQuery": ".secondary_id_query",
    "SecondaryIdQueryType": ".secondary_id_query_type",
    "Select": ".select",
    "SelectBase": ".select_base",
    "SelectFilterBase": ".select_filter_base",
    "SelectId": ".select_id",
    "Select_Count": ".select",
    "Select_CountQuarters": ".select",
    "Select_DateDistance": ".select",
    "Select_DateUnion": ".select",
    "Select_Distinct": ".select",
    "Select_DurationSum": ".select",
    "Select_First": ".select",
    "Select_Flags": ".select",
    "Select_Last": ".select",
    "Select_Quarter": ".select",
    "Select_QuartersInYear": ".select",
    "Select_Random": ".select",
    "Select_Sum": ".select",
    "Semantics": ".semantics",
    "SemanticsBase": ".semantics_base",
    "SemanticsCategorical": ".semantics_categorical",
    "SemanticsColumn": ".semantics_column",
    "SemanticsConceptColumn": ".semantics_concept_column",
    "SemanticsEventDate": ".semantics_event_date",
    "SemanticsGroup": ".semantics_group",
    "SemanticsHidden": ".semantics_hidden",
    "SemanticsId": ".semantics_id",
    "SemanticsSecondaryId": ".semantics_secondary_id",
    "SemanticsSelect": ".semantics_select",
    "SemanticsSources": ".semantics_sources",
    "Semantics_Categorical": ".semantics",
    "Semantics_Column": ".semantics",
    "Semantics_ConceptColumn": ".semantics",
    "Semantics_EventDate": ".semantics",
    "Semantics_Group": ".semantics",
    "Semantics_Hidden": ".semantics",
    "Semantics_Id": ".semantics",
    "Semantics_SecondaryId": ".semantics",
    "Semantics_Select": ".semantics",
    "Semantics_Sources": ".semantics",
    "SingleSelectFilter": ".single_select_filter",
    "SumFilter": ".sum_filter",
    "SumSelect": ".sum_select",
    "Table": ".table",
    "TableExportQuery": ".table_export_query",
    "TableId": ".table_id",
    "TemplateId": ".template_id",
    "TemporalSampler": ".temporal_sampler",
    "UniversalSelect": ".universal_select",
    "UniversalSelect_ConceptColumn": ".universal_select",
    "UniversalSelect_CountQuarters": ".universal_select",
    "UniversalSelect_EventDateUnion": ".universal_select",
    "UniversalSelect_EventDurationSum": ".universal_select",
    "UniversalSelect_Exists": ".universal_select",
    "UniversalSelect_Quarter": ".universal_select",
    "UploadConfig": ".upload_config",
    "UserId": ".user_id",
    "ValidityDate": ".validity_date",
    "ValidityDateId": ".validity_date_id",
    "VersionContainer": ".version_container",
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
    "AbsoluteFormQuery",
    "AndCondition",
    "ArrayConceptQuery",
    "ArrayConceptQueryType",
    "BigMultiSelectFilter",
    "Column",
    "ColumnConfig",
    "ColumnDescription",
    "ColumnEqualCondition",
    "ColumnId",
    "ColumnType",
    "CompoundDateRangeOutput",
    "Concept",
    "ConceptAdditionalInfosItem",
    "ConceptColumnSelect",
    "ConceptCondition",
    "ConceptCondition_And",
    "ConceptCondition_ColumnEqual",
    "ConceptCondition_Equal",
    "ConceptCondition_Groovy",
    "ConceptCondition_Not",
    "ConceptCondition_Or",
    "ConceptCondition_Prefix",
    "ConceptCondition_PrefixRange",
    "ConceptCondition_Present",
    "ConceptElementId",
    "ConceptId",
    "ConceptQuery",
    "ConceptQueryType",
    "ConceptTreeChild",
    "ConceptTreeChildAdditionalInfosItem",
    "Connector",
    "ConnectorCondition",
    "ConnectorCondition_And",
    "ConnectorCondition_ColumnEqual",
    "ConnectorCondition_Equal",
    "ConnectorCondition_Groovy",
    "ConnectorCondition_Not",
    "ConnectorCondition_Or",
    "ConnectorCondition_Prefix",
    "ConnectorCondition_PrefixRange",
    "ConnectorCondition_Present",
    "ConnectorId",
    "ConnectorSelectsItem",
    "CopyOutput",
    "CountFilter",
    "CountQuartersFilter",
    "CountQuartersFilterType",
    "CountQuartersSelect",
    "CountSelect",
    "CqAnd",
    "CqBefore",
    "CqBeforeOrSame",
    "CqConcept",
    "CqConceptTables",
    "CqConceptTablesDateColumn",
    "CqConceptType",
    "CqDateRestriction",
    "CqDaysBefore",
    "CqDaysBeforeDays",
    "CqDaysBeforeOrNever",
    "CqElement",
    "CqElementBase",
    "CqElement_And",
    "CqElement_Before",
    "CqElement_BeforeOrNever",
    "CqElement_BeforeOrSame",
    "CqElement_Concept",
    "CqElement_DateRestriction",
    "CqElement_DaysBefore",
    "CqElement_External",
    "CqElement_Negation",
    "CqElement_Or",
    "CqElement_ResultInfoDecorator",
    "CqElement_Same",
    "CqElement_SavedQuery",
    "CqExternal",
    "CqExternalFormatItem",
    "CqExternalFormatItemOne",
    "CqNegation",
    "CqOr",
    "CqResultInfoDecorator",
    "CqReusedQuery",
    "CqSame",
    "CqSampled",
    "CurrencyConfig",
    "DatasetId",
    "Date",
    "DateAggregationMode",
    "DateDistanceFilter",
    "DateDistanceFilterTimeUnit",
    "DateDistanceSelect",
    "DateDistanceSelectTimeUnit",
    "DateRange",
    "DateRangeOutput",
    "DateTime",
    "DateUnionSelect",
    "DistinctSelect",
    "DurationSumFilter",
    "DurationSumSelect",
    "EntityDateQuery",
    "EntityHistoryExecutionStatus",
    "EntityHistoryExecutionStatusInfosItem",
    "EntityHistoryExecutionStatusTimeStratifiedInfosItem",
    "EntityHistoryExecutionStatusTimeStratifiedInfosItemColumns",
    "EntityHistoryExecutionStatusTimeStratifiedInfosItemYearsItem",
    "EntityHistoryExecutionStatusTimeStratifiedInfosItemYearsItemQuartersItem",
    "EntityPreviewConfig",
    "EntityPreviewConfigAllItem",
    "EntityPreviewConfigDefaultItem",
    "EpochDateRangeOutput",
    "EpochOutput",
    "EqualCondition",
    "Error",
    "ErrorInfo",
    "EventDateUnionSelect",
    "EventDurationSumSelect",
    "ExecutionId",
    "ExistsSelect",
    "Filter",
    "FilterBase",
    "FilterId",
    "FilterValue",
    "FilterValueBase",
    "FilterValueBigMultiSelect",
    "FilterValueInteger",
    "FilterValueIntegerRange",
    "FilterValueIntegerRangeValue",
    "FilterValueMultiSelect",
    "FilterValueNumberRange",
    "FilterValueNumberRangeValue",
    "FilterValueSingleSelect",
    "FilterValueString",
    "FilterValue_BigMultiSelect",
    "FilterValue_DecimalRange",
    "FilterValue_Integer",
    "FilterValue_IntegerRange",
    "FilterValue_MoneyRange",
    "FilterValue_MultiSelect",
    "FilterValue_RealRange",
    "FilterValue_Select",
    "FilterValue_String",
    "Filter_BigMultiSelect",
    "Filter_Count",
    "Filter_DateDistance",
    "Filter_DurationSum",
    "Filter_Flags",
    "Filter_MultiSelect",
    "Filter_Number",
    "Filter_QuartersInYear",
    "Filter_SingleSelect",
    "Filter_Sum",
    "FirstValueSelect",
    "FlagFilter",
    "FlagSelect",
    "FrontendConfig",
    "FrontendDatasetId",
    "FullExecutionStatus",
    "GroovyCondition",
    "GroupFilterValue",
    "Id",
    "Import",
    "ImportInputsItem",
    "IsPresentCondition",
    "Labeled",
    "LastValueSelect",
    "LineOutput",
    "Mail",
    "MajorType",
    "MappingId",
    "Me",
    "MeDatasetAbilitiesValue",
    "MeGroupsItem",
    "MultiSelectFilter",
    "NotCondition",
    "NullOutput",
    "NumberFilter",
    "OrCondition",
    "OutputDescription",
    "OutputDescriptionBase",
    "OutputDescription_CompoundDateRange",
    "OutputDescription_Copy",
    "OutputDescription_DateRange",
    "OutputDescription_Epoch",
    "OutputDescription_EpochDateRange",
    "OutputDescription_Line",
    "OutputDescription_Null",
    "PrefixCondition",
    "PrefixRangeCondition",
    "PreviewConfig",
    "PreviewConfigInfoCardSelectsItem",
    "PreviewConfigTimeStratifiedSelectsItem",
    "PreviewConfigTimeStratifiedSelectsItemSelectsItem",
    "QuarterSelect",
    "QuartersInYearFilter",
    "QuartersInYearSelect",
    "Query",
    "QueryState",
    "QueryStatus",
    "Query_AbsoluteFormQuery",
    "Query_ArrayConceptQuery",
    "Query_ConceptQuery",
    "Query_EntityDateQuery",
    "Query_RelativeFormQuery",
    "Query_SecondaryIdQuery",
    "Query_TableExport",
    "RandomValueSelect",
    "RelativeFormQuery",
    "RelativeFormQueryIndexPlacement",
    "RelativeFormQueryTimeUnit",
    "ResolutionAndAlignment",
    "ResolutionAndAlignmentAlignment",
    "ResolutionAndAlignmentResolution",
    "ResolvedConceptsResult",
    "ResolvedConceptsResultResolvedFilter",
    "ResolvedConceptsResultResolvedFilterValueItem",
    "ResultAsset",
    "Searchable",
    "SecondaryIdId",
    "SecondaryIdQuery",
    "SecondaryIdQueryType",
    "Select",
    "SelectBase",
    "SelectFilterBase",
    "SelectId",
    "Select_Count",
    "Select_CountQuarters",
    "Select_DateDistance",
    "Select_DateUnion",
    "Select_Distinct",
    "Select_DurationSum",
    "Select_First",
    "Select_Flags",
    "Select_Last",
    "Select_Quarter",
    "Select_QuartersInYear",
    "Select_Random",
    "Select_Sum",
    "Semantics",
    "SemanticsBase",
    "SemanticsCategorical",
    "SemanticsColumn",
    "SemanticsConceptColumn",
    "SemanticsEventDate",
    "SemanticsGroup",
    "SemanticsHidden",
    "SemanticsId",
    "SemanticsSecondaryId",
    "SemanticsSelect",
    "SemanticsSources",
    "Semantics_Categorical",
    "Semantics_Column",
    "Semantics_ConceptColumn",
    "Semantics_EventDate",
    "Semantics_Group",
    "Semantics_Hidden",
    "Semantics_Id",
    "Semantics_SecondaryId",
    "Semantics_Select",
    "Semantics_Sources",
    "SingleSelectFilter",
    "SumFilter",
    "SumSelect",
    "Table",
    "TableExportQuery",
    "TableId",
    "TemplateId",
    "TemporalSampler",
    "UniversalSelect",
    "UniversalSelect_ConceptColumn",
    "UniversalSelect_CountQuarters",
    "UniversalSelect_EventDateUnion",
    "UniversalSelect_EventDurationSum",
    "UniversalSelect_Exists",
    "UniversalSelect_Quarter",
    "UploadConfig",
    "UserId",
    "ValidityDate",
    "ValidityDateId",
    "VersionContainer",
]
