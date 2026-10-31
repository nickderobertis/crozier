



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .asset_kind import AssetKind
    from .barcode_element import BarcodeElement
    from .batch_child_page import BatchChildPage
    from .batch_child_summary import BatchChildSummary
    from .batch_child_summary_result import BatchChildSummaryResult
    from .batch_job_accepted import BatchJobAccepted
    from .batch_job_accepted_operation import BatchJobAcceptedOperation
    from .batch_summary_counts import BatchSummaryCounts
    from .bounding_box import BoundingBox
    from .confidence import Confidence
    from .confidence_scope import ConfidenceScope
    from .confidence_source_scale import ConfidenceSourceScale
    from .coordinate_unit import CoordinateUnit
    from .delete_extraction_pipeline_response import DeleteExtractionPipelineResponse
    from .delete_file_response import DeleteFileResponse
    from .document_asset import DocumentAsset
    from .document_element import (
        DocumentElement,
        DocumentElement_Barcode,
        DocumentElement_Figure,
        DocumentElement_Formula,
        DocumentElement_KeyValue,
        DocumentElement_Link,
        DocumentElement_Other,
        DocumentElement_QueryAnswer,
        DocumentElement_Section,
        DocumentElement_SelectionMark,
        DocumentElement_Signature,
        DocumentElement_Stamp,
        DocumentElement_Table,
        DocumentElement_Text,
    )
    from .document_element_kind import DocumentElementKind
    from .document_page import DocumentPage
    from .document_page_quality import DocumentPageQuality
    from .document_page_quality_defects_item import DocumentPageQualityDefectsItem
    from .document_page_quality_metrics_item import DocumentPageQualityMetricsItem
    from .document_page_quality_metrics_item_value import DocumentPageQualityMetricsItemValue
    from .document_provenance import DocumentProvenance
    from .document_relation import DocumentRelation
    from .error_body import ErrorBody
    from .error_response import ErrorResponse
    from .extract_batch_item import ExtractBatchItem
    from .extract_batch_item_grounding import ExtractBatchItemGrounding
    from .extract_batch_item_llm_options import ExtractBatchItemLlmOptions
    from .extract_batch_item_llm_options_reasoning_effort import ExtractBatchItemLlmOptionsReasoningEffort
    from .extract_batch_item_llm_options_reasoning_effort_one import ExtractBatchItemLlmOptionsReasoningEffortOne
    from .extract_batch_item_llm_options_reasoning_effort_zero import ExtractBatchItemLlmOptionsReasoningEffortZero
    from .extract_batch_request import ExtractBatchRequest
    from .extract_batch_request_items_item import ExtractBatchRequestItemsItem
    from .extract_batch_request_items_item_grounding import ExtractBatchRequestItemsItemGrounding
    from .extract_batch_request_items_item_llm_options import ExtractBatchRequestItemsItemLlmOptions
    from .extract_batch_request_items_item_llm_options_reasoning_effort import (
        ExtractBatchRequestItemsItemLlmOptionsReasoningEffort,
    )
    from .extract_batch_request_items_item_llm_options_reasoning_effort_one import (
        ExtractBatchRequestItemsItemLlmOptionsReasoningEffortOne,
    )
    from .extract_batch_request_items_item_llm_options_reasoning_effort_zero import (
        ExtractBatchRequestItemsItemLlmOptionsReasoningEffortZero,
    )
    from .extract_batch_request_output_format import ExtractBatchRequestOutputFormat
    from .extract_request import ExtractRequest
    from .extract_request_grounding import ExtractRequestGrounding
    from .extract_request_llm_options import ExtractRequestLlmOptions
    from .extract_request_llm_options_reasoning_effort import ExtractRequestLlmOptionsReasoningEffort
    from .extract_request_llm_options_reasoning_effort_one import ExtractRequestLlmOptionsReasoningEffortOne
    from .extract_request_llm_options_reasoning_effort_zero import ExtractRequestLlmOptionsReasoningEffortZero
    from .extract_request_output_format import ExtractRequestOutputFormat
    from .extraction_attempt import ExtractionAttempt
    from .extraction_attempt_kind import ExtractionAttemptKind
    from .extraction_attempt_status import ExtractionAttemptStatus
    from .extraction_citation import ExtractionCitation
    from .extraction_citation_granularity import ExtractionCitationGranularity
    from .extraction_grounding_field import ExtractionGroundingField
    from .extraction_grounding_field_transform_claim import ExtractionGroundingFieldTransformClaim
    from .extraction_grounding_field_transform_claim_confidence import ExtractionGroundingFieldTransformClaimConfidence
    from .extraction_grounding_field_transform_claim_operation import ExtractionGroundingFieldTransformClaimOperation
    from .extraction_grounding_field_transform_claim_parameters_value import (
        ExtractionGroundingFieldTransformClaimParametersValue,
    )
    from .extraction_grounding_mode import ExtractionGroundingMode
    from .extraction_grounding_result import ExtractionGroundingResult
    from .extraction_grounding_result_mode import ExtractionGroundingResultMode
    from .extraction_pipeline import ExtractionPipeline
    from .extraction_pipeline_id import ExtractionPipelineId
    from .extraction_pipeline_list_response import ExtractionPipelineListResponse
    from .extraction_pipeline_llm_options import ExtractionPipelineLlmOptions
    from .extraction_pipeline_llm_options_reasoning_effort import ExtractionPipelineLlmOptionsReasoningEffort
    from .extraction_pipeline_llm_options_reasoning_effort_one import ExtractionPipelineLlmOptionsReasoningEffortOne
    from .extraction_pipeline_llm_options_reasoning_effort_zero import ExtractionPipelineLlmOptionsReasoningEffortZero
    from .extraction_review import ExtractionReview
    from .extraction_review_confirmation import ExtractionReviewConfirmation
    from .extraction_review_event import ExtractionReviewEvent
    from .extraction_review_event_one import ExtractionReviewEventOne
    from .extraction_review_event_one_type import ExtractionReviewEventOneType
    from .extraction_review_event_previous_value import ExtractionReviewEventPreviousValue
    from .extraction_review_event_previous_value_type import ExtractionReviewEventPreviousValueType
    from .extraction_review_event_three import ExtractionReviewEventThree
    from .extraction_review_event_three_type import ExtractionReviewEventThreeType
    from .extraction_review_event_two import ExtractionReviewEventTwo
    from .extraction_review_event_two_type import ExtractionReviewEventTwoType
    from .extraction_review_retraction import ExtractionReviewRetraction
    from .extraction_review_status import ExtractionReviewStatus
    from .extraction_terminal_result import ExtractionTerminalResult
    from .extraction_terminal_result_reasoning_effort import ExtractionTerminalResultReasoningEffort
    from .extraction_usage_totals import ExtractionUsageTotals
    from .figure_element import FigureElement
    from .file_id import FileId
    from .formula_element import FormulaElement
    from .formula_format import FormulaFormat
    from .geometry import Geometry
    from .job import Job
    from .job_accepted import JobAccepted
    from .job_accepted_operation import JobAcceptedOperation
    from .job_failure import JobFailure
    from .job_id import JobId
    from .job_list_response import JobListResponse
    from .job_operation import JobOperation
    from .job_progress import JobProgress
    from .job_related_extractions_item import JobRelatedExtractionsItem
    from .job_result import JobResult
    from .job_status import JobStatus
    from .job_summary import JobSummary
    from .json_schema_object import JsonSchemaObject
    from .key_value_element import KeyValueElement
    from .language import Language
    from .lineage_activity import LineageActivity
    from .lineage_activity_status import LineageActivityStatus
    from .lineage_agent import LineageAgent
    from .lineage_association import LineageAssociation
    from .lineage_attribution import LineageAttribution
    from .lineage_confidence_assertion import LineageConfidenceAssertion
    from .lineage_confidence_assertion_kind import LineageConfidenceAssertionKind
    from .lineage_confidence_assertion_sources_item import LineageConfidenceAssertionSourcesItem
    from .lineage_confidence_assertion_sources_item_type import LineageConfidenceAssertionSourcesItemType
    from .lineage_confidence_scale import LineageConfidenceScale
    from .lineage_derivation import LineageDerivation
    from .lineage_derivation_input import LineageDerivationInput
    from .lineage_derivation_input_effect import LineageDerivationInputEffect
    from .lineage_digest import LineageDigest
    from .lineage_document import LineageDocument
    from .lineage_document_format import LineageDocumentFormat
    from .lineage_entity import LineageEntity
    from .lineage_entity_approvals_item import LineageEntityApprovalsItem
    from .lineage_entity_kind import LineageEntityKind
    from .lineage_implementation import LineageImplementation
    from .lineage_locator import LineageLocator
    from .lineage_relation import LineageRelation
    from .lineage_relation_type import LineageRelationType
    from .lineage_selector import LineageSelector
    from .lineage_transformation import LineageTransformation
    from .link_element import LinkElement
    from .llm_model import LlmModel
    from .ocr_llm_model_catalog_entry import OcrLlmModelCatalogEntry
    from .ocr_llm_model_catalog_entry_pricing import OcrLlmModelCatalogEntryPricing
    from .ocr_llm_model_catalog_entry_pricing_basis import OcrLlmModelCatalogEntryPricingBasis
    from .ocr_llm_model_catalog_entry_reasoning import OcrLlmModelCatalogEntryReasoning
    from .ocr_llm_model_catalog_entry_reasoning_default_effort import OcrLlmModelCatalogEntryReasoningDefaultEffort
    from .ocr_llm_model_catalog_entry_reasoning_supported_efforts_item import (
        OcrLlmModelCatalogEntryReasoningSupportedEffortsItem,
    )
    from .ocr_llm_model_catalog_entry_recommendation import OcrLlmModelCatalogEntryRecommendation
    from .ocr_llm_models_response import OcrLlmModelsResponse
    from .ocr_llm_models_response_mode import OcrLlmModelsResponseMode
    from .ocr_model import OcrModel
    from .ocr_model_catalog_entry import OcrModelCatalogEntry
    from .ocr_model_catalog_entry_availability import OcrModelCatalogEntryAvailability
    from .ocr_model_catalog_entry_benchmark import OcrModelCatalogEntryBenchmark
    from .ocr_model_catalog_entry_capabilities import OcrModelCatalogEntryCapabilities
    from .ocr_model_catalog_entry_guidance import OcrModelCatalogEntryGuidance
    from .ocr_model_catalog_entry_option_controls_item import OcrModelCatalogEntryOptionControlsItem
    from .ocr_model_catalog_entry_option_controls_item_choices_item import (
        OcrModelCatalogEntryOptionControlsItemChoicesItem,
    )
    from .ocr_model_catalog_entry_option_controls_item_kind import OcrModelCatalogEntryOptionControlsItemKind
    from .ocr_model_catalog_entry_pricing import OcrModelCatalogEntryPricing
    from .ocr_model_catalog_entry_pricing_basis import OcrModelCatalogEntryPricingBasis
    from .ocr_model_catalog_entry_pricing_configurations_item import OcrModelCatalogEntryPricingConfigurationsItem
    from .ocr_model_catalog_entry_pricing_configurations_item_options_value import (
        OcrModelCatalogEntryPricingConfigurationsItemOptionsValue,
    )
    from .ocr_model_catalog_entry_pricing_configurations_item_options_value_one import (
        OcrModelCatalogEntryPricingConfigurationsItemOptionsValueOne,
    )
    from .ocr_model_catalog_entry_pricing_configurations_item_options_value_two import (
        OcrModelCatalogEntryPricingConfigurationsItemOptionsValueTwo,
    )
    from .ocr_model_catalog_entry_provider import OcrModelCatalogEntryProvider
    from .ocr_model_catalog_entry_provider_logo_data import OcrModelCatalogEntryProviderLogoData
    from .ocr_model_catalog_entry_provider_logo_data_paths_item import OcrModelCatalogEntryProviderLogoDataPathsItem
    from .ocr_model_catalog_entry_provider_logo_data_paths_item_clip_rule import (
        OcrModelCatalogEntryProviderLogoDataPathsItemClipRule,
    )
    from .ocr_models_response import OcrModelsResponse
    from .ocr_output_format import OcrOutputFormat
    from .other_element import OtherElement
    from .parse_batch_item import ParseBatchItem
    from .parse_batch_request import ParseBatchRequest
    from .parse_batch_request_items_item import ParseBatchRequestItemsItem
    from .parse_batch_request_output_format import ParseBatchRequestOutputFormat
    from .parse_request import ParseRequest
    from .parse_request_output_format import ParseRequestOutputFormat
    from .parse_result import ParseResult, ParseResult_Openparser1, ParseResult_Raw
    from .parsed_document import ParsedDocument
    from .parsed_document_output_format import ParsedDocumentOutputFormat
    from .point import Point
    from .polygon import Polygon
    from .public_file import PublicFile
    from .query_answer_element import QueryAnswerElement
    from .raw_parse_result import RawParseResult
    from .raw_parse_result_output_format import RawParseResultOutputFormat
    from .raw_parse_result_profile import RawParseResultProfile
    from .relation_type import RelationType
    from .repair_attempts import RepairAttempts
    from .section_element import SectionElement
    from .section_role import SectionRole
    from .selection_mark_element import SelectionMarkElement
    from .selection_mark_type import SelectionMarkType
    from .selection_state import SelectionState
    from .signature_element import SignatureElement
    from .source_provenance import SourceProvenance
    from .stamp_element import StampElement
    from .structured_value import StructuredValue
    from .suggest_schema_response import SuggestSchemaResponse
    from .table_cell import TableCell
    from .table_cell_role import TableCellRole
    from .table_element import TableElement
    from .text_annotation import TextAnnotation
    from .text_break import TextBreak
    from .text_element import TextElement
    from .text_role import TextRole
    from .text_span import TextSpan
    from .text_style import TextStyle
    from .text_style_font_size_unit import TextStyleFontSizeUnit
