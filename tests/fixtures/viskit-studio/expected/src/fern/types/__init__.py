



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .asset_delete_response import AssetDeleteResponse
    from .asset_edit_context import AssetEditContext
    from .asset_list_response import AssetListResponse
    from .asset_out import AssetOut
    from .compliance_out import ComplianceOut
    from .config_state_response import ConfigStateResponse
    from .delete_kit_image_response import DeleteKitImageResponse
    from .detail_section_in import DetailSectionIn
    from .detail_section_in_id import DetailSectionInId
    from .detail_section_out import DetailSectionOut
    from .detail_section_out_id import DetailSectionOutId
    from .edit_accepted import EditAccepted
    from .edit_result_out import EditResultOut
    from .editor_project_response import EditorProjectResponse
    from .editor_project_save_request import EditorProjectSaveRequest
    from .endpoint_secret_response import EndpointSecretResponse
    from .endpoint_stanza import EndpointStanza
    from .extract_response import ExtractResponse
    from .field_inference import FieldInference
    from .generate_response import GenerateResponse
    from .generation_job_created import GenerationJobCreated
    from .generation_job_created_status import GenerationJobCreatedStatus
    from .generation_job_list_response import GenerationJobListResponse
    from .generation_job_out import GenerationJobOut
    from .generation_job_out_status import GenerationJobOutStatus
    from .generation_job_start_response import GenerationJobStartResponse
    from .generation_job_start_response_status import GenerationJobStartResponseStatus
    from .generation_job_stop_response import GenerationJobStopResponse
    from .generation_job_stop_response_status import GenerationJobStopResponseStatus
    from .generation_output_create import GenerationOutputCreate
    from .generation_output_create_destination_type import GenerationOutputCreateDestinationType
    from .generation_output_create_output_kind import GenerationOutputCreateOutputKind
    from .generation_output_out import GenerationOutputOut
    from .generation_plan_item_out import GenerationPlanItemOut
    from .generation_plan_item_out_destination_type import GenerationPlanItemOutDestinationType
    from .generation_plan_out import GenerationPlanOut
    from .generation_plan_out_plan_source import GenerationPlanOutPlanSource
    from .hero_section_in import HeroSectionIn
    from .hero_section_in_id import HeroSectionInId
    from .hero_section_out import HeroSectionOut
    from .hero_section_out_id import HeroSectionOutId
    from .http_validation_error import HttpValidationError
    from .kit_list_item import KitListItem
    from .kit_list_item_source_type import KitListItemSourceType
    from .kit_list_response import KitListResponse
    from .kit_meta_response import KitMetaResponse
    from .ocr_response import OcrResponse
    from .onboarding_needed_response import OnboardingNeededResponse
    from .preview_response import PreviewResponse
    from .probe_candidate_response import ProbeCandidateResponse
    from .product_profile_in import ProductProfileIn
    from .provider_health_row import ProviderHealthRow
    from .provider_health_row_status import ProviderHealthRowStatus
    from .provider_probe_response import ProviderProbeResponse
    from .provider_probe_row import ProviderProbeRow
    from .providers_summary_response import ProvidersSummaryResponse
    from .queue_job import QueueJob
    from .queue_job_stages_item import QueueJobStagesItem
    from .save_endpoints_response import SaveEndpointsResponse
    from .save_image_response import SaveImageResponse
    from .save_image_response_mode import SaveImageResponseMode
    from .scheme_slot import SchemeSlot
    from .scheme_slot_slot_id import SchemeSlotSlotId
    from .scheme_summary import SchemeSummary
    from .scheme_summary_locale import SchemeSummaryLocale
    from .scheme_summary_source import SchemeSummarySource
    from .selling_point_in import SellingPointIn
    from .selling_point_in_priority import SellingPointInPriority
    from .settings_response import SettingsResponse
    from .sku_meta_in import SkuMetaIn
    from .sku_meta_in_product_type import SkuMetaInProductType
    from .source_image_import_out import SourceImageImportOut
    from .source_image_out import SourceImageOut
    from .sparks import Sparks
    from .spec_in import SpecIn
    from .spec_in_locale import SpecInLocale
    from .spec_out import SpecOut
    from .spec_out_locale import SpecOutLocale
    from .spec_response import SpecResponse
    from .store_secret_response import StoreSecretResponse
    from .template_summary import TemplateSummary
    from .template_summary_category import TemplateSummaryCategory
    from .template_summary_locale import TemplateSummaryLocale
    from .template_summary_source import TemplateSummarySource
    from .text_box_out import TextBoxOut
    from .three_piece_in import ThreePieceIn
    from .three_piece_out import ThreePieceOut
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
    from .violation_out import ViolationOut
    from .violation_out_severity import ViolationOutSeverity
    from .weekly_metrics_response import WeeklyMetricsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AssetDeleteResponse": ".asset_delete_response",
    "AssetEditContext": ".asset_edit_context",
    "AssetListResponse": ".asset_list_response",
    "AssetOut": ".asset_out",
    "ComplianceOut": ".compliance_out",
    "ConfigStateResponse": ".config_state_response",
    "DeleteKitImageResponse": ".delete_kit_image_response",
    "DetailSectionIn": ".detail_section_in",
    "DetailSectionInId": ".detail_section_in_id",
    "DetailSectionOut": ".detail_section_out",
    "DetailSectionOutId": ".detail_section_out_id",
    "EditAccepted": ".edit_accepted",
    "EditResultOut": ".edit_result_out",
    "EditorProjectResponse": ".editor_project_response",
    "EditorProjectSaveRequest": ".editor_project_save_request",
    "EndpointSecretResponse": ".endpoint_secret_response",
    "EndpointStanza": ".endpoint_stanza",
    "ExtractResponse": ".extract_response",
    "FieldInference": ".field_inference",
    "GenerateResponse": ".generate_response",
    "GenerationJobCreated": ".generation_job_created",
    "GenerationJobCreatedStatus": ".generation_job_created_status",
    "GenerationJobListResponse": ".generation_job_list_response",
    "GenerationJobOut": ".generation_job_out",
    "GenerationJobOutStatus": ".generation_job_out_status",
    "GenerationJobStartResponse": ".generation_job_start_response",
    "GenerationJobStartResponseStatus": ".generation_job_start_response_status",
    "GenerationJobStopResponse": ".generation_job_stop_response",
    "GenerationJobStopResponseStatus": ".generation_job_stop_response_status",
    "GenerationOutputCreate": ".generation_output_create",
    "GenerationOutputCreateDestinationType": ".generation_output_create_destination_type",
    "GenerationOutputCreateOutputKind": ".generation_output_create_output_kind",
    "GenerationOutputOut": ".generation_output_out",
    "GenerationPlanItemOut": ".generation_plan_item_out",
    "GenerationPlanItemOutDestinationType": ".generation_plan_item_out_destination_type",
    "GenerationPlanOut": ".generation_plan_out",
    "GenerationPlanOutPlanSource": ".generation_plan_out_plan_source",
    "HeroSectionIn": ".hero_section_in",
    "HeroSectionInId": ".hero_section_in_id",
    "HeroSectionOut": ".hero_section_out",
    "HeroSectionOutId": ".hero_section_out_id",
    "HttpValidationError": ".http_validation_error",
    "KitListItem": ".kit_list_item",
    "KitListItemSourceType": ".kit_list_item_source_type",
    "KitListResponse": ".kit_list_response",
    "KitMetaResponse": ".kit_meta_response",
    "OcrResponse": ".ocr_response",
    "OnboardingNeededResponse": ".onboarding_needed_response",
    "PreviewResponse": ".preview_response",
    "ProbeCandidateResponse": ".probe_candidate_response",
    "ProductProfileIn": ".product_profile_in",
    "ProviderHealthRow": ".provider_health_row",
    "ProviderHealthRowStatus": ".provider_health_row_status",
    "ProviderProbeResponse": ".provider_probe_response",
    "ProviderProbeRow": ".provider_probe_row",
    "ProvidersSummaryResponse": ".providers_summary_response",
    "QueueJob": ".queue_job",
    "QueueJobStagesItem": ".queue_job_stages_item",
    "SaveEndpointsResponse": ".save_endpoints_response",
    "SaveImageResponse": ".save_image_response",
    "SaveImageResponseMode": ".save_image_response_mode",
    "SchemeSlot": ".scheme_slot",
    "SchemeSlotSlotId": ".scheme_slot_slot_id",
    "SchemeSummary": ".scheme_summary",
    "SchemeSummaryLocale": ".scheme_summary_locale",
    "SchemeSummarySource": ".scheme_summary_source",
    "SellingPointIn": ".selling_point_in",
    "SellingPointInPriority": ".selling_point_in_priority",
    "SettingsResponse": ".settings_response",
    "SkuMetaIn": ".sku_meta_in",
    "SkuMetaInProductType": ".sku_meta_in_product_type",
    "SourceImageImportOut": ".source_image_import_out",
    "SourceImageOut": ".source_image_out",
    "Sparks": ".sparks",
    "SpecIn": ".spec_in",
    "SpecInLocale": ".spec_in_locale",
    "SpecOut": ".spec_out",
    "SpecOutLocale": ".spec_out_locale",
    "SpecResponse": ".spec_response",
    "StoreSecretResponse": ".store_secret_response",
    "TemplateSummary": ".template_summary",
    "TemplateSummaryCategory": ".template_summary_category",
    "TemplateSummaryLocale": ".template_summary_locale",
    "TemplateSummarySource": ".template_summary_source",
    "TextBoxOut": ".text_box_out",
    "ThreePieceIn": ".three_piece_in",
    "ThreePieceOut": ".three_piece_out",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
    "ViolationOut": ".violation_out",
    "ViolationOutSeverity": ".violation_out_severity",
    "WeeklyMetricsResponse": ".weekly_metrics_response",
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
    "AssetDeleteResponse",
    "AssetEditContext",
    "AssetListResponse",
    "AssetOut",
    "ComplianceOut",
    "ConfigStateResponse",
    "DeleteKitImageResponse",
    "DetailSectionIn",
    "DetailSectionInId",
    "DetailSectionOut",
    "DetailSectionOutId",
    "EditAccepted",
    "EditResultOut",
    "EditorProjectResponse",
    "EditorProjectSaveRequest",
    "EndpointSecretResponse",
    "EndpointStanza",
    "ExtractResponse",
    "FieldInference",
    "GenerateResponse",
    "GenerationJobCreated",
    "GenerationJobCreatedStatus",
    "GenerationJobListResponse",
    "GenerationJobOut",
    "GenerationJobOutStatus",
    "GenerationJobStartResponse",
    "GenerationJobStartResponseStatus",
    "GenerationJobStopResponse",
    "GenerationJobStopResponseStatus",
    "GenerationOutputCreate",
    "GenerationOutputCreateDestinationType",
    "GenerationOutputCreateOutputKind",
    "GenerationOutputOut",
    "GenerationPlanItemOut",
    "GenerationPlanItemOutDestinationType",
    "GenerationPlanOut",
    "GenerationPlanOutPlanSource",
    "HeroSectionIn",
    "HeroSectionInId",
    "HeroSectionOut",
    "HeroSectionOutId",
    "HttpValidationError",
    "KitListItem",
    "KitListItemSourceType",
    "KitListResponse",
    "KitMetaResponse",
    "OcrResponse",
    "OnboardingNeededResponse",
    "PreviewResponse",
    "ProbeCandidateResponse",
    "ProductProfileIn",
    "ProviderHealthRow",
    "ProviderHealthRowStatus",
    "ProviderProbeResponse",
    "ProviderProbeRow",
    "ProvidersSummaryResponse",
    "QueueJob",
    "QueueJobStagesItem",
    "SaveEndpointsResponse",
    "SaveImageResponse",
    "SaveImageResponseMode",
    "SchemeSlot",
    "SchemeSlotSlotId",
    "SchemeSummary",
    "SchemeSummaryLocale",
    "SchemeSummarySource",
    "SellingPointIn",
    "SellingPointInPriority",
    "SettingsResponse",
    "SkuMetaIn",
    "SkuMetaInProductType",
    "SourceImageImportOut",
    "SourceImageOut",
    "Sparks",
    "SpecIn",
    "SpecInLocale",
    "SpecOut",
    "SpecOutLocale",
    "SpecResponse",
    "StoreSecretResponse",
    "TemplateSummary",
    "TemplateSummaryCategory",
    "TemplateSummaryLocale",
    "TemplateSummarySource",
    "TextBoxOut",
    "ThreePieceIn",
    "ThreePieceOut",
    "ValidationError",
    "ValidationErrorLocItem",
    "ViolationOut",
    "ViolationOutSeverity",
    "WeeklyMetricsResponse",
]
