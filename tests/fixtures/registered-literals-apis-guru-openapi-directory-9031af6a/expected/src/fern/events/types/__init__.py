



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_events_response import GetEventsResponse
    from .get_events_response_data_item import GetEventsResponseDataItem
    from .get_events_response_data_item_group import GetEventsResponseDataItemGroup
    from .get_events_response_meta import GetEventsResponseMeta
    from .track_journey_event_request_identification import TrackJourneyEventRequestIdentification
    from .track_journey_event_request_identification_account import TrackJourneyEventRequestIdentificationAccount
    from .track_journey_event_request_identification_user import TrackJourneyEventRequestIdentificationUser
    from .track_journey_event_request_metadata_value import TrackJourneyEventRequestMetadataValue
    from .track_journey_event_response import TrackJourneyEventResponse
    from .track_journey_event_response_meta import TrackJourneyEventResponseMeta
_dynamic_imports: typing.Dict[str, str] = {
    "GetEventsResponse": ".get_events_response",
    "GetEventsResponseDataItem": ".get_events_response_data_item",
    "GetEventsResponseDataItemGroup": ".get_events_response_data_item_group",
    "GetEventsResponseMeta": ".get_events_response_meta",
    "TrackJourneyEventRequestIdentification": ".track_journey_event_request_identification",
    "TrackJourneyEventRequestIdentificationAccount": ".track_journey_event_request_identification_account",
    "TrackJourneyEventRequestIdentificationUser": ".track_journey_event_request_identification_user",
    "TrackJourneyEventRequestMetadataValue": ".track_journey_event_request_metadata_value",
    "TrackJourneyEventResponse": ".track_journey_event_response",
    "TrackJourneyEventResponseMeta": ".track_journey_event_response_meta",
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
    "GetEventsResponse",
    "GetEventsResponseDataItem",
    "GetEventsResponseDataItemGroup",
    "GetEventsResponseMeta",
    "TrackJourneyEventRequestIdentification",
    "TrackJourneyEventRequestIdentificationAccount",
    "TrackJourneyEventRequestIdentificationUser",
    "TrackJourneyEventRequestMetadataValue",
    "TrackJourneyEventResponse",
    "TrackJourneyEventResponseMeta",
]
