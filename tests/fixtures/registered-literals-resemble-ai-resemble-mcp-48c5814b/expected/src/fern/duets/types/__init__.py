



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_duet_voice_pair_response import CreateDuetVoicePairResponse
    from .create_duet_voice_response import CreateDuetVoiceResponse
    from .delete_duet_voice_response import DeleteDuetVoiceResponse
    from .generate_duet_request_script_item import GenerateDuetRequestScriptItem
    from .generate_duet_response import GenerateDuetResponse
    from .generate_duet_response_item import GenerateDuetResponseItem
    from .list_duet_voice_pairs_response import ListDuetVoicePairsResponse
    from .list_duet_voices_response import ListDuetVoicesResponse
    from .update_duet_voice_response import UpdateDuetVoiceResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateDuetVoicePairResponse": ".create_duet_voice_pair_response",
    "CreateDuetVoiceResponse": ".create_duet_voice_response",
    "DeleteDuetVoiceResponse": ".delete_duet_voice_response",
    "GenerateDuetRequestScriptItem": ".generate_duet_request_script_item",
    "GenerateDuetResponse": ".generate_duet_response",
    "GenerateDuetResponseItem": ".generate_duet_response_item",
    "ListDuetVoicePairsResponse": ".list_duet_voice_pairs_response",
    "ListDuetVoicesResponse": ".list_duet_voices_response",
    "UpdateDuetVoiceResponse": ".update_duet_voice_response",
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
    "CreateDuetVoicePairResponse",
    "CreateDuetVoiceResponse",
    "DeleteDuetVoiceResponse",
    "GenerateDuetRequestScriptItem",
    "GenerateDuetResponse",
    "GenerateDuetResponseItem",
    "ListDuetVoicePairsResponse",
    "ListDuetVoicesResponse",
    "UpdateDuetVoiceResponse",
]
