



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .properties_archive_response import PropertiesArchiveResponse
    from .properties_by_id_response import PropertiesByIdResponse
    from .properties_by_id_response_data import PropertiesByIdResponseData
    from .properties_by_id_response_data_unit_statuses_item import PropertiesByIdResponseDataUnitStatusesItem
    from .properties_by_id_response_data_unit_statuses_item_one import PropertiesByIdResponseDataUnitStatusesItemOne
    from .properties_by_id_response_data_unit_statuses_item_zero import PropertiesByIdResponseDataUnitStatusesItemZero
    from .properties_complete_image_upload_response import PropertiesCompleteImageUploadResponse
    from .properties_create_image_upload_url_request_content_type import (
        PropertiesCreateImageUploadUrlRequestContentType,
    )
    from .properties_create_image_upload_url_response import PropertiesCreateImageUploadUrlResponse
    from .properties_create_request_address import PropertiesCreateRequestAddress
    from .properties_create_request_property_type import PropertiesCreateRequestPropertyType
    from .properties_create_request_units_item import PropertiesCreateRequestUnitsItem
    from .properties_create_request_units_item_unit_type import PropertiesCreateRequestUnitsItemUnitType
    from .properties_create_response import PropertiesCreateResponse
    from .properties_delete_image_response import PropertiesDeleteImageResponse
    from .properties_delete_response import PropertiesDeleteResponse
    from .properties_inactivate_response import PropertiesInactivateResponse
    from .properties_list_response import PropertiesListResponse
    from .properties_reactivate_response import PropertiesReactivateResponse
    from .properties_update_notes_response import PropertiesUpdateNotesResponse
    from .properties_update_request_address import PropertiesUpdateRequestAddress
    from .properties_update_request_property_type import PropertiesUpdateRequestPropertyType
    from .properties_update_request_units_item import PropertiesUpdateRequestUnitsItem
    from .properties_update_request_units_item_unit_type import PropertiesUpdateRequestUnitsItemUnitType
    from .properties_update_response import PropertiesUpdateResponse
_dynamic_imports: typing.Dict[str, str] = {
    "PropertiesArchiveResponse": ".properties_archive_response",
    "PropertiesByIdResponse": ".properties_by_id_response",
    "PropertiesByIdResponseData": ".properties_by_id_response_data",
    "PropertiesByIdResponseDataUnitStatusesItem": ".properties_by_id_response_data_unit_statuses_item",
    "PropertiesByIdResponseDataUnitStatusesItemOne": ".properties_by_id_response_data_unit_statuses_item_one",
    "PropertiesByIdResponseDataUnitStatusesItemZero": ".properties_by_id_response_data_unit_statuses_item_zero",
    "PropertiesCompleteImageUploadResponse": ".properties_complete_image_upload_response",
    "PropertiesCreateImageUploadUrlRequestContentType": ".properties_create_image_upload_url_request_content_type",
    "PropertiesCreateImageUploadUrlResponse": ".properties_create_image_upload_url_response",
    "PropertiesCreateRequestAddress": ".properties_create_request_address",
    "PropertiesCreateRequestPropertyType": ".properties_create_request_property_type",
    "PropertiesCreateRequestUnitsItem": ".properties_create_request_units_item",
    "PropertiesCreateRequestUnitsItemUnitType": ".properties_create_request_units_item_unit_type",
    "PropertiesCreateResponse": ".properties_create_response",
    "PropertiesDeleteImageResponse": ".properties_delete_image_response",
    "PropertiesDeleteResponse": ".properties_delete_response",
    "PropertiesInactivateResponse": ".properties_inactivate_response",
    "PropertiesListResponse": ".properties_list_response",
    "PropertiesReactivateResponse": ".properties_reactivate_response",
    "PropertiesUpdateNotesResponse": ".properties_update_notes_response",
    "PropertiesUpdateRequestAddress": ".properties_update_request_address",
    "PropertiesUpdateRequestPropertyType": ".properties_update_request_property_type",
    "PropertiesUpdateRequestUnitsItem": ".properties_update_request_units_item",
    "PropertiesUpdateRequestUnitsItemUnitType": ".properties_update_request_units_item_unit_type",
    "PropertiesUpdateResponse": ".properties_update_response",
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
    "PropertiesArchiveResponse",
    "PropertiesByIdResponse",
    "PropertiesByIdResponseData",
    "PropertiesByIdResponseDataUnitStatusesItem",
    "PropertiesByIdResponseDataUnitStatusesItemOne",
    "PropertiesByIdResponseDataUnitStatusesItemZero",
    "PropertiesCompleteImageUploadResponse",
    "PropertiesCreateImageUploadUrlRequestContentType",
    "PropertiesCreateImageUploadUrlResponse",
    "PropertiesCreateRequestAddress",
    "PropertiesCreateRequestPropertyType",
    "PropertiesCreateRequestUnitsItem",
    "PropertiesCreateRequestUnitsItemUnitType",
    "PropertiesCreateResponse",
    "PropertiesDeleteImageResponse",
    "PropertiesDeleteResponse",
    "PropertiesInactivateResponse",
    "PropertiesListResponse",
    "PropertiesReactivateResponse",
    "PropertiesUpdateNotesResponse",
    "PropertiesUpdateRequestAddress",
    "PropertiesUpdateRequestPropertyType",
    "PropertiesUpdateRequestUnitsItem",
    "PropertiesUpdateRequestUnitsItemUnitType",
    "PropertiesUpdateResponse",
]
