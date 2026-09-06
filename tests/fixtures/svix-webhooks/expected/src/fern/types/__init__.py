



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .app_portal_access_out import AppPortalAccessOut
    from .application_in import ApplicationIn
    from .application_out import ApplicationOut
    from .background_task_status import BackgroundTaskStatus
    from .background_task_type import BackgroundTaskType
    from .bulk_expunge_contents_out import BulkExpungeContentsOut
    from .bulk_expunge_status import BulkExpungeStatus
    from .empty_response import EmptyResponse
    from .endpoint_created_event import EndpointCreatedEvent
    from .endpoint_created_event_data import EndpointCreatedEventData
    from .endpoint_created_event_type import EndpointCreatedEventType
    from .endpoint_deleted_event import EndpointDeletedEvent
    from .endpoint_deleted_event_data import EndpointDeletedEventData
    from .endpoint_deleted_event_type import EndpointDeletedEventType
    from .endpoint_disabled_event import EndpointDisabledEvent
    from .endpoint_disabled_event_data import EndpointDisabledEventData
    from .endpoint_disabled_event_type import EndpointDisabledEventType
    from .endpoint_headers_out import EndpointHeadersOut
    from .endpoint_message_out import EndpointMessageOut
    from .endpoint_out import EndpointOut
    from .endpoint_secret_out import EndpointSecretOut
    from .endpoint_stats import EndpointStats
    from .endpoint_stats_range import EndpointStatsRange
    from .endpoint_updated_event import EndpointUpdatedEvent
    from .endpoint_updated_event_data import EndpointUpdatedEventData
    from .endpoint_updated_event_type import EndpointUpdatedEventType
    from .event_type_out import EventTypeOut
    from .http_error_out import HttpErrorOut
    from .http_validation_error import HttpValidationError
    from .list_response_application_out import ListResponseApplicationOut
    from .list_response_endpoint_message_out import ListResponseEndpointMessageOut
    from .list_response_endpoint_out import ListResponseEndpointOut
    from .list_response_event_type_out import ListResponseEventTypeOut
    from .list_response_message_attempt_out import ListResponseMessageAttemptOut
    from .list_response_message_endpoint_out import ListResponseMessageEndpointOut
    from .list_response_message_out import ListResponseMessageOut
    from .message_attempet_last import MessageAttempetLast
    from .message_attempt_exhausted_event import MessageAttemptExhaustedEvent
    from .message_attempt_exhausted_event_data import MessageAttemptExhaustedEventData
    from .message_attempt_exhausted_event_type import MessageAttemptExhaustedEventType
    from .message_attempt_failing_event import MessageAttemptFailingEvent
    from .message_attempt_failing_event_data import MessageAttemptFailingEventData
    from .message_attempt_failing_event_type import MessageAttemptFailingEventType
    from .message_attempt_out import MessageAttemptOut
    from .message_attempt_recovered_event import MessageAttemptRecoveredEvent
    from .message_attempt_recovered_event_data import MessageAttemptRecoveredEventData
    from .message_attempt_recovered_event_type import MessageAttemptRecoveredEventType
    from .message_attempt_trigger_type import MessageAttemptTriggerType
    from .message_endpoint_out import MessageEndpointOut
    from .message_out import MessageOut
    from .message_status import MessageStatus
    from .message_status_text import MessageStatusText
    from .ordering import Ordering
    from .recover_out import RecoverOut
    from .status_code_class import StatusCodeClass
    from .validation_error_item import ValidationErrorItem
