



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ErrorBadRequest,
        ErrorBadRequestIssuesItem,
        ErrorForbidden,
        ErrorForbiddenIssuesItem,
        ErrorInternalServerError,
        ErrorInternalServerErrorIssuesItem,
        ErrorNotFound,
        ErrorNotFoundIssuesItem,
        ErrorUnauthorized,
        ErrorUnauthorizedIssuesItem,
    )
    from .errors import BadRequestError, ForbiddenError, InternalServerError, NotFoundError, UnauthorizedError
    from . import amenities, properties, system, tags, tenants, unit_options, units
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .amenities import AmenitiesListResponse, AmenitiesUpdateResponse
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .properties import (
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
    from .system import HealthResponse
    from .tags import TagsCreateResponse, TagsListResponse
    from .tenants import (
        TenantsCompleteImageUploadResponse,
        TenantsCreateImageUploadUrlRequestContentType,
        TenantsCreateImageUploadUrlResponse,
        TenantsDeleteImageResponse,
    )
    from .unit_options import UnitOptionsListResponse
    from .units import (
        UnitsByIdResponse,
        UnitsCreateRequestUnitType,
        UnitsCreateResponse,
        UnitsDeleteResponse,
        UnitsListResponse,
        UnitsUpdateRequestUnitType,
        UnitsUpdateResponse,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AmenitiesListResponse": ".amenities",
    "AmenitiesUpdateResponse": ".amenities",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "ErrorBadRequest": ".types",
    "ErrorBadRequestIssuesItem": ".types",
    "ErrorForbidden": ".types",
    "ErrorForbiddenIssuesItem": ".types",
    "ErrorInternalServerError": ".types",
    "ErrorInternalServerErrorIssuesItem": ".types",
    "ErrorNotFound": ".types",
    "ErrorNotFoundIssuesItem": ".types",
    "ErrorUnauthorized": ".types",
    "ErrorUnauthorizedIssuesItem": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "HealthResponse": ".system",
    "InternalServerError": ".errors",
    "NotFoundError": ".errors",
    "PropertiesArchiveResponse": ".properties",
    "PropertiesByIdResponse": ".properties",
    "PropertiesByIdResponseData": ".properties",
    "PropertiesByIdResponseDataUnitStatusesItem": ".properties",
    "PropertiesByIdResponseDataUnitStatusesItemOne": ".properties",
    "PropertiesByIdResponseDataUnitStatusesItemZero": ".properties",
    "PropertiesCompleteImageUploadResponse": ".properties",
    "PropertiesCreateImageUploadUrlRequestContentType": ".properties",
    "PropertiesCreateImageUploadUrlResponse": ".properties",
    "PropertiesCreateRequestAddress": ".properties",
    "PropertiesCreateRequestPropertyType": ".properties",
    "PropertiesCreateRequestUnitsItem": ".properties",
    "PropertiesCreateRequestUnitsItemUnitType": ".properties",
    "PropertiesCreateResponse": ".properties",
    "PropertiesDeleteImageResponse": ".properties",
    "PropertiesDeleteResponse": ".properties",
    "PropertiesInactivateResponse": ".properties",
    "PropertiesListResponse": ".properties",
    "PropertiesReactivateResponse": ".properties",
    "PropertiesUpdateNotesResponse": ".properties",
    "PropertiesUpdateRequestAddress": ".properties",
    "PropertiesUpdateRequestPropertyType": ".properties",
    "PropertiesUpdateRequestUnitsItem": ".properties",
    "PropertiesUpdateRequestUnitsItemUnitType": ".properties",
    "PropertiesUpdateResponse": ".properties",
    "TagsCreateResponse": ".tags",
    "TagsListResponse": ".tags",
    "TenantsCompleteImageUploadResponse": ".tenants",
    "TenantsCreateImageUploadUrlRequestContentType": ".tenants",
    "TenantsCreateImageUploadUrlResponse": ".tenants",
    "TenantsDeleteImageResponse": ".tenants",
    "UnauthorizedError": ".errors",
    "UnitOptionsListResponse": ".unit_options",
    "UnitsByIdResponse": ".units",
    "UnitsCreateRequestUnitType": ".units",
    "UnitsCreateResponse": ".units",
    "UnitsDeleteResponse": ".units",
    "UnitsListResponse": ".units",
    "UnitsUpdateRequestUnitType": ".units",
    "UnitsUpdateResponse": ".units",
    "__version__": ".version",
    "amenities": ".amenities",
    "properties": ".properties",
    "system": ".system",
    "tags": ".tags",
    "tenants": ".tenants",
    "unit_options": ".unit_options",
    "units": ".units",
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
    "AmenitiesListResponse",
    "AmenitiesUpdateResponse",
    "AsyncFernApi",
    "BadRequestError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "ErrorBadRequest",
    "ErrorBadRequestIssuesItem",
    "ErrorForbidden",
    "ErrorForbiddenIssuesItem",
    "ErrorInternalServerError",
    "ErrorInternalServerErrorIssuesItem",
    "ErrorNotFound",
    "ErrorNotFoundIssuesItem",
    "ErrorUnauthorized",
    "ErrorUnauthorizedIssuesItem",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "HealthResponse",
    "InternalServerError",
    "NotFoundError",
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
    "TagsCreateResponse",
    "TagsListResponse",
    "TenantsCompleteImageUploadResponse",
    "TenantsCreateImageUploadUrlRequestContentType",
    "TenantsCreateImageUploadUrlResponse",
    "TenantsDeleteImageResponse",
    "UnauthorizedError",
    "UnitOptionsListResponse",
    "UnitsByIdResponse",
    "UnitsCreateRequestUnitType",
    "UnitsCreateResponse",
    "UnitsDeleteResponse",
    "UnitsListResponse",
    "UnitsUpdateRequestUnitType",
    "UnitsUpdateResponse",
    "__version__",
    "amenities",
    "properties",
    "system",
    "tags",
    "tenants",
    "unit_options",
    "units",
]
