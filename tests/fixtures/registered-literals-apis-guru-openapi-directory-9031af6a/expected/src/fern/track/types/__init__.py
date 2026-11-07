



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .track_event_request_identification import TrackEventRequestIdentification
    from .track_event_request_identification_account import TrackEventRequestIdentificationAccount
    from .track_event_request_identification_user import TrackEventRequestIdentificationUser
    from .track_event_request_metadata_value import TrackEventRequestMetadataValue
    from .track_event_response import TrackEventResponse
    from .track_event_response_meta import TrackEventResponseMeta
_dynamic_imports: typing.Dict[str, str] = {
    "TrackEventRequestIdentification": ".track_event_request_identification",
    "TrackEventRequestIdentificationAccount": ".track_event_request_identification_account",
    "TrackEventRequestIdentificationUser": ".track_event_request_identification_user",
    "TrackEventRequestMetadataValue": ".track_event_request_metadata_value",
    "TrackEventResponse": ".track_event_response",
    "TrackEventResponseMeta": ".track_event_response_meta",
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
    "TrackEventRequestIdentification",
    "TrackEventRequestIdentificationAccount",
    "TrackEventRequestIdentificationUser",
    "TrackEventRequestMetadataValue",
    "TrackEventResponse",
    "TrackEventResponseMeta",
]
