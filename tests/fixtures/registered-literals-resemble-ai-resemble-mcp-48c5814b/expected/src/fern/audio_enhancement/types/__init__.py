



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_audio_enhancement_request_enhancement_engine import CreateAudioEnhancementRequestEnhancementEngine
    from .create_audio_enhancement_response import CreateAudioEnhancementResponse
    from .create_audio_enhancement_response_status import CreateAudioEnhancementResponseStatus
    from .get_audio_enhancement_response import GetAudioEnhancementResponse
    from .get_audio_enhancement_response_status import GetAudioEnhancementResponseStatus
    from .list_audio_enhancements_response import ListAudioEnhancementsResponse
    from .list_audio_enhancements_response_items_item import ListAudioEnhancementsResponseItemsItem
    from .list_audio_enhancements_response_items_item_enhancement_engine import (
        ListAudioEnhancementsResponseItemsItemEnhancementEngine,
    )
    from .list_audio_enhancements_response_items_item_status import ListAudioEnhancementsResponseItemsItemStatus
_dynamic_imports: typing.Dict[str, str] = {
    "CreateAudioEnhancementRequestEnhancementEngine": ".create_audio_enhancement_request_enhancement_engine",
    "CreateAudioEnhancementResponse": ".create_audio_enhancement_response",
    "CreateAudioEnhancementResponseStatus": ".create_audio_enhancement_response_status",
    "GetAudioEnhancementResponse": ".get_audio_enhancement_response",
    "GetAudioEnhancementResponseStatus": ".get_audio_enhancement_response_status",
    "ListAudioEnhancementsResponse": ".list_audio_enhancements_response",
    "ListAudioEnhancementsResponseItemsItem": ".list_audio_enhancements_response_items_item",
    "ListAudioEnhancementsResponseItemsItemEnhancementEngine": ".list_audio_enhancements_response_items_item_enhancement_engine",
    "ListAudioEnhancementsResponseItemsItemStatus": ".list_audio_enhancements_response_items_item_status",
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
    "CreateAudioEnhancementRequestEnhancementEngine",
    "CreateAudioEnhancementResponse",
    "CreateAudioEnhancementResponseStatus",
    "GetAudioEnhancementResponse",
    "GetAudioEnhancementResponseStatus",
    "ListAudioEnhancementsResponse",
    "ListAudioEnhancementsResponseItemsItem",
    "ListAudioEnhancementsResponseItemsItemEnhancementEngine",
    "ListAudioEnhancementsResponseItemsItemStatus",
]