_dynamic_imports: typing.Dict[str, str] = {
    "AppPortalAccessOut": ".app_portal_access_out",
    "ApplicationIn": ".application_in",
    "ApplicationOut": ".application_out",
    "BackgroundTaskStatus": ".background_task_status",
    "BackgroundTaskType": ".background_task_type",
    "BulkExpungeContentsOut": ".bulk_expunge_contents_out",
    "BulkExpungeStatus": ".bulk_expunge_status",
    "EmptyResponse": ".empty_response",
    "EndpointCreatedEvent": ".endpoint_created_event",
    "EndpointCreatedEventData": ".endpoint_created_event_data",
    "EndpointCreatedEventType": ".endpoint_created_event_type",
    "EndpointDeletedEvent": ".endpoint_deleted_event",
    "EndpointDeletedEventData": ".endpoint_deleted_event_data",
    "EndpointDeletedEventType": ".endpoint_deleted_event_type",
    "EndpointDisabledEvent": ".endpoint_disabled_event",
    "EndpointDisabledEventData": ".endpoint_disabled_event_data",
    "EndpointDisabledEventType": ".endpoint_disabled_event_type",
    "EndpointHeadersOut": ".endpoint_headers_out",
    "EndpointMessageOut": ".endpoint_message_out",
    "EndpointOut": ".endpoint_out",
    "EndpointSecretOut": ".endpoint_secret_out",
    "EndpointStats": ".endpoint_stats",
    "EndpointStatsRange": ".endpoint_stats_range",
    "EndpointUpdatedEvent": ".endpoint_updated_event",
    "EndpointUpdatedEventData": ".endpoint_updated_event_data",
    "EndpointUpdatedEventType": ".endpoint_updated_event_type",
    "EventTypeOut": ".event_type_out",
    "HttpErrorOut": ".http_error_out",
    "HttpValidationError": ".http_validation_error",
    "ListResponseApplicationOut": ".list_response_application_out",
    "ListResponseEndpointMessageOut": ".list_response_endpoint_message_out",
    "ListResponseEndpointOut": ".list_response_endpoint_out",
    "ListResponseEventTypeOut": ".list_response_event_type_out",
    "ListResponseMessageAttemptOut": ".list_response_message_attempt_out",
    "ListResponseMessageEndpointOut": ".list_response_message_endpoint_out",
    "ListResponseMessageOut": ".list_response_message_out",
    "MessageAttempetLast": ".message_attempet_last",
    "MessageAttemptExhaustedEvent": ".message_attempt_exhausted_event",
    "MessageAttemptExhaustedEventData": ".message_attempt_exhausted_event_data",
    "MessageAttemptExhaustedEventType": ".message_attempt_exhausted_event_type",
    "MessageAttemptFailingEvent": ".message_attempt_failing_event",
    "MessageAttemptFailingEventData": ".message_attempt_failing_event_data",
    "MessageAttemptFailingEventType": ".message_attempt_failing_event_type",
    "MessageAttemptOut": ".message_attempt_out",
    "MessageAttemptRecoveredEvent": ".message_attempt_recovered_event",
    "MessageAttemptRecoveredEventData": ".message_attempt_recovered_event_data",
    "MessageAttemptRecoveredEventType": ".message_attempt_recovered_event_type",
    "MessageAttemptTriggerType": ".message_attempt_trigger_type",
    "MessageEndpointOut": ".message_endpoint_out",
    "MessageOut": ".message_out",
    "MessageStatus": ".message_status",
    "MessageStatusText": ".message_status_text",
    "Ordering": ".ordering",
    "RecoverOut": ".recover_out",
    "StatusCodeClass": ".status_code_class",
    "ValidationErrorItem": ".validation_error_item",
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
    "AppPortalAccessOut",
    "ApplicationIn",
    "ApplicationOut",
    "BackgroundTaskStatus",
    "BackgroundTaskType",
    "BulkExpungeContentsOut",
    "BulkExpungeStatus",
    "EmptyResponse",
    "EndpointCreatedEvent",
    "EndpointCreatedEventData",
    "EndpointCreatedEventType",
    "EndpointDeletedEvent",
    "EndpointDeletedEventData",
    "EndpointDeletedEventType",
    "EndpointDisabledEvent",
    "EndpointDisabledEventData",
    "EndpointDisabledEventType",
    "EndpointHeadersOut",
    "EndpointMessageOut",
    "EndpointOut",
    "EndpointSecretOut",
    "EndpointStats",
    "EndpointStatsRange",
    "EndpointUpdatedEvent",
    "EndpointUpdatedEventData",
    "EndpointUpdatedEventType",
    "EventTypeOut",
    "HttpErrorOut",
    "HttpValidationError",
    "ListResponseApplicationOut",
    "ListResponseEndpointMessageOut",
    "ListResponseEndpointOut",
    "ListResponseEventTypeOut",
    "ListResponseMessageAttemptOut",
    "ListResponseMessageEndpointOut",
    "ListResponseMessageOut",
    "MessageAttempetLast",
    "MessageAttemptExhaustedEvent",
    "MessageAttemptExhaustedEventData",
    "MessageAttemptExhaustedEventType",
    "MessageAttemptFailingEvent",
    "MessageAttemptFailingEventData",
    "MessageAttemptFailingEventType",
    "MessageAttemptOut",
    "MessageAttemptRecoveredEvent",
    "MessageAttemptRecoveredEventData",
    "MessageAttemptRecoveredEventType",
    "MessageAttemptTriggerType",
    "MessageEndpointOut",
    "MessageOut",
    "MessageStatus",
    "MessageStatusText",
    "Ordering",
    "RecoverOut",
    "StatusCodeClass",
    "ValidationErrorItem",
]
