



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_audio_edit_response import CreateAudioEditResponse
    from .create_audio_edit_response_item import CreateAudioEditResponseItem
    from .get_audio_edit_response import GetAudioEditResponse
    from .get_audio_edit_response_item import GetAudioEditResponseItem
    from .list_audio_edits_response import ListAudioEditsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateAudioEditResponse": ".create_audio_edit_response",
    "CreateAudioEditResponseItem": ".create_audio_edit_response_item",
    "GetAudioEditResponse": ".get_audio_edit_response",
    "GetAudioEditResponseItem": ".get_audio_edit_response_item",
    "ListAudioEditsResponse": ".list_audio_edits_response",
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
    "CreateAudioEditResponse",
    "CreateAudioEditResponseItem",
    "GetAudioEditResponse",
    "GetAudioEditResponseItem",
    "ListAudioEditsResponse",
]
