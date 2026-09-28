



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .conversation_threshold_get_response import ConversationThresholdGetResponse
    from .conversation_threshold_put_request_threshold import ConversationThresholdPutRequestThreshold
    from .conversation_threshold_put_response import ConversationThresholdPutResponse
    from .conversation_threshold_put_response_threshold import ConversationThresholdPutResponseThreshold
    from .permissions_thresholds_get_response import PermissionsThresholdsGetResponse
    from .permissions_thresholds_get_response_autonomous import PermissionsThresholdsGetResponseAutonomous
    from .permissions_thresholds_get_response_headless import PermissionsThresholdsGetResponseHeadless
    from .permissions_thresholds_get_response_interactive import PermissionsThresholdsGetResponseInteractive
    from .permissions_thresholds_put_request_autonomous import PermissionsThresholdsPutRequestAutonomous
    from .permissions_thresholds_put_request_headless import PermissionsThresholdsPutRequestHeadless
    from .permissions_thresholds_put_request_interactive import PermissionsThresholdsPutRequestInteractive
    from .permissions_thresholds_put_response import PermissionsThresholdsPutResponse
    from .permissions_thresholds_put_response_autonomous import PermissionsThresholdsPutResponseAutonomous
    from .permissions_thresholds_put_response_headless import PermissionsThresholdsPutResponseHeadless
    from .permissions_thresholds_put_response_interactive import PermissionsThresholdsPutResponseInteractive
_dynamic_imports: typing.Dict[str, str] = {
    "ConversationThresholdGetResponse": ".conversation_threshold_get_response",
    "ConversationThresholdPutRequestThreshold": ".conversation_threshold_put_request_threshold",
    "ConversationThresholdPutResponse": ".conversation_threshold_put_response",
    "ConversationThresholdPutResponseThreshold": ".conversation_threshold_put_response_threshold",
    "PermissionsThresholdsGetResponse": ".permissions_thresholds_get_response",
    "PermissionsThresholdsGetResponseAutonomous": ".permissions_thresholds_get_response_autonomous",
    "PermissionsThresholdsGetResponseHeadless": ".permissions_thresholds_get_response_headless",
    "PermissionsThresholdsGetResponseInteractive": ".permissions_thresholds_get_response_interactive",
    "PermissionsThresholdsPutRequestAutonomous": ".permissions_thresholds_put_request_autonomous",
    "PermissionsThresholdsPutRequestHeadless": ".permissions_thresholds_put_request_headless",
    "PermissionsThresholdsPutRequestInteractive": ".permissions_thresholds_put_request_interactive",
    "PermissionsThresholdsPutResponse": ".permissions_thresholds_put_response",
    "PermissionsThresholdsPutResponseAutonomous": ".permissions_thresholds_put_response_autonomous",
    "PermissionsThresholdsPutResponseHeadless": ".permissions_thresholds_put_response_headless",
    "PermissionsThresholdsPutResponseInteractive": ".permissions_thresholds_put_response_interactive",
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
    "ConversationThresholdGetResponse",
    "ConversationThresholdPutRequestThreshold",
    "ConversationThresholdPutResponse",
    "ConversationThresholdPutResponseThreshold",
    "PermissionsThresholdsGetResponse",
    "PermissionsThresholdsGetResponseAutonomous",
    "PermissionsThresholdsGetResponseHeadless",
    "PermissionsThresholdsGetResponseInteractive",
    "PermissionsThresholdsPutRequestAutonomous",
    "PermissionsThresholdsPutRequestHeadless",
    "PermissionsThresholdsPutRequestInteractive",
    "PermissionsThresholdsPutResponse",
    "PermissionsThresholdsPutResponseAutonomous",
    "PermissionsThresholdsPutResponseHeadless",
    "PermissionsThresholdsPutResponseInteractive",
]
