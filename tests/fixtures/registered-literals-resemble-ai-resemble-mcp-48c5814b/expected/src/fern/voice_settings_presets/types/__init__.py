



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_voice_settings_preset_response import CreateVoiceSettingsPresetResponse
    from .delete_voice_settings_preset_response import DeleteVoiceSettingsPresetResponse
    from .get_voice_settings_preset_response import GetVoiceSettingsPresetResponse
    from .list_voice_settings_presets_response import ListVoiceSettingsPresetsResponse
    from .update_voice_settings_preset_response import UpdateVoiceSettingsPresetResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateVoiceSettingsPresetResponse": ".create_voice_settings_preset_response",
    "DeleteVoiceSettingsPresetResponse": ".delete_voice_settings_preset_response",
    "GetVoiceSettingsPresetResponse": ".get_voice_settings_preset_response",
    "ListVoiceSettingsPresetsResponse": ".list_voice_settings_presets_response",
    "UpdateVoiceSettingsPresetResponse": ".update_voice_settings_preset_response",
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
    "CreateVoiceSettingsPresetResponse",
    "DeleteVoiceSettingsPresetResponse",
    "GetVoiceSettingsPresetResponse",
    "ListVoiceSettingsPresetsResponse",
    "UpdateVoiceSettingsPresetResponse",
]
