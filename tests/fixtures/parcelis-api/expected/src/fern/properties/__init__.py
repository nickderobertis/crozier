



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PropertiesArchiveResponse,
        PropertiesByIdResponse,
        PropertiesByIdResponseData,
        PropertiesByIdResponseDataUnitStatusesItem,
        PropertiesByIdResponseDataUnitStatusesItemOne,
        PropertiesByIdResponseDataUnitStatusesItemZero,
        PropertiesCompleteImageUploadResponse,
        PropertiesCreateImageUploadUrlRequestContentType,
        PropertiesCreateImageUploadUrlResponse,
        PropertiesCreateRequestAddress,
        PropertiesCreateRequestPropertyType,
        PropertiesCreateRequestUnitsItem,
        PropertiesCreateRequestUnitsItemUnitType,
        PropertiesCreateResponse,
        PropertiesDeleteImageResponse,
        PropertiesDeleteResponse,
        PropertiesInactivateResponse,
        PropertiesListResponse,
        PropertiesReactivateResponse,
        PropertiesUpdateNotesResponse,
        PropertiesUpdateRequestAddress,
        PropertiesUpdateRequestPropertyType,
        PropertiesUpdateRequestUnitsItem,
        PropertiesUpdateRequestUnitsItemUnitType,
        PropertiesUpdateResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PropertiesArchiveResponse": ".types",
    "PropertiesByIdResponse": ".types",
    "PropertiesByIdResponseData": ".types",
    "PropertiesByIdResponseDataUnitStatusesItem": ".types",
    "PropertiesByIdResponseDataUnitStatusesItemOne": ".types",
    "PropertiesByIdResponseDataUnitStatusesItemZero": ".types",
    "PropertiesCompleteImageUploadResponse": ".types",
    "PropertiesCreateImageUploadUrlRequestContentType": ".types",
    "PropertiesCreateImageUploadUrlResponse": ".types",
    "PropertiesCreateRequestAddress": ".types",
    "PropertiesCreateRequestPropertyType": ".types",
    "PropertiesCreateRequestUnitsItem": ".types",
    "PropertiesCreateRequestUnitsItemUnitType": ".types",
    "PropertiesCreateResponse": ".types",
    "PropertiesDeleteImageResponse": ".types",
    "PropertiesDeleteResponse": ".types",
    "PropertiesInactivateResponse": ".types",
    "PropertiesListResponse": ".types",
    "PropertiesReactivateResponse": ".types",
    "PropertiesUpdateNotesResponse": ".types",
    "PropertiesUpdateRequestAddress": ".types",
    "PropertiesUpdateRequestPropertyType": ".types",
    "PropertiesUpdateRequestUnitsItem": ".types",
    "PropertiesUpdateRequestUnitsItemUnitType": ".types",
    "PropertiesUpdateResponse": ".types",
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
