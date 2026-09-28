



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .feature_flags_get_response import FeatureFlagsGetResponse
    from .feature_flags_get_response_flags_item import FeatureFlagsGetResponseFlagsItem
    from .feature_flags_get_response_flags_item_default_enabled import FeatureFlagsGetResponseFlagsItemDefaultEnabled
    from .feature_flags_get_response_flags_item_enabled import FeatureFlagsGetResponseFlagsItemEnabled
    from .feature_flags_patch_request_enabled import FeatureFlagsPatchRequestEnabled
    from .feature_flags_patch_response import FeatureFlagsPatchResponse
    from .feature_flags_patch_response_enabled import FeatureFlagsPatchResponseEnabled
_dynamic_imports: typing.Dict[str, str] = {
    "FeatureFlagsGetResponse": ".feature_flags_get_response",
    "FeatureFlagsGetResponseFlagsItem": ".feature_flags_get_response_flags_item",
    "FeatureFlagsGetResponseFlagsItemDefaultEnabled": ".feature_flags_get_response_flags_item_default_enabled",
    "FeatureFlagsGetResponseFlagsItemEnabled": ".feature_flags_get_response_flags_item_enabled",
    "FeatureFlagsPatchRequestEnabled": ".feature_flags_patch_request_enabled",
    "FeatureFlagsPatchResponse": ".feature_flags_patch_response",
    "FeatureFlagsPatchResponseEnabled": ".feature_flags_patch_response_enabled",
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
    "FeatureFlagsGetResponse",
    "FeatureFlagsGetResponseFlagsItem",
    "FeatureFlagsGetResponseFlagsItemDefaultEnabled",
    "FeatureFlagsGetResponseFlagsItemEnabled",
    "FeatureFlagsPatchRequestEnabled",
    "FeatureFlagsPatchResponse",
    "FeatureFlagsPatchResponseEnabled",
]
