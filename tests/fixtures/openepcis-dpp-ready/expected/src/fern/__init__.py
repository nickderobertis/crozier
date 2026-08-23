



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CreateDppResult,
        DataElement,
        DataElementBase,
        DataElementCollection,
        DataElement_DataElementCollection,
        DataElement_MultiLanguageDataElement,
        DataElement_MultiValuedDataElement,
        DataElement_RelatedResource,
        DataElement_SingleValuedDataElement,
        DigitalProductPassport,
        DigitalProductPassportCompressed,
        DigitalProductPassportFull,
        DppEnvelope,
        DppIdPage,
        DppStatus,
        Granularity,
        Identifier,
        Message,
        MessageTypeEnum,
        MultiLanguageDataElement,
        MultiLanguageValue,
        MultiValuedDataElement,
        MultiValuedDataElementValueItem,
        MultiValuedDataElementValueItemZero,
        RegisterResult,
        RelatedResource,
        Result,
        SingleValuedDataElement,
        SingleValuedDataElementValue,
        StatusCode,
        Timestamp,
    )
    from .errors import (
        BadGatewayError,
        BadRequestError,
        ConflictError,
        ForbiddenError,
        InternalServerError,
        NotFoundError,
        NotImplementedError,
        UnauthorizedError,
    )
    from . import fine_granular_api, life_cycle_api, registry_api
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .fine_granular_api import ReadDataElementRequestRepresentation, UpdateDataElementRequestRepresentation
    from .life_cycle_api import (
        CreateDppRequestRepresentation,
        ReadDppByIdRequestRepresentation,
        ReadDppByProductIdRequestRepresentation,
        ReadDppVersionByIdAndDateRequestRepresentation,
        UpdateDppByIdRequestRepresentation,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadGatewayError": ".errors",
    "BadRequestError": ".errors",
    "ConflictError": ".errors",
    "CreateDppRequestRepresentation": ".life_cycle_api",
    "CreateDppResult": ".types",
    "DataElement": ".types",
    "DataElementBase": ".types",
    "DataElementCollection": ".types",
    "DataElement_DataElementCollection": ".types",
    "DataElement_MultiLanguageDataElement": ".types",
    "DataElement_MultiValuedDataElement": ".types",
    "DataElement_RelatedResource": ".types",
    "DataElement_SingleValuedDataElement": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DigitalProductPassport": ".types",
    "DigitalProductPassportCompressed": ".types",
    "DigitalProductPassportFull": ".types",
    "DppEnvelope": ".types",
    "DppIdPage": ".types",
    "DppStatus": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "Granularity": ".types",
    "Identifier": ".types",
    "InternalServerError": ".errors",
    "Message": ".types",
    "MessageTypeEnum": ".types",
    "MultiLanguageDataElement": ".types",
    "MultiLanguageValue": ".types",
    "MultiValuedDataElement": ".types",
    "MultiValuedDataElementValueItem": ".types",
    "MultiValuedDataElementValueItemZero": ".types",
    "NotFoundError": ".errors",
    "NotImplementedError": ".errors",
    "ReadDataElementRequestRepresentation": ".fine_granular_api",
    "ReadDppByIdRequestRepresentation": ".life_cycle_api",
    "ReadDppByProductIdRequestRepresentation": ".life_cycle_api",
    "ReadDppVersionByIdAndDateRequestRepresentation": ".life_cycle_api",
    "RegisterResult": ".types",
    "RelatedResource": ".types",
    "Result": ".types",
    "SingleValuedDataElement": ".types",
    "SingleValuedDataElementValue": ".types",
    "StatusCode": ".types",
    "Timestamp": ".types",
    "UnauthorizedError": ".errors",
    "UpdateDataElementRequestRepresentation": ".fine_granular_api",
    "UpdateDppByIdRequestRepresentation": ".life_cycle_api",
    "__version__": ".version",
    "fine_granular_api": ".fine_granular_api",
    "life_cycle_api": ".life_cycle_api",
    "registry_api": ".registry_api",
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
    "BadGatewayError",
    "BadRequestError",
    "ConflictError",
    "CreateDppRequestRepresentation",
    "CreateDppResult",
    "DataElement",
    "DataElementBase",
    "DataElementCollection",
    "DataElement_DataElementCollection",
    "DataElement_MultiLanguageDataElement",
    "DataElement_MultiValuedDataElement",
    "DataElement_RelatedResource",
    "DataElement_SingleValuedDataElement",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DigitalProductPassport",
    "DigitalProductPassportCompressed",
    "DigitalProductPassportFull",
    "DppEnvelope",
    "DppIdPage",
    "DppStatus",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "Granularity",
    "Identifier",
    "InternalServerError",
    "Message",
    "MessageTypeEnum",
    "MultiLanguageDataElement",
    "MultiLanguageValue",
    "MultiValuedDataElement",
    "MultiValuedDataElementValueItem",
    "MultiValuedDataElementValueItemZero",
    "NotFoundError",
    "NotImplementedError",
    "ReadDataElementRequestRepresentation",
    "ReadDppByIdRequestRepresentation",
    "ReadDppByProductIdRequestRepresentation",
    "ReadDppVersionByIdAndDateRequestRepresentation",
    "RegisterResult",
    "RelatedResource",
    "Result",
    "SingleValuedDataElement",
    "SingleValuedDataElementValue",
    "StatusCode",
    "Timestamp",
    "UnauthorizedError",
    "UpdateDataElementRequestRepresentation",
    "UpdateDppByIdRequestRepresentation",
    "__version__",
    "fine_granular_api",
    "life_cycle_api",
    "registry_api",
]
