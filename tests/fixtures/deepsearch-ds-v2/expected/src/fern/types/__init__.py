



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .acquisition import Acquisition
    from .acquisition_type import AcquisitionType
    from .affiliation import Affiliation
    from .api_server_fastapi_server_public_models_data_indices_upload_models_http_source import (
        ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource,
    )
    from .api_server_fastapi_server_public_models_data_indices_upload_models_identifier import (
        ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier,
    )
    from .api_server_fastapi_server_public_models_project_models_http_source import (
        ApiServerFastapiServerPublicModelsProjectModelsHttpSource,
    )
    from .assemble_mode import AssembleMode
    from .assemble_mode_page_elements_item import AssembleModePageElementsItem
    from .assemble_mode_tables_item import AssembleModeTablesItem
    from .assemble_settings import AssembleSettings
    from .attachment_upload_data import AttachmentUploadData
    from .author import Author
    from .bag_flavour_full_data import BagFlavourFullData
    from .base_model import BaseModel
    from .ccs_project import CcsProject
    from .collection_document_info_str import CollectionDocumentInfoStr
    from .collection_document_info_str_type import CollectionDocumentInfoStrType
    from .collection_metadata_settings import CollectionMetadataSettings
    from .cps_package import CpsPackage
    from .cps_package_type import CpsPackageType
    from .cps_summary import CpsSummary
    from .cps_task import CpsTask
    from .data_flow import DataFlow
    from .default_values import DefaultValues
    from .deployment import Deployment
    from .description_license import DescriptionLicense
    from .direct_model_config import DirectModelConfig
    from .docling_core_types_base_identifier import DoclingCoreTypesBaseIdentifier
    from .document_artifacts import DocumentArtifacts
    from .document_artifacts_item import DocumentArtifactsItem
    from .document_artifacts_page_item import DocumentArtifactsPageItem
    from .document_description import DocumentDescription
    from .document_meta import DocumentMeta
    from .document_statistics import DocumentStatistics
    from .elastic_index_property_object import ElasticIndexPropertyObject
    from .elastic_index_property_primitive import ElasticIndexPropertyPrimitive
    from .elastic_index_property_primitive_properties_value import ElasticIndexPropertyPrimitivePropertiesValue
    from .elastic_index_search_query_options import ElasticIndexSearchQueryOptions
    from .elastic_index_source import ElasticIndexSource
    from .elastic_instance_data_index import ElasticInstanceDataIndex
    from .elastic_metadata import ElasticMetadata
    from .file_source import FileSource
    from .flavour import Flavour
    from .flavours_default_quota import FlavoursDefaultQuota
    from .flavours_quota import FlavoursQuota
    from .gen_ai_openai import GenAiOpenai
    from .gen_ai_openai_config import GenAiOpenaiConfig
    from .gen_ai_params import GenAiParams
    from .gen_ai_partial_params import GenAiPartialParams
    from .gen_ai_watsonx import GenAiWatsonx
    from .gen_ai_watsonx_config import GenAiWatsonxConfig
    from .gen_aiaws_bedrock import GenAiawsBedrock
    from .gen_aiaws_bedrock_config import GenAiawsBedrockConfig
    from .gen_aibam import GenAibam
    from .gen_aibam_config import GenAibamConfig
    from .gen_aicpd import GenAicpd
    from .gen_aicpd_config import GenAicpdConfig
    from .gen_aihf_inference_api import GenAihfInferenceApi
    from .gen_aihf_inference_api_config import GenAihfInferenceApiConfig
    from .grouped_project_documents import GroupedProjectDocuments
    from .grouped_project_documents_upload_date import GroupedProjectDocumentsUploadDate
    from .http_validation_error import HttpValidationError
    from .image_urls_info import ImageUrlsInfo
    from .list_project_flavours import ListProjectFlavours
    from .log import Log
    from .model_pipeline_settings import ModelPipelineSettings
    from .model_pipeline_settings_clusters_item import ModelPipelineSettingsClustersItem
    from .model_pipeline_settings_normalization_item import ModelPipelineSettingsNormalizationItem
    from .model_pipeline_settings_page_item import ModelPipelineSettingsPageItem
    from .model_pipeline_settings_tables_item import ModelPipelineSettingsTablesItem
    from .modules_config import ModulesConfig
    from .ocr_options import OcrOptions
    from .ocr_options_kind import OcrOptionsKind
    from .ocr_settings import OcrSettings
    from .package import Package
    from .partial_direct_conversion_parameters import PartialDirectConversionParameters
    from .partial_direct_conversion_parameters_type import PartialDirectConversionParametersType
    from .project_agent import ProjectAgent
    from .project_agents import ProjectAgents
    from .project_data_index_conversion_settings_input import ProjectDataIndexConversionSettingsInput
    from .project_data_index_conversion_settings_output import ProjectDataIndexConversionSettingsOutput
    from .project_data_index_non_view import ProjectDataIndexNonView
    from .project_data_index_non_view_schema_key import ProjectDataIndexNonViewSchemaKey
    from .project_data_index_source import ProjectDataIndexSource
    from .project_data_index_view import ProjectDataIndexView
    from .project_data_index_view_view_of import ProjectDataIndexViewViewOf
    from .project_data_index_with_status import ProjectDataIndexWithStatus
    from .project_data_index_with_status_record_properties_value import ProjectDataIndexWithStatusRecordPropertiesValue
    from .project_data_index_with_status_schema_key import ProjectDataIndexWithStatusSchemaKey
    from .project_data_index_with_status_source import ProjectDataIndexWithStatusSource
    from .project_data_index_with_status_view_of import ProjectDataIndexWithStatusViewOf
    from .project_document import ProjectDocument
    from .project_document_url import ProjectDocumentUrl
    from .project_documents import ProjectDocuments
    from .project_flavour_total_kgs import ProjectFlavourTotalKgs
    from .project_flavours_quota import ProjectFlavoursQuota
    from .project_scratch_files import ProjectScratchFiles
    from .project_scratch_files_paginated import ProjectScratchFilesPaginated
    from .project_source_data_index import ProjectSourceDataIndex
    from .projects_flavours import ProjectsFlavours
    from .publication import Publication
    from .reference_to_model import ReferenceToModel
    from .response_document_artifacts import ResponseDocumentArtifacts
    from .response_grouped_documents import ResponseGroupedDocuments
    from .response_upload_jobs import ResponseUploadJobs
    from .s3coordinates import S3Coordinates
    from .s3document_source import S3DocumentSource
    from .semantic_ingest_req_params import SemanticIngestReqParams
    from .semantic_ingest_source_private_data_collection import SemanticIngestSourcePrivateDataCollection
    from .semantic_ingest_source_private_data_document import SemanticIngestSourcePrivateDataDocument
    from .semantic_ingest_source_public_data_document import SemanticIngestSourcePublicDataDocument
    from .semantic_ingest_source_url import SemanticIngestSourceUrl
    from .status_filter import StatusFilter
    from .storage_summary_task import StorageSummaryTask
    from .storage_summary_task_kind import StorageSummaryTaskKind
    from .system_info import SystemInfo
    from .table_former_mode import TableFormerMode
    from .table_structure_options import TableStructureOptions
    from .target_conversion_parameters import TargetConversionParameters
    from .task_context import TaskContext
    from .task_result import TaskResult
    from .temporary_upload_file_result import TemporaryUploadFileResult
    from .temporary_url import TemporaryUrl
    from .temporary_url_fields import TemporaryUrlFields
    from .token_response import TokenResponse
    from .upload_job import UploadJob
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
_dynamic_imports: typing.Dict[str, str] = {
    "Acquisition": ".acquisition",
    "AcquisitionType": ".acquisition_type",
    "Affiliation": ".affiliation",
    "ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource": ".api_server_fastapi_server_public_models_data_indices_upload_models_http_source",
    "ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier": ".api_server_fastapi_server_public_models_data_indices_upload_models_identifier",
    "ApiServerFastapiServerPublicModelsProjectModelsHttpSource": ".api_server_fastapi_server_public_models_project_models_http_source",
    "AssembleMode": ".assemble_mode",
    "AssembleModePageElementsItem": ".assemble_mode_page_elements_item",
    "AssembleModeTablesItem": ".assemble_mode_tables_item",
    "AssembleSettings": ".assemble_settings",
    "AttachmentUploadData": ".attachment_upload_data",
    "Author": ".author",
    "BagFlavourFullData": ".bag_flavour_full_data",
    "BaseModel": ".base_model",
    "CcsProject": ".ccs_project",
    "CollectionDocumentInfoStr": ".collection_document_info_str",
    "CollectionDocumentInfoStrType": ".collection_document_info_str_type",
    "CollectionMetadataSettings": ".collection_metadata_settings",
    "CpsPackage": ".cps_package",
    "CpsPackageType": ".cps_package_type",
    "CpsSummary": ".cps_summary",
    "CpsTask": ".cps_task",
    "DataFlow": ".data_flow",
    "DefaultValues": ".default_values",
    "Deployment": ".deployment",
    "DescriptionLicense": ".description_license",
    "DirectModelConfig": ".direct_model_config",
    "DoclingCoreTypesBaseIdentifier": ".docling_core_types_base_identifier",
    "DocumentArtifacts": ".document_artifacts",
    "DocumentArtifactsItem": ".document_artifacts_item",
    "DocumentArtifactsPageItem": ".document_artifacts_page_item",
    "DocumentDescription": ".document_description",
    "DocumentMeta": ".document_meta",
    "DocumentStatistics": ".document_statistics",
    "ElasticIndexPropertyObject": ".elastic_index_property_object",
    "ElasticIndexPropertyPrimitive": ".elastic_index_property_primitive",
    "ElasticIndexPropertyPrimitivePropertiesValue": ".elastic_index_property_primitive_properties_value",
    "ElasticIndexSearchQueryOptions": ".elastic_index_search_query_options",
    "ElasticIndexSource": ".elastic_index_source",
    "ElasticInstanceDataIndex": ".elastic_instance_data_index",
    "ElasticMetadata": ".elastic_metadata",
    "FileSource": ".file_source",
    "Flavour": ".flavour",
    "FlavoursDefaultQuota": ".flavours_default_quota",
    "FlavoursQuota": ".flavours_quota",
    "GenAiOpenai": ".gen_ai_openai",
    "GenAiOpenaiConfig": ".gen_ai_openai_config",
    "GenAiParams": ".gen_ai_params",
    "GenAiPartialParams": ".gen_ai_partial_params",
    "GenAiWatsonx": ".gen_ai_watsonx",
    "GenAiWatsonxConfig": ".gen_ai_watsonx_config",
    "GenAiawsBedrock": ".gen_aiaws_bedrock",
    "GenAiawsBedrockConfig": ".gen_aiaws_bedrock_config",
    "GenAibam": ".gen_aibam",
    "GenAibamConfig": ".gen_aibam_config",
    "GenAicpd": ".gen_aicpd",
    "GenAicpdConfig": ".gen_aicpd_config",
    "GenAihfInferenceApi": ".gen_aihf_inference_api",
    "GenAihfInferenceApiConfig": ".gen_aihf_inference_api_config",
    "GroupedProjectDocuments": ".grouped_project_documents",
    "GroupedProjectDocumentsUploadDate": ".grouped_project_documents_upload_date",
    "HttpValidationError": ".http_validation_error",
    "ImageUrlsInfo": ".image_urls_info",
    "ListProjectFlavours": ".list_project_flavours",
    "Log": ".log",
    "ModelPipelineSettings": ".model_pipeline_settings",
    "ModelPipelineSettingsClustersItem": ".model_pipeline_settings_clusters_item",
    "ModelPipelineSettingsNormalizationItem": ".model_pipeline_settings_normalization_item",
    "ModelPipelineSettingsPageItem": ".model_pipeline_settings_page_item",
    "ModelPipelineSettingsTablesItem": ".model_pipeline_settings_tables_item",
    "ModulesConfig": ".modules_config",
    "OcrOptions": ".ocr_options",
    "OcrOptionsKind": ".ocr_options_kind",
    "OcrSettings": ".ocr_settings",
    "Package": ".package",
    "PartialDirectConversionParameters": ".partial_direct_conversion_parameters",
    "PartialDirectConversionParametersType": ".partial_direct_conversion_parameters_type",
    "ProjectAgent": ".project_agent",
    "ProjectAgents": ".project_agents",
    "ProjectDataIndexConversionSettingsInput": ".project_data_index_conversion_settings_input",
    "ProjectDataIndexConversionSettingsOutput": ".project_data_index_conversion_settings_output",
    "ProjectDataIndexNonView": ".project_data_index_non_view",
    "ProjectDataIndexNonViewSchemaKey": ".project_data_index_non_view_schema_key",
    "ProjectDataIndexSource": ".project_data_index_source",
    "ProjectDataIndexView": ".project_data_index_view",
    "ProjectDataIndexViewViewOf": ".project_data_index_view_view_of",
    "ProjectDataIndexWithStatus": ".project_data_index_with_status",
    "ProjectDataIndexWithStatusRecordPropertiesValue": ".project_data_index_with_status_record_properties_value",
    "ProjectDataIndexWithStatusSchemaKey": ".project_data_index_with_status_schema_key",
    "ProjectDataIndexWithStatusSource": ".project_data_index_with_status_source",
    "ProjectDataIndexWithStatusViewOf": ".project_data_index_with_status_view_of",
    "ProjectDocument": ".project_document",
    "ProjectDocumentUrl": ".project_document_url",
    "ProjectDocuments": ".project_documents",
    "ProjectFlavourTotalKgs": ".project_flavour_total_kgs",
    "ProjectFlavoursQuota": ".project_flavours_quota",
    "ProjectScratchFiles": ".project_scratch_files",
    "ProjectScratchFilesPaginated": ".project_scratch_files_paginated",
    "ProjectSourceDataIndex": ".project_source_data_index",
    "ProjectsFlavours": ".projects_flavours",
    "Publication": ".publication",
    "ReferenceToModel": ".reference_to_model",
    "ResponseDocumentArtifacts": ".response_document_artifacts",
    "ResponseGroupedDocuments": ".response_grouped_documents",
    "ResponseUploadJobs": ".response_upload_jobs",
    "S3Coordinates": ".s3coordinates",
    "S3DocumentSource": ".s3document_source",
    "SemanticIngestReqParams": ".semantic_ingest_req_params",
    "SemanticIngestSourcePrivateDataCollection": ".semantic_ingest_source_private_data_collection",
    "SemanticIngestSourcePrivateDataDocument": ".semantic_ingest_source_private_data_document",
    "SemanticIngestSourcePublicDataDocument": ".semantic_ingest_source_public_data_document",
    "SemanticIngestSourceUrl": ".semantic_ingest_source_url",
    "StatusFilter": ".status_filter",
    "StorageSummaryTask": ".storage_summary_task",
    "StorageSummaryTaskKind": ".storage_summary_task_kind",
    "SystemInfo": ".system_info",
    "TableFormerMode": ".table_former_mode",
    "TableStructureOptions": ".table_structure_options",
    "TargetConversionParameters": ".target_conversion_parameters",
    "TaskContext": ".task_context",
    "TaskResult": ".task_result",
    "TemporaryUploadFileResult": ".temporary_upload_file_result",
    "TemporaryUrl": ".temporary_url",
    "TemporaryUrlFields": ".temporary_url_fields",
    "TokenResponse": ".token_response",
    "UploadJob": ".upload_job",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
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
    "Acquisition",
    "AcquisitionType",
    "Affiliation",
    "ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource",
    "ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier",
    "ApiServerFastapiServerPublicModelsProjectModelsHttpSource",
    "AssembleMode",
    "AssembleModePageElementsItem",
    "AssembleModeTablesItem",
    "AssembleSettings",
    "AttachmentUploadData",
    "Author",
    "BagFlavourFullData",
    "BaseModel",
    "CcsProject",
    "CollectionDocumentInfoStr",
    "CollectionDocumentInfoStrType",
    "CollectionMetadataSettings",
    "CpsPackage",
    "CpsPackageType",
    "CpsSummary",
    "CpsTask",
    "DataFlow",
    "DefaultValues",
    "Deployment",
    "DescriptionLicense",
    "DirectModelConfig",
    "DoclingCoreTypesBaseIdentifier",
    "DocumentArtifacts",
    "DocumentArtifactsItem",
    "DocumentArtifactsPageItem",
    "DocumentDescription",
    "DocumentMeta",
    "DocumentStatistics",
    "ElasticIndexPropertyObject",
    "ElasticIndexPropertyPrimitive",
    "ElasticIndexPropertyPrimitivePropertiesValue",
    "ElasticIndexSearchQueryOptions",
    "ElasticIndexSource",
    "ElasticInstanceDataIndex",
    "ElasticMetadata",
    "FileSource",
    "Flavour",
    "FlavoursDefaultQuota",
    "FlavoursQuota",
    "GenAiOpenai",
    "GenAiOpenaiConfig",
    "GenAiParams",
    "GenAiPartialParams",
    "GenAiWatsonx",
    "GenAiWatsonxConfig",
    "GenAiawsBedrock",
    "GenAiawsBedrockConfig",
    "GenAibam",
    "GenAibamConfig",
    "GenAicpd",
    "GenAicpdConfig",
    "GenAihfInferenceApi",
    "GenAihfInferenceApiConfig",
    "GroupedProjectDocuments",
    "GroupedProjectDocumentsUploadDate",
    "HttpValidationError",
    "ImageUrlsInfo",
    "ListProjectFlavours",
    "Log",
    "ModelPipelineSettings",
    "ModelPipelineSettingsClustersItem",
    "ModelPipelineSettingsNormalizationItem",
    "ModelPipelineSettingsPageItem",
    "ModelPipelineSettingsTablesItem",
    "ModulesConfig",
    "OcrOptions",
    "OcrOptionsKind",
    "OcrSettings",
    "Package",
    "PartialDirectConversionParameters",
    "PartialDirectConversionParametersType",
    "ProjectAgent",
    "ProjectAgents",
    "ProjectDataIndexConversionSettingsInput",
    "ProjectDataIndexConversionSettingsOutput",
    "ProjectDataIndexNonView",
    "ProjectDataIndexNonViewSchemaKey",
    "ProjectDataIndexSource",
    "ProjectDataIndexView",
    "ProjectDataIndexViewViewOf",
    "ProjectDataIndexWithStatus",
    "ProjectDataIndexWithStatusRecordPropertiesValue",
    "ProjectDataIndexWithStatusSchemaKey",
    "ProjectDataIndexWithStatusSource",
    "ProjectDataIndexWithStatusViewOf",
    "ProjectDocument",
    "ProjectDocumentUrl",
    "ProjectDocuments",
    "ProjectFlavourTotalKgs",
    "ProjectFlavoursQuota",
    "ProjectScratchFiles",
    "ProjectScratchFilesPaginated",
    "ProjectSourceDataIndex",
    "ProjectsFlavours",
    "Publication",
    "ReferenceToModel",
    "ResponseDocumentArtifacts",
    "ResponseGroupedDocuments",
    "ResponseUploadJobs",
    "S3Coordinates",
    "S3DocumentSource",
    "SemanticIngestReqParams",
    "SemanticIngestSourcePrivateDataCollection",
    "SemanticIngestSourcePrivateDataDocument",
    "SemanticIngestSourcePublicDataDocument",
    "SemanticIngestSourceUrl",
    "StatusFilter",
    "StorageSummaryTask",
    "StorageSummaryTaskKind",
    "SystemInfo",
    "TableFormerMode",
    "TableStructureOptions",
    "TargetConversionParameters",
    "TaskContext",
    "TaskResult",
    "TemporaryUploadFileResult",
    "TemporaryUrl",
    "TemporaryUrlFields",
    "TokenResponse",
    "UploadJob",
    "ValidationError",
    "ValidationErrorLocItem",
]
