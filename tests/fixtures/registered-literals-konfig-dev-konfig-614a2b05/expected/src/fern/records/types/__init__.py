



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_a_record_request_parent import CreateARecordRequestParent
    from .create_a_record_request_properties import CreateARecordRequestProperties
    from .create_a_record_request_properties_agreement_date import CreateARecordRequestPropertiesAgreementDate
    from .create_a_record_request_properties_counterparty_name import CreateARecordRequestPropertiesCounterpartyName
    from .create_a_smart_import_record_response import CreateASmartImportRecordResponse
    from .create_a_smart_import_record_to_import_response import CreateASmartImportRecordToImportResponse
    from .create_an_attachment_on_a_record_request_metadata import CreateAnAttachmentOnARecordRequestMetadata
    from .create_an_attachment_on_a_record_response import CreateAnAttachmentOnARecordResponse
    from .delete_a_record_response import DeleteARecordResponse
    from .list_all_records_metadata_response import ListAllRecordsMetadataResponse
    from .list_all_records_metadata_response_attachments import ListAllRecordsMetadataResponseAttachments
    from .list_all_records_metadata_response_attachments_signed_copy import (
        ListAllRecordsMetadataResponseAttachmentsSignedCopy,
    )
    from .list_all_records_metadata_response_links import ListAllRecordsMetadataResponseLinks
    from .list_all_records_metadata_response_properties import ListAllRecordsMetadataResponseProperties
    from .list_all_records_metadata_response_properties_additional_notes import (
        ListAllRecordsMetadataResponsePropertiesAdditionalNotes,
    )
    from .list_all_records_metadata_response_properties_agreement_date import (
        ListAllRecordsMetadataResponsePropertiesAgreementDate,
    )
    from .list_all_records_metadata_response_properties_workflow_id import (
        ListAllRecordsMetadataResponsePropertiesWorkflowId,
    )
    from .list_all_records_metadata_response_record_types import ListAllRecordsMetadataResponseRecordTypes
    from .list_all_records_metadata_response_record_types_contract import (
        ListAllRecordsMetadataResponseRecordTypesContract,
    )
    from .list_all_records_request_sort_direction import ListAllRecordsRequestSortDirection
    from .list_all_records_request_sort_field import ListAllRecordsRequestSortField
    from .list_all_records_response import ListAllRecordsResponse
    from .replace_a_record_request_parent import ReplaceARecordRequestParent
    from .replace_a_record_request_properties import ReplaceARecordRequestProperties
    from .replace_a_record_request_properties_agreement_date import ReplaceARecordRequestPropertiesAgreementDate
    from .replace_a_record_request_properties_counterparty_name import ReplaceARecordRequestPropertiesCounterpartyName
    from .retrieve_an_attachment_on_a_record_response import RetrieveAnAttachmentOnARecordResponse
    from .retrieve_import_predictions_response import RetrieveImportPredictionsResponse
    from .retrieve_import_predictions_response_one_item import RetrieveImportPredictionsResponseOneItem
    from .retrieve_import_predictions_response_one_item_status import RetrieveImportPredictionsResponseOneItemStatus
    from .retrieve_xlsx_export_file_of_all_records_response import RetrieveXlsxExportFileOfAllRecordsResponse
    from .update_record_metadata_request_add_properties import UpdateRecordMetadataRequestAddProperties
    from .update_record_metadata_request_add_properties_agreement_date import (
        UpdateRecordMetadataRequestAddPropertiesAgreementDate,
    )
    from .update_record_metadata_request_add_properties_counterparty_name import (
        UpdateRecordMetadataRequestAddPropertiesCounterpartyName,
    )
    from .update_record_metadata_request_set_parent import UpdateRecordMetadataRequestSetParent
_dynamic_imports: typing.Dict[str, str] = {
    "CreateARecordRequestParent": ".create_a_record_request_parent",
    "CreateARecordRequestProperties": ".create_a_record_request_properties",
    "CreateARecordRequestPropertiesAgreementDate": ".create_a_record_request_properties_agreement_date",
    "CreateARecordRequestPropertiesCounterpartyName": ".create_a_record_request_properties_counterparty_name",
    "CreateASmartImportRecordResponse": ".create_a_smart_import_record_response",
    "CreateASmartImportRecordToImportResponse": ".create_a_smart_import_record_to_import_response",
    "CreateAnAttachmentOnARecordRequestMetadata": ".create_an_attachment_on_a_record_request_metadata",
    "CreateAnAttachmentOnARecordResponse": ".create_an_attachment_on_a_record_response",
    "DeleteARecordResponse": ".delete_a_record_response",
    "ListAllRecordsMetadataResponse": ".list_all_records_metadata_response",
    "ListAllRecordsMetadataResponseAttachments": ".list_all_records_metadata_response_attachments",
    "ListAllRecordsMetadataResponseAttachmentsSignedCopy": ".list_all_records_metadata_response_attachments_signed_copy",
    "ListAllRecordsMetadataResponseLinks": ".list_all_records_metadata_response_links",
    "ListAllRecordsMetadataResponseProperties": ".list_all_records_metadata_response_properties",
    "ListAllRecordsMetadataResponsePropertiesAdditionalNotes": ".list_all_records_metadata_response_properties_additional_notes",
    "ListAllRecordsMetadataResponsePropertiesAgreementDate": ".list_all_records_metadata_response_properties_agreement_date",
    "ListAllRecordsMetadataResponsePropertiesWorkflowId": ".list_all_records_metadata_response_properties_workflow_id",
    "ListAllRecordsMetadataResponseRecordTypes": ".list_all_records_metadata_response_record_types",
    "ListAllRecordsMetadataResponseRecordTypesContract": ".list_all_records_metadata_response_record_types_contract",
    "ListAllRecordsRequestSortDirection": ".list_all_records_request_sort_direction",
    "ListAllRecordsRequestSortField": ".list_all_records_request_sort_field",
    "ListAllRecordsResponse": ".list_all_records_response",
    "ReplaceARecordRequestParent": ".replace_a_record_request_parent",
    "ReplaceARecordRequestProperties": ".replace_a_record_request_properties",
    "ReplaceARecordRequestPropertiesAgreementDate": ".replace_a_record_request_properties_agreement_date",
    "ReplaceARecordRequestPropertiesCounterpartyName": ".replace_a_record_request_properties_counterparty_name",
    "RetrieveAnAttachmentOnARecordResponse": ".retrieve_an_attachment_on_a_record_response",
    "RetrieveImportPredictionsResponse": ".retrieve_import_predictions_response",
    "RetrieveImportPredictionsResponseOneItem": ".retrieve_import_predictions_response_one_item",
    "RetrieveImportPredictionsResponseOneItemStatus": ".retrieve_import_predictions_response_one_item_status",
    "RetrieveXlsxExportFileOfAllRecordsResponse": ".retrieve_xlsx_export_file_of_all_records_response",
    "UpdateRecordMetadataRequestAddProperties": ".update_record_metadata_request_add_properties",
    "UpdateRecordMetadataRequestAddPropertiesAgreementDate": ".update_record_metadata_request_add_properties_agreement_date",
    "UpdateRecordMetadataRequestAddPropertiesCounterpartyName": ".update_record_metadata_request_add_properties_counterparty_name",
    "UpdateRecordMetadataRequestSetParent": ".update_record_metadata_request_set_parent",
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
