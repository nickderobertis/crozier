



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .records_create_attachment_request_metadata import RecordsCreateAttachmentRequestMetadata
    from .records_create_record_request_parent import RecordsCreateRecordRequestParent
    from .records_create_record_request_properties import RecordsCreateRecordRequestProperties
    from .records_create_record_request_properties_agreement_date import (
        RecordsCreateRecordRequestPropertiesAgreementDate,
    )
    from .records_create_record_request_properties_counterparty_name import (
        RecordsCreateRecordRequestPropertiesCounterpartyName,
    )
    from .records_list_all_request_sort_direction import RecordsListAllRequestSortDirection
    from .records_list_all_request_sort_field import RecordsListAllRequestSortField
    from .records_replace_metadata_request_parent import RecordsReplaceMetadataRequestParent
    from .records_replace_metadata_request_properties import RecordsReplaceMetadataRequestProperties
    from .records_replace_metadata_request_properties_agreement_date import (
        RecordsReplaceMetadataRequestPropertiesAgreementDate,
    )
    from .records_replace_metadata_request_properties_counterparty_name import (
        RecordsReplaceMetadataRequestPropertiesCounterpartyName,
    )
    from .records_update_metadata_request_add_properties import RecordsUpdateMetadataRequestAddProperties
    from .records_update_metadata_request_add_properties_agreement_date import (
        RecordsUpdateMetadataRequestAddPropertiesAgreementDate,
    )
    from .records_update_metadata_request_add_properties_counterparty_name import (
        RecordsUpdateMetadataRequestAddPropertiesCounterpartyName,
    )
    from .records_update_metadata_request_set_parent import RecordsUpdateMetadataRequestSetParent
_dynamic_imports: typing.Dict[str, str] = {
    "RecordsCreateAttachmentRequestMetadata": ".records_create_attachment_request_metadata",
    "RecordsCreateRecordRequestParent": ".records_create_record_request_parent",
    "RecordsCreateRecordRequestProperties": ".records_create_record_request_properties",
    "RecordsCreateRecordRequestPropertiesAgreementDate": ".records_create_record_request_properties_agreement_date",
    "RecordsCreateRecordRequestPropertiesCounterpartyName": ".records_create_record_request_properties_counterparty_name",
    "RecordsListAllRequestSortDirection": ".records_list_all_request_sort_direction",
    "RecordsListAllRequestSortField": ".records_list_all_request_sort_field",
    "RecordsReplaceMetadataRequestParent": ".records_replace_metadata_request_parent",
    "RecordsReplaceMetadataRequestProperties": ".records_replace_metadata_request_properties",
    "RecordsReplaceMetadataRequestPropertiesAgreementDate": ".records_replace_metadata_request_properties_agreement_date",
    "RecordsReplaceMetadataRequestPropertiesCounterpartyName": ".records_replace_metadata_request_properties_counterparty_name",
    "RecordsUpdateMetadataRequestAddProperties": ".records_update_metadata_request_add_properties",
    "RecordsUpdateMetadataRequestAddPropertiesAgreementDate": ".records_update_metadata_request_add_properties_agreement_date",
    "RecordsUpdateMetadataRequestAddPropertiesCounterpartyName": ".records_update_metadata_request_add_properties_counterparty_name",
    "RecordsUpdateMetadataRequestSetParent": ".records_update_metadata_request_set_parent",
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
    "RecordsCreateAttachmentRequestMetadata",
    "RecordsCreateRecordRequestParent",
    "RecordsCreateRecordRequestProperties",
    "RecordsCreateRecordRequestPropertiesAgreementDate",
    "RecordsCreateRecordRequestPropertiesCounterpartyName",
    "RecordsListAllRequestSortDirection",
    "RecordsListAllRequestSortField",
    "RecordsReplaceMetadataRequestParent",
    "RecordsReplaceMetadataRequestProperties",
    "RecordsReplaceMetadataRequestPropertiesAgreementDate",
    "RecordsReplaceMetadataRequestPropertiesCounterpartyName",
    "RecordsUpdateMetadataRequestAddProperties",
    "RecordsUpdateMetadataRequestAddPropertiesAgreementDate",
    "RecordsUpdateMetadataRequestAddPropertiesCounterpartyName",
    "RecordsUpdateMetadataRequestSetParent",
]
