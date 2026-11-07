



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_audio_source_tracing_response import GetAudioSourceTracingResponse
    from .get_audio_source_tracing_response_item import GetAudioSourceTracingResponseItem
    from .get_audio_source_tracing_response_item_results import GetAudioSourceTracingResponseItemResults
    from .list_audio_source_tracings_response import ListAudioSourceTracingsResponse
    from .list_audio_source_tracings_response_items_item import ListAudioSourceTracingsResponseItemsItem
    from .list_audio_source_tracings_response_items_item_results import ListAudioSourceTracingsResponseItemsItemResults
_dynamic_imports: typing.Dict[str, str] = {
    "GetAudioSourceTracingResponse": ".get_audio_source_tracing_response",
    "GetAudioSourceTracingResponseItem": ".get_audio_source_tracing_response_item",
    "GetAudioSourceTracingResponseItemResults": ".get_audio_source_tracing_response_item_results",
    "ListAudioSourceTracingsResponse": ".list_audio_source_tracings_response",
    "ListAudioSourceTracingsResponseItemsItem": ".list_audio_source_tracings_response_items_item",
    "ListAudioSourceTracingsResponseItemsItemResults": ".list_audio_source_tracings_response_items_item_results",
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
    "GetAudioSourceTracingResponse",
    "GetAudioSourceTracingResponseItem",
    "GetAudioSourceTracingResponseItemResults",
    "ListAudioSourceTracingsResponse",
    "ListAudioSourceTracingsResponseItemsItem",
    "ListAudioSourceTracingsResponseItemsItemResults",
]
