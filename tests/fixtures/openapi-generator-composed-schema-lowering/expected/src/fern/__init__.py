



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AllNullTest,
        AnyOfOverlapping,
        AnyOfPropertyHolder,
        AnyOfStringInteger,
        Cat,
        CatPetType,
        CreateResponse,
        CreateResponseBase,
        DataObject,
        DedupTest,
        DedupTestOne,
        Dog,
        DogPetType,
        InputItem,
        InputParam,
        ModelIds,
        ModelIdsCompaction,
        ModelIdsResponses,
        ModelIdsResponsesOne,
        ModelIdsShared,
        ModelIdsSharedOne,
        NullableDataObject,
        NullableTemperature,
        OasConstObject,
        OasConstObjectType,
        OneOfWithStringOverlap,
        OpenStringModel,
        OptionalScore,
        OverlappingObjectA,
        OverlappingObjectB,
        ParentWithAnyOfOverlapping,
        PetByType,
        RefHolder,
        ResponseCompletedEvent,
        ResponseCreatedEvent,
        ResponseStreamEvent,
        ResponseStreamEvent_ResponseCompleted,
        ResponseStreamEvent_ResponseCreated,
        SingleBranchTest,
        StainlessObject,
        StainlessObjectType,
        StringEnumModel,
        StringOverlapHolder,
        TemperatureContainer,
        TimestampContainer,
        VariantPayload,
    )
    from . import composed_schema
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .composed_schema import GetInlineAnyOfResponseResponse, GetInlineOneOfEventsResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AllNullTest": ".types",
    "AnyOfOverlapping": ".types",
    "AnyOfPropertyHolder": ".types",
    "AnyOfStringInteger": ".types",
    "AsyncFernApi": ".client",
    "Cat": ".types",
    "CatPetType": ".types",
    "CreateResponse": ".types",
    "CreateResponseBase": ".types",
    "DataObject": ".types",
    "DedupTest": ".types",
    "DedupTestOne": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Dog": ".types",
    "DogPetType": ".types",
    "FernApi": ".client",
    "GetInlineAnyOfResponseResponse": ".composed_schema",
    "GetInlineOneOfEventsResponse": ".composed_schema",
    "InputItem": ".types",
    "InputParam": ".types",
    "ModelIds": ".types",
    "ModelIdsCompaction": ".types",
    "ModelIdsResponses": ".types",
    "ModelIdsResponsesOne": ".types",
    "ModelIdsShared": ".types",
    "ModelIdsSharedOne": ".types",
    "NullableDataObject": ".types",
    "NullableTemperature": ".types",
    "OasConstObject": ".types",
    "OasConstObjectType": ".types",
    "OneOfWithStringOverlap": ".types",
    "OpenStringModel": ".types",
    "OptionalScore": ".types",
    "OverlappingObjectA": ".types",
    "OverlappingObjectB": ".types",
    "ParentWithAnyOfOverlapping": ".types",
    "PetByType": ".types",
    "RefHolder": ".types",
    "ResponseCompletedEvent": ".types",
    "ResponseCreatedEvent": ".types",
    "ResponseStreamEvent": ".types",
    "ResponseStreamEvent_ResponseCompleted": ".types",
    "ResponseStreamEvent_ResponseCreated": ".types",
    "SingleBranchTest": ".types",
    "StainlessObject": ".types",
    "StainlessObjectType": ".types",
    "StringEnumModel": ".types",
    "StringOverlapHolder": ".types",
    "TemperatureContainer": ".types",
    "TimestampContainer": ".types",
    "VariantPayload": ".types",
    "__version__": ".version",
    "composed_schema": ".composed_schema",
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
    "AllNullTest",
    "AnyOfOverlapping",
    "AnyOfPropertyHolder",
    "AnyOfStringInteger",
    "AsyncFernApi",
    "Cat",
    "CatPetType",
    "CreateResponse",
    "CreateResponseBase",
    "DataObject",
    "DedupTest",
    "DedupTestOne",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Dog",
    "DogPetType",
    "FernApi",
    "GetInlineAnyOfResponseResponse",
    "GetInlineOneOfEventsResponse",
    "InputItem",
    "InputParam",
    "ModelIds",
    "ModelIdsCompaction",
    "ModelIdsResponses",
    "ModelIdsResponsesOne",
    "ModelIdsShared",
    "ModelIdsSharedOne",
    "NullableDataObject",
    "NullableTemperature",
    "OasConstObject",
    "OasConstObjectType",
    "OneOfWithStringOverlap",
    "OpenStringModel",
    "OptionalScore",
    "OverlappingObjectA",
    "OverlappingObjectB",
    "ParentWithAnyOfOverlapping",
    "PetByType",
    "RefHolder",
    "ResponseCompletedEvent",
    "ResponseCreatedEvent",
    "ResponseStreamEvent",
    "ResponseStreamEvent_ResponseCompleted",
    "ResponseStreamEvent_ResponseCreated",
    "SingleBranchTest",
    "StainlessObject",
    "StainlessObjectType",
    "StringEnumModel",
    "StringOverlapHolder",
    "TemperatureContainer",
    "TimestampContainer",
    "VariantPayload",
    "__version__",
    "composed_schema",
]