_dynamic_imports: typing.Dict[str, str] = {
    "AssetKind": ".asset_kind",
    "BarcodeElement": ".barcode_element",
    "BatchChildPage": ".batch_child_page",
    "BatchChildSummary": ".batch_child_summary",
    "BatchChildSummaryResult": ".batch_child_summary_result",
    "BatchJobAccepted": ".batch_job_accepted",
    "BatchJobAcceptedOperation": ".batch_job_accepted_operation",
    "BatchSummaryCounts": ".batch_summary_counts",
    "BoundingBox": ".bounding_box",
    "Confidence": ".confidence",
    "ConfidenceScope": ".confidence_scope",
    "ConfidenceSourceScale": ".confidence_source_scale",
    "CoordinateUnit": ".coordinate_unit",
    "DeleteExtractionPipelineResponse": ".delete_extraction_pipeline_response",
    "DeleteFileResponse": ".delete_file_response",
    "DocumentAsset": ".document_asset",
    "DocumentElement": ".document_element",
    "DocumentElementKind": ".document_element_kind",
    "DocumentElement_Barcode": ".document_element",
    "DocumentElement_Figure": ".document_element",
    "DocumentElement_Formula": ".document_element",
    "DocumentElement_KeyValue": ".document_element",
    "DocumentElement_Link": ".document_element",
    "DocumentElement_Other": ".document_element",
    "DocumentElement_QueryAnswer": ".document_element",
    "DocumentElement_Section": ".document_element",
    "DocumentElement_SelectionMark": ".document_element",
    "DocumentElement_Signature": ".document_element",
    "DocumentElement_Stamp": ".document_element",
    "DocumentElement_Table": ".document_element",
    "DocumentElement_Text": ".document_element",
    "DocumentPage": ".document_page",
    "DocumentPageQuality": ".document_page_quality",
    "DocumentPageQualityDefectsItem": ".document_page_quality_defects_item",
    "DocumentPageQualityMetricsItem": ".document_page_quality_metrics_item",
    "DocumentPageQualityMetricsItemValue": ".document_page_quality_metrics_item_value",
    "DocumentProvenance": ".document_provenance",
    "DocumentRelation": ".document_relation",
    "ErrorBody": ".error_body",
    "ErrorResponse": ".error_response",
    "ExtractBatchItem": ".extract_batch_item",
    "ExtractBatchItemGrounding": ".extract_batch_item_grounding",
    "ExtractBatchItemLlmOptions": ".extract_batch_item_llm_options",
    "ExtractBatchItemLlmOptionsReasoningEffort": ".extract_batch_item_llm_options_reasoning_effort",
    "ExtractBatchItemLlmOptionsReasoningEffortOne": ".extract_batch_item_llm_options_reasoning_effort_one",
    "ExtractBatchItemLlmOptionsReasoningEffortZero": ".extract_batch_item_llm_options_reasoning_effort_zero",
    "ExtractBatchRequest": ".extract_batch_request",
    "ExtractBatchRequestItemsItem": ".extract_batch_request_items_item",
    "ExtractBatchRequestItemsItemGrounding": ".extract_batch_request_items_item_grounding",
    "ExtractBatchRequestItemsItemLlmOptions": ".extract_batch_request_items_item_llm_options",
    "ExtractBatchRequestItemsItemLlmOptionsReasoningEffort": ".extract_batch_request_items_item_llm_options_reasoning_effort",
    "ExtractBatchRequestItemsItemLlmOptionsReasoningEffortOne": ".extract_batch_request_items_item_llm_options_reasoning_effort_one",
    "ExtractBatchRequestItemsItemLlmOptionsReasoningEffortZero": ".extract_batch_request_items_item_llm_options_reasoning_effort_zero",
    "ExtractBatchRequestOutputFormat": ".extract_batch_request_output_format",
    "ExtractRequest": ".extract_request",
    "ExtractRequestGrounding": ".extract_request_grounding",
    "ExtractRequestLlmOptions": ".extract_request_llm_options",
    "ExtractRequestLlmOptionsReasoningEffort": ".extract_request_llm_options_reasoning_effort",
    "ExtractRequestLlmOptionsReasoningEffortOne": ".extract_request_llm_options_reasoning_effort_one",
    "ExtractRequestLlmOptionsReasoningEffortZero": ".extract_request_llm_options_reasoning_effort_zero",
    "ExtractRequestOutputFormat": ".extract_request_output_format",
    "ExtractionAttempt": ".extraction_attempt",
    "ExtractionAttemptKind": ".extraction_attempt_kind",
    "ExtractionAttemptStatus": ".extraction_attempt_status",
    "ExtractionCitation": ".extraction_citation",
    "ExtractionCitationGranularity": ".extraction_citation_granularity",
    "ExtractionGroundingField": ".extraction_grounding_field",
    "ExtractionGroundingFieldTransformClaim": ".extraction_grounding_field_transform_claim",
    "ExtractionGroundingFieldTransformClaimConfidence": ".extraction_grounding_field_transform_claim_confidence",
    "ExtractionGroundingFieldTransformClaimOperation": ".extraction_grounding_field_transform_claim_operation",
    "ExtractionGroundingFieldTransformClaimParametersValue": ".extraction_grounding_field_transform_claim_parameters_value",
    "ExtractionGroundingMode": ".extraction_grounding_mode",
    "ExtractionGroundingResult": ".extraction_grounding_result",
    "ExtractionGroundingResultMode": ".extraction_grounding_result_mode",
    "ExtractionPipeline": ".extraction_pipeline",
    "ExtractionPipelineId": ".extraction_pipeline_id",
    "ExtractionPipelineListResponse": ".extraction_pipeline_list_response",
    "ExtractionPipelineLlmOptions": ".extraction_pipeline_llm_options",
    "ExtractionPipelineLlmOptionsReasoningEffort": ".extraction_pipeline_llm_options_reasoning_effort",
    "ExtractionPipelineLlmOptionsReasoningEffortOne": ".extraction_pipeline_llm_options_reasoning_effort_one",
    "ExtractionPipelineLlmOptionsReasoningEffortZero": ".extraction_pipeline_llm_options_reasoning_effort_zero",
    "ExtractionReview": ".extraction_review",
    "ExtractionReviewConfirmation": ".extraction_review_confirmation",
    "ExtractionReviewEvent": ".extraction_review_event",
    "ExtractionReviewEventOne": ".extraction_review_event_one",
    "ExtractionReviewEventOneType": ".extraction_review_event_one_type",
    "ExtractionReviewEventPreviousValue": ".extraction_review_event_previous_value",
    "ExtractionReviewEventPreviousValueType": ".extraction_review_event_previous_value_type",
    "ExtractionReviewEventThree": ".extraction_review_event_three",
    "ExtractionReviewEventThreeType": ".extraction_review_event_three_type",
    "ExtractionReviewEventTwo": ".extraction_review_event_two",
    "ExtractionReviewEventTwoType": ".extraction_review_event_two_type",
    "ExtractionReviewRetraction": ".extraction_review_retraction",
    "ExtractionReviewStatus": ".extraction_review_status",
    "ExtractionTerminalResult": ".extraction_terminal_result",
    "ExtractionTerminalResultReasoningEffort": ".extraction_terminal_result_reasoning_effort",
    "ExtractionUsageTotals": ".extraction_usage_totals",
    "FigureElement": ".figure_element",
    "FileId": ".file_id",
    "FormulaElement": ".formula_element",
    "FormulaFormat": ".formula_format",
    "Geometry": ".geometry",
    "Job": ".job",
    "JobAccepted": ".job_accepted",
    "JobAcceptedOperation": ".job_accepted_operation",
    "JobFailure": ".job_failure",
    "JobId": ".job_id",
    "JobListResponse": ".job_list_response",
    "JobOperation": ".job_operation",
    "JobProgress": ".job_progress",
    "JobRelatedExtractionsItem": ".job_related_extractions_item",
    "JobResult": ".job_result",
    "JobStatus": ".job_status",
    "JobSummary": ".job_summary",
    "JsonSchemaObject": ".json_schema_object",
    "KeyValueElement": ".key_value_element",
    "Language": ".language",
    "LineageActivity": ".lineage_activity",
    "LineageActivityStatus": ".lineage_activity_status",
    "LineageAgent": ".lineage_agent",
    "LineageAssociation": ".lineage_association",
    "LineageAttribution": ".lineage_attribution",
    "LineageConfidenceAssertion": ".lineage_confidence_assertion",
    "LineageConfidenceAssertionKind": ".lineage_confidence_assertion_kind",
    "LineageConfidenceAssertionSourcesItem": ".lineage_confidence_assertion_sources_item",
    "LineageConfidenceAssertionSourcesItemType": ".lineage_confidence_assertion_sources_item_type",
    "LineageConfidenceScale": ".lineage_confidence_scale",
    "LineageDerivation": ".lineage_derivation",
    "LineageDerivationInput": ".lineage_derivation_input",
    "LineageDerivationInputEffect": ".lineage_derivation_input_effect",
    "LineageDigest": ".lineage_digest",
    "LineageDocument": ".lineage_document",
    "LineageDocumentFormat": ".lineage_document_format",
    "LineageEntity": ".lineage_entity",
    "LineageEntityApprovalsItem": ".lineage_entity_approvals_item",
    "LineageEntityKind": ".lineage_entity_kind",
    "LineageImplementation": ".lineage_implementation",
    "LineageLocator": ".lineage_locator",
    "LineageRelation": ".lineage_relation",
    "LineageRelationType": ".lineage_relation_type",
    "LineageSelector": ".lineage_selector",
    "LineageTransformation": ".lineage_transformation",
    "LinkElement": ".link_element",
    "LlmModel": ".llm_model",
    "OcrLlmModelCatalogEntry": ".ocr_llm_model_catalog_entry",
    "OcrLlmModelCatalogEntryPricing": ".ocr_llm_model_catalog_entry_pricing",
    "OcrLlmModelCatalogEntryPricingBasis": ".ocr_llm_model_catalog_entry_pricing_basis",
    "OcrLlmModelCatalogEntryReasoning": ".ocr_llm_model_catalog_entry_reasoning",
    "OcrLlmModelCatalogEntryReasoningDefaultEffort": ".ocr_llm_model_catalog_entry_reasoning_default_effort",
    "OcrLlmModelCatalogEntryReasoningSupportedEffortsItem": ".ocr_llm_model_catalog_entry_reasoning_supported_efforts_item",
    "OcrLlmModelCatalogEntryRecommendation": ".ocr_llm_model_catalog_entry_recommendation",
    "OcrLlmModelsResponse": ".ocr_llm_models_response",
    "OcrLlmModelsResponseMode": ".ocr_llm_models_response_mode",
    "OcrModel": ".ocr_model",
    "OcrModelCatalogEntry": ".ocr_model_catalog_entry",
    "OcrModelCatalogEntryAvailability": ".ocr_model_catalog_entry_availability",
    "OcrModelCatalogEntryBenchmark": ".ocr_model_catalog_entry_benchmark",
    "OcrModelCatalogEntryCapabilities": ".ocr_model_catalog_entry_capabilities",
    "OcrModelCatalogEntryGuidance": ".ocr_model_catalog_entry_guidance",
    "OcrModelCatalogEntryOptionControlsItem": ".ocr_model_catalog_entry_option_controls_item",
    "OcrModelCatalogEntryOptionControlsItemChoicesItem": ".ocr_model_catalog_entry_option_controls_item_choices_item",
    "OcrModelCatalogEntryOptionControlsItemKind": ".ocr_model_catalog_entry_option_controls_item_kind",
    "OcrModelCatalogEntryPricing": ".ocr_model_catalog_entry_pricing",
    "OcrModelCatalogEntryPricingBasis": ".ocr_model_catalog_entry_pricing_basis",
    "OcrModelCatalogEntryPricingConfigurationsItem": ".ocr_model_catalog_entry_pricing_configurations_item",
    "OcrModelCatalogEntryPricingConfigurationsItemOptionsValue": ".ocr_model_catalog_entry_pricing_configurations_item_options_value",
    "OcrModelCatalogEntryPricingConfigurationsItemOptionsValueOne": ".ocr_model_catalog_entry_pricing_configurations_item_options_value_one",
    "OcrModelCatalogEntryPricingConfigurationsItemOptionsValueTwo": ".ocr_model_catalog_entry_pricing_configurations_item_options_value_two",
    "OcrModelCatalogEntryProvider": ".ocr_model_catalog_entry_provider",
    "OcrModelCatalogEntryProviderLogoData": ".ocr_model_catalog_entry_provider_logo_data",
    "OcrModelCatalogEntryProviderLogoDataPathsItem": ".ocr_model_catalog_entry_provider_logo_data_paths_item",
    "OcrModelCatalogEntryProviderLogoDataPathsItemClipRule": ".ocr_model_catalog_entry_provider_logo_data_paths_item_clip_rule",
    "OcrModelsResponse": ".ocr_models_response",
    "OcrOutputFormat": ".ocr_output_format",
    "OtherElement": ".other_element",
    "ParseBatchItem": ".parse_batch_item",
    "ParseBatchRequest": ".parse_batch_request",
    "ParseBatchRequestItemsItem": ".parse_batch_request_items_item",
    "ParseBatchRequestOutputFormat": ".parse_batch_request_output_format",
    "ParseRequest": ".parse_request",
    "ParseRequestOutputFormat": ".parse_request_output_format",
    "ParseResult": ".parse_result",
    "ParseResult_Openparser1": ".parse_result",
    "ParseResult_Raw": ".parse_result",
    "ParsedDocument": ".parsed_document",
    "ParsedDocumentOutputFormat": ".parsed_document_output_format",
    "Point": ".point",
    "Polygon": ".polygon",
    "PublicFile": ".public_file",
    "QueryAnswerElement": ".query_answer_element",
    "RawParseResult": ".raw_parse_result",
    "RawParseResultOutputFormat": ".raw_parse_result_output_format",
    "RawParseResultProfile": ".raw_parse_result_profile",
    "RelationType": ".relation_type",
    "RepairAttempts": ".repair_attempts",
    "SectionElement": ".section_element",
    "SectionRole": ".section_role",
    "SelectionMarkElement": ".selection_mark_element",
    "SelectionMarkType": ".selection_mark_type",
    "SelectionState": ".selection_state",
    "SignatureElement": ".signature_element",
    "SourceProvenance": ".source_provenance",
    "StampElement": ".stamp_element",
    "StructuredValue": ".structured_value",
    "SuggestSchemaResponse": ".suggest_schema_response",
    "TableCell": ".table_cell",
    "TableCellRole": ".table_cell_role",
    "TableElement": ".table_element",
    "TextAnnotation": ".text_annotation",
    "TextBreak": ".text_break",
    "TextElement": ".text_element",
    "TextRole": ".text_role",
    "TextSpan": ".text_span",
    "TextStyle": ".text_style",
    "TextStyleFontSizeUnit": ".text_style_font_size_unit",
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
    "AssetKind",
    "BarcodeElement",
    "BatchChildPage",
    "BatchChildSummary",
    "BatchChildSummaryResult",
    "BatchJobAccepted",
    "BatchJobAcceptedOperation",
    "BatchSummaryCounts",
    "BoundingBox",
    "Confidence",
    "ConfidenceScope",
    "ConfidenceSourceScale",
    "CoordinateUnit",
    "DeleteExtractionPipelineResponse",
    "DeleteFileResponse",
    "DocumentAsset",
    "DocumentElement",
    "DocumentElementKind",
    "DocumentElement_Barcode",
    "DocumentElement_Figure",
    "DocumentElement_Formula",
    "DocumentElement_KeyValue",
    "DocumentElement_Link",
    "DocumentElement_Other",
    "DocumentElement_QueryAnswer",
    "DocumentElement_Section",
    "DocumentElement_SelectionMark",
    "DocumentElement_Signature",
    "DocumentElement_Stamp",
    "DocumentElement_Table",
    "DocumentElement_Text",
    "DocumentPage",
    "DocumentPageQuality",
    "DocumentPageQualityDefectsItem",
    "DocumentPageQualityMetricsItem",
    "DocumentPageQualityMetricsItemValue",
    "DocumentProvenance",
    "DocumentRelation",
    "ErrorBody",
    "ErrorResponse",
    "ExtractBatchItem",
    "ExtractBatchItemGrounding",
    "ExtractBatchItemLlmOptions",
    "ExtractBatchItemLlmOptionsReasoningEffort",
    "ExtractBatchItemLlmOptionsReasoningEffortOne",
    "ExtractBatchItemLlmOptionsReasoningEffortZero",
    "ExtractBatchRequest",
    "ExtractBatchRequestItemsItem",
    "ExtractBatchRequestItemsItemGrounding",
    "ExtractBatchRequestItemsItemLlmOptions",
    "ExtractBatchRequestItemsItemLlmOptionsReasoningEffort",
    "ExtractBatchRequestItemsItemLlmOptionsReasoningEffortOne",
    "ExtractBatchRequestItemsItemLlmOptionsReasoningEffortZero",
    "ExtractBatchRequestOutputFormat",
    "ExtractRequest",
    "ExtractRequestGrounding",
    "ExtractRequestLlmOptions",
    "ExtractRequestLlmOptionsReasoningEffort",
    "ExtractRequestLlmOptionsReasoningEffortOne",
    "ExtractRequestLlmOptionsReasoningEffortZero",
    "ExtractRequestOutputFormat",
    "ExtractionAttempt",
    "ExtractionAttemptKind",
    "ExtractionAttemptStatus",
    "ExtractionCitation",
    "ExtractionCitationGranularity",
    "ExtractionGroundingField",
    "ExtractionGroundingFieldTransformClaim",
    "ExtractionGroundingFieldTransformClaimConfidence",
    "ExtractionGroundingFieldTransformClaimOperation",
    "ExtractionGroundingFieldTransformClaimParametersValue",
    "ExtractionGroundingMode",
    "ExtractionGroundingResult",
    "ExtractionGroundingResultMode",
    "ExtractionPipeline",
    "ExtractionPipelineId",
    "ExtractionPipelineListResponse",
    "ExtractionPipelineLlmOptions",
    "ExtractionPipelineLlmOptionsReasoningEffort",
    "ExtractionPipelineLlmOptionsReasoningEffortOne",
    "ExtractionPipelineLlmOptionsReasoningEffortZero",
    "ExtractionReview",
    "ExtractionReviewConfirmation",
    "ExtractionReviewEvent",
    "ExtractionReviewEventOne",
    "ExtractionReviewEventOneType",
    "ExtractionReviewEventPreviousValue",
    "ExtractionReviewEventPreviousValueType",
    "ExtractionReviewEventThree",
    "ExtractionReviewEventThreeType",
    "ExtractionReviewEventTwo",
    "ExtractionReviewEventTwoType",
    "ExtractionReviewRetraction",
    "ExtractionReviewStatus",
    "ExtractionTerminalResult",
    "ExtractionTerminalResultReasoningEffort",
    "ExtractionUsageTotals",
    "FigureElement",
    "FileId",
    "FormulaElement",
    "FormulaFormat",
    "Geometry",
    "Job",
    "JobAccepted",
    "JobAcceptedOperation",
    "JobFailure",
    "JobId",
    "JobListResponse",
    "JobOperation",
    "JobProgress",
    "JobRelatedExtractionsItem",
    "JobResult",
    "JobStatus",
    "JobSummary",
    "JsonSchemaObject",
    "KeyValueElement",
    "Language",
    "LineageActivity",
    "LineageActivityStatus",
    "LineageAgent",
    "LineageAssociation",
    "LineageAttribution",
    "LineageConfidenceAssertion",
    "LineageConfidenceAssertionKind",
    "LineageConfidenceAssertionSourcesItem",
    "LineageConfidenceAssertionSourcesItemType",
    "LineageConfidenceScale",
    "LineageDerivation",
    "LineageDerivationInput",
    "LineageDerivationInputEffect",
    "LineageDigest",
    "LineageDocument",
    "LineageDocumentFormat",
    "LineageEntity",
    "LineageEntityApprovalsItem",
    "LineageEntityKind",
    "LineageImplementation",
    "LineageLocator",
    "LineageRelation",
    "LineageRelationType",
    "LineageSelector",
    "LineageTransformation",
    "LinkElement",
    "LlmModel",
    "OcrLlmModelCatalogEntry",
    "OcrLlmModelCatalogEntryPricing",
    "OcrLlmModelCatalogEntryPricingBasis",
    "OcrLlmModelCatalogEntryReasoning",
    "OcrLlmModelCatalogEntryReasoningDefaultEffort",
    "OcrLlmModelCatalogEntryReasoningSupportedEffortsItem",
    "OcrLlmModelCatalogEntryRecommendation",
    "OcrLlmModelsResponse",
    "OcrLlmModelsResponseMode",
    "OcrModel",
    "OcrModelCatalogEntry",
    "OcrModelCatalogEntryAvailability",
    "OcrModelCatalogEntryBenchmark",
    "OcrModelCatalogEntryCapabilities",
    "OcrModelCatalogEntryGuidance",
    "OcrModelCatalogEntryOptionControlsItem",
    "OcrModelCatalogEntryOptionControlsItemChoicesItem",
    "OcrModelCatalogEntryOptionControlsItemKind",
    "OcrModelCatalogEntryPricing",
    "OcrModelCatalogEntryPricingBasis",
    "OcrModelCatalogEntryPricingConfigurationsItem",
    "OcrModelCatalogEntryPricingConfigurationsItemOptionsValue",
    "OcrModelCatalogEntryPricingConfigurationsItemOptionsValueOne",
    "OcrModelCatalogEntryPricingConfigurationsItemOptionsValueTwo",
    "OcrModelCatalogEntryProvider",
    "OcrModelCatalogEntryProviderLogoData",
    "OcrModelCatalogEntryProviderLogoDataPathsItem",
    "OcrModelCatalogEntryProviderLogoDataPathsItemClipRule",
    "OcrModelsResponse",
    "OcrOutputFormat",
    "OtherElement",
    "ParseBatchItem",
    "ParseBatchRequest",
    "ParseBatchRequestItemsItem",
    "ParseBatchRequestOutputFormat",
    "ParseRequest",
    "ParseRequestOutputFormat",
    "ParseResult",
    "ParseResult_Openparser1",
    "ParseResult_Raw",
    "ParsedDocument",
    "ParsedDocumentOutputFormat",
    "Point",
    "Polygon",
    "PublicFile",
    "QueryAnswerElement",
    "RawParseResult",
    "RawParseResultOutputFormat",
    "RawParseResultProfile",
    "RelationType",
    "RepairAttempts",
    "SectionElement",
    "SectionRole",
    "SelectionMarkElement",
    "SelectionMarkType",
    "SelectionState",
    "SignatureElement",
    "SourceProvenance",
    "StampElement",
    "StructuredValue",
    "SuggestSchemaResponse",
    "TableCell",
    "TableCellRole",
    "TableElement",
    "TextAnnotation",
    "TextBreak",
    "TextElement",
    "TextRole",
    "TextSpan",
    "TextStyle",
    "TextStyleFontSizeUnit",
]
