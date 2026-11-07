



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CreateARecordRequestParent,
        CreateARecordRequestProperties,
        CreateARecordRequestPropertiesAgreementDate,
        CreateARecordRequestPropertiesCounterpartyName,
        CreateASmartImportRecordResponse,
        CreateASmartImportRecordToImportResponse,
        CreateAnAttachmentOnARecordRequestMetadata,
        CreateAnAttachmentOnARecordResponse,
        DeleteARecordResponse,
        ListAllRecordsMetadataResponse,
        ListAllRecordsMetadataResponseAttachments,
        ListAllRecordsMetadataResponseAttachmentsSignedCopy,
        ListAllRecordsMetadataResponseLinks,
        ListAllRecordsMetadataResponseProperties,
        ListAllRecordsMetadataResponsePropertiesAdditionalNotes,
        ListAllRecordsMetadataResponsePropertiesAgreementDate,
        ListAllRecordsMetadataResponsePropertiesWorkflowId,
        ListAllRecordsMetadataResponseRecordTypes,
        ListAllRecordsMetadataResponseRecordTypesContract,
        ListAllRecordsRequestSortDirection,
        ListAllRecordsRequestSortField,
        ListAllRecordsResponse,
        ReplaceARecordRequestParent,
        ReplaceARecordRequestProperties,
        ReplaceARecordRequestPropertiesAgreementDate,
        ReplaceARecordRequestPropertiesCounterpartyName,
        RetrieveAnAttachmentOnARecordResponse,
        RetrieveImportPredictionsResponse,
        RetrieveImportPredictionsResponseOneItem,
        RetrieveImportPredictionsResponseOneItemStatus,
        RetrieveXlsxExportFileOfAllRecordsResponse,
        UpdateRecordMetadataRequestAddProperties,
        UpdateRecordMetadataRequestAddPropertiesAgreementDate,
        UpdateRecordMetadataRequestAddPropertiesCounterpartyName,
        UpdateRecordMetadataRequestSetParent,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateARecordRequestParent": ".types",
    "CreateARecordRequestProperties": ".types",
    "CreateARecordRequestPropertiesAgreementDate": ".types",
    "CreateARecordRequestPropertiesCounterpartyName": ".types",
    "CreateASmartImportRecordResponse": ".types",
    "CreateASmartImportRecordToImportResponse": ".types",
    "CreateAnAttachmentOnARecordRequestMetadata": ".types",
    "CreateAnAttachmentOnARecordResponse": ".types",
    "DeleteARecordResponse": ".types",
    "ListAllRecordsMetadataResponse": ".types",
    "ListAllRecordsMetadataResponseAttachments": ".types",
    "ListAllRecordsMetadataResponseAttachmentsSignedCopy": ".types",
    "ListAllRecordsMetadataResponseLinks": ".types",
    "ListAllRecordsMetadataResponseProperties": ".types",
    "ListAllRecordsMetadataResponsePropertiesAdditionalNotes": ".types",
    "ListAllRecordsMetadataResponsePropertiesAgreementDate": ".types",
    "ListAllRecordsMetadataResponsePropertiesWorkflowId": ".types",
    "ListAllRecordsMetadataResponseRecordTypes": ".types",
    "ListAllRecordsMetadataResponseRecordTypesContract": ".types",
    "ListAllRecordsRequestSortDirection": ".types",
    "ListAllRecordsRequestSortField": ".types",
    "ListAllRecordsResponse": ".types",
    "ReplaceARecordRequestParent": ".types",
    "ReplaceARecordRequestProperties": ".types",
    "ReplaceARecordRequestPropertiesAgreementDate": ".types",
    "ReplaceARecordRequestPropertiesCounterpartyName": ".types",
    "RetrieveAnAttachmentOnARecordResponse": ".types",
    "RetrieveImportPredictionsResponse": ".types",
    "RetrieveImportPredictionsResponseOneItem": ".types",
    "RetrieveImportPredictionsResponseOneItemStatus": ".types",
    "RetrieveXlsxExportFileOfAllRecordsResponse": ".types",
    "UpdateRecordMetadataRequestAddProperties": ".types",
    "UpdateRecordMetadataRequestAddPropertiesAgreementDate": ".types",
    "UpdateRecordMetadataRequestAddPropertiesCounterpartyName": ".types",
    "UpdateRecordMetadataRequestSetParent": ".types",
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
    "CreateARecordRequestParent",
    "CreateARecordRequestProperties",
    "CreateARecordRequestPropertiesAgreementDate",
    "CreateARecordRequestPropertiesCounterpartyName",
    "CreateASmartImportRecordResponse",
    "CreateASmartImportRecordToImportResponse",
    "CreateAnAttachmentOnARecordRequestMetadata",
    "CreateAnAttachmentOnARecordResponse",
    "DeleteARecordResponse",
    "ListAllRecordsMetadataResponse",
    "ListAllRecordsMetadataResponseAttachments",
    "ListAllRecordsMetadataResponseAttachmentsSignedCopy",
    "ListAllRecordsMetadataResponseLinks",
    "ListAllRecordsMetadataResponseProperties",
    "ListAllRecordsMetadataResponsePropertiesAdditionalNotes",
    "ListAllRecordsMetadataResponsePropertiesAgreementDate",
    "ListAllRecordsMetadataResponsePropertiesWorkflowId",
    "ListAllRecordsMetadataResponseRecordTypes",
    "ListAllRecordsMetadataResponseRecordTypesContract",
    "ListAllRecordsRequestSortDirection",
    "ListAllRecordsRequestSortField",
    "ListAllRecordsResponse",
    "ReplaceARecordRequestParent",
    "ReplaceARecordRequestProperties",
    "ReplaceARecordRequestPropertiesAgreementDate",
    "ReplaceARecordRequestPropertiesCounterpartyName",
    "RetrieveAnAttachmentOnARecordResponse",
    "RetrieveImportPredictionsResponse",
    "RetrieveImportPredictionsResponseOneItem",
    "RetrieveImportPredictionsResponseOneItemStatus",
    "RetrieveXlsxExportFileOfAllRecordsResponse",
    "UpdateRecordMetadataRequestAddProperties",
    "UpdateRecordMetadataRequestAddPropertiesAgreementDate",
    "UpdateRecordMetadataRequestAddPropertiesCounterpartyName",
    "UpdateRecordMetadataRequestSetParent",
]
