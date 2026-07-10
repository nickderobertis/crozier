



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BadObjectRequestInfo,
        EndpointsError,
        EndpointsErrorCategory,
        EndpointsErrorCode,
        EndpointsPaginatedResponse,
        EndpointsPutResponse,
        TypesAnimal,
        TypesAnimalOne,
        TypesAnimalOneAnimal,
        TypesAnimalZero,
        TypesAnimalZeroAnimal,
        TypesCat,
        TypesDocumentedUnknownType,
        TypesDog,
        TypesDoubleOptional,
        TypesMapOfDocumentedUnknownType,
        TypesMixedType,
        TypesNestedObjectWithOptionalField,
        TypesNestedObjectWithRequiredField,
        TypesObjectWithDatetimeLikeString,
        TypesObjectWithDocs,
        TypesObjectWithDocumentedUnknownType,
        TypesObjectWithMapOfMap,
        TypesObjectWithOptionalField,
        TypesObjectWithRequiredField,
        TypesObjectWithUnknownField,
        TypesOptionalAlias,
        TypesWeatherReport,
    )
    from .errors import BadRequestError
    from . import (
        endpoints_container,
        endpoints_content_type,
        endpoints_enum,
        endpoints_http_methods,
        endpoints_object,
        endpoints_pagination,
        endpoints_params,
        endpoints_primitive,
        endpoints_put,
        endpoints_union,
        endpoints_urls,
        inlinedrequests,
        noauth,
        noreqbody,
        reqwithheaders,
    )
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadObjectRequestInfo": ".types",
    "BadRequestError": ".errors",
    "EndpointsError": ".types",
    "EndpointsErrorCategory": ".types",
    "EndpointsErrorCode": ".types",
    "EndpointsPaginatedResponse": ".types",
    "EndpointsPutResponse": ".types",
    "FernApi": ".client",
    "TypesAnimal": ".types",
    "TypesAnimalOne": ".types",
    "TypesAnimalOneAnimal": ".types",
    "TypesAnimalZero": ".types",
    "TypesAnimalZeroAnimal": ".types",
    "TypesCat": ".types",
    "TypesDocumentedUnknownType": ".types",
    "TypesDog": ".types",
    "TypesDoubleOptional": ".types",
    "TypesMapOfDocumentedUnknownType": ".types",
    "TypesMixedType": ".types",
    "TypesNestedObjectWithOptionalField": ".types",
    "TypesNestedObjectWithRequiredField": ".types",
    "TypesObjectWithDatetimeLikeString": ".types",
    "TypesObjectWithDocs": ".types",
    "TypesObjectWithDocumentedUnknownType": ".types",
    "TypesObjectWithMapOfMap": ".types",
    "TypesObjectWithOptionalField": ".types",
    "TypesObjectWithRequiredField": ".types",
    "TypesObjectWithUnknownField": ".types",
    "TypesOptionalAlias": ".types",
    "TypesWeatherReport": ".types",
    "__version__": ".version",
    "endpoints_container": ".endpoints_container",
    "endpoints_content_type": ".endpoints_content_type",
    "endpoints_enum": ".endpoints_enum",
    "endpoints_http_methods": ".endpoints_http_methods",
    "endpoints_object": ".endpoints_object",
    "endpoints_pagination": ".endpoints_pagination",
    "endpoints_params": ".endpoints_params",
    "endpoints_primitive": ".endpoints_primitive",
    "endpoints_put": ".endpoints_put",
    "endpoints_union": ".endpoints_union",
    "endpoints_urls": ".endpoints_urls",
    "inlinedrequests": ".inlinedrequests",
    "noauth": ".noauth",
    "noreqbody": ".noreqbody",
    "reqwithheaders": ".reqwithheaders",
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
    "AsyncFernApi",
    "BadObjectRequestInfo",
    "BadRequestError",
    "EndpointsError",
    "EndpointsErrorCategory",
    "EndpointsErrorCode",
    "EndpointsPaginatedResponse",
    "EndpointsPutResponse",
    "FernApi",
    "TypesAnimal",
    "TypesAnimalOne",
    "TypesAnimalOneAnimal",
    "TypesAnimalZero",
    "TypesAnimalZeroAnimal",
    "TypesCat",
    "TypesDocumentedUnknownType",
    "TypesDog",
    "TypesDoubleOptional",
    "TypesMapOfDocumentedUnknownType",
    "TypesMixedType",
    "TypesNestedObjectWithOptionalField",
    "TypesNestedObjectWithRequiredField",
    "TypesObjectWithDatetimeLikeString",
    "TypesObjectWithDocs",
    "TypesObjectWithDocumentedUnknownType",
    "TypesObjectWithMapOfMap",
    "TypesObjectWithOptionalField",
    "TypesObjectWithRequiredField",
    "TypesObjectWithUnknownField",
    "TypesOptionalAlias",
    "TypesWeatherReport",
    "__version__",
    "endpoints_container",
    "endpoints_content_type",
    "endpoints_enum",
    "endpoints_http_methods",
    "endpoints_object",
    "endpoints_pagination",
    "endpoints_params",
    "endpoints_primitive",
    "endpoints_put",
    "endpoints_union",
    "endpoints_urls",
    "inlinedrequests",
    "noauth",
    "noreqbody",
    "reqwithheaders",
]
