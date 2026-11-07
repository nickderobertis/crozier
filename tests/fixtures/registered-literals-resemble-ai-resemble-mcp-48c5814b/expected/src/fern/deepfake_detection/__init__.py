



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CreateDetectionRequestModelTypes,
        CreateDetectionResponse,
        CreateDetectionResponseItem,
        CreateDetectionResponseItemIntelligence,
        CreateDetectionResponseItemIntelligenceDescription,
        GetDetectionResponse,
        GetDetectionResponseItem,
        GetDetectionResponseItemAudioSourceTracing,
        GetDetectionResponseItemIntelligence,
        GetDetectionResponseItemIntelligenceDescription,
        GetDetectionResponseItemMediaType,
        GetDetectionResponseItemStatus,
        ListDetectionsResponse,
        ListDetectionsResponseItemsItem,
        ListDetectionsResponseItemsItemAudioSourceTracing,
        ListDetectionsResponseItemsItemMediaType,
        ListDetectionsResponseItemsItemStatus,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateDetectionRequestModelTypes": ".types",
    "CreateDetectionResponse": ".types",
    "CreateDetectionResponseItem": ".types",
    "CreateDetectionResponseItemIntelligence": ".types",
    "CreateDetectionResponseItemIntelligenceDescription": ".types",
    "GetDetectionResponse": ".types",
    "GetDetectionResponseItem": ".types",
    "GetDetectionResponseItemAudioSourceTracing": ".types",
    "GetDetectionResponseItemIntelligence": ".types",
    "GetDetectionResponseItemIntelligenceDescription": ".types",
    "GetDetectionResponseItemMediaType": ".types",
    "GetDetectionResponseItemStatus": ".types",
    "ListDetectionsResponse": ".types",
    "ListDetectionsResponseItemsItem": ".types",
    "ListDetectionsResponseItemsItemAudioSourceTracing": ".types",
    "ListDetectionsResponseItemsItemMediaType": ".types",
    "ListDetectionsResponseItemsItemStatus": ".types",
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
    "CreateDetectionRequestModelTypes",
    "CreateDetectionResponse",
    "CreateDetectionResponseItem",
    "CreateDetectionResponseItemIntelligence",
    "CreateDetectionResponseItemIntelligenceDescription",
    "GetDetectionResponse",
    "GetDetectionResponseItem",
    "GetDetectionResponseItemAudioSourceTracing",
    "GetDetectionResponseItemIntelligence",
    "GetDetectionResponseItemIntelligenceDescription",
    "GetDetectionResponseItemMediaType",
    "GetDetectionResponseItemStatus",
    "ListDetectionsResponse",
    "ListDetectionsResponseItemsItem",
    "ListDetectionsResponseItemsItemAudioSourceTracing",
    "ListDetectionsResponseItemsItemMediaType",
    "ListDetectionsResponseItemsItemStatus",
]
