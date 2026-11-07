



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_detection_request_model_types import CreateDetectionRequestModelTypes
    from .create_detection_response import CreateDetectionResponse
    from .create_detection_response_item import CreateDetectionResponseItem
    from .create_detection_response_item_intelligence import CreateDetectionResponseItemIntelligence
    from .create_detection_response_item_intelligence_description import (
        CreateDetectionResponseItemIntelligenceDescription,
    )
    from .get_detection_response import GetDetectionResponse
    from .get_detection_response_item import GetDetectionResponseItem
    from .get_detection_response_item_audio_source_tracing import GetDetectionResponseItemAudioSourceTracing
    from .get_detection_response_item_intelligence import GetDetectionResponseItemIntelligence
    from .get_detection_response_item_intelligence_description import GetDetectionResponseItemIntelligenceDescription
    from .get_detection_response_item_media_type import GetDetectionResponseItemMediaType
    from .get_detection_response_item_status import GetDetectionResponseItemStatus
    from .list_detections_response import ListDetectionsResponse
    from .list_detections_response_items_item import ListDetectionsResponseItemsItem
    from .list_detections_response_items_item_audio_source_tracing import (
        ListDetectionsResponseItemsItemAudioSourceTracing,
    )
    from .list_detections_response_items_item_media_type import ListDetectionsResponseItemsItemMediaType
    from .list_detections_response_items_item_status import ListDetectionsResponseItemsItemStatus
_dynamic_imports: typing.Dict[str, str] = {
    "CreateDetectionRequestModelTypes": ".create_detection_request_model_types",
    "CreateDetectionResponse": ".create_detection_response",
    "CreateDetectionResponseItem": ".create_detection_response_item",
    "CreateDetectionResponseItemIntelligence": ".create_detection_response_item_intelligence",
    "CreateDetectionResponseItemIntelligenceDescription": ".create_detection_response_item_intelligence_description",
    "GetDetectionResponse": ".get_detection_response",
    "GetDetectionResponseItem": ".get_detection_response_item",
    "GetDetectionResponseItemAudioSourceTracing": ".get_detection_response_item_audio_source_tracing",
    "GetDetectionResponseItemIntelligence": ".get_detection_response_item_intelligence",
    "GetDetectionResponseItemIntelligenceDescription": ".get_detection_response_item_intelligence_description",
    "GetDetectionResponseItemMediaType": ".get_detection_response_item_media_type",
    "GetDetectionResponseItemStatus": ".get_detection_response_item_status",
    "ListDetectionsResponse": ".list_detections_response",
    "ListDetectionsResponseItemsItem": ".list_detections_response_items_item",
    "ListDetectionsResponseItemsItemAudioSourceTracing": ".list_detections_response_items_item_audio_source_tracing",
    "ListDetectionsResponseItemsItemMediaType": ".list_detections_response_items_item_media_type",
    "ListDetectionsResponseItemsItemStatus": ".list_detections_response_items_item_status",
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
