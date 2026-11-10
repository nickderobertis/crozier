



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_live_activity_job_request import CreateLiveActivityJobRequest
    from .live_activity_action import LiveActivityAction
    from .live_activity_activity_id_scope import LiveActivityActivityIdScope
    from .live_activity_end_job_request import LiveActivityEndJobRequest
    from .live_activity_end_job_request_action import LiveActivityEndJobRequestAction
    from .live_activity_job_response import LiveActivityJobResponse
    from .live_activity_job_response_status import LiveActivityJobResponseStatus
    from .live_activity_job_target import LiveActivityJobTarget
    from .live_activity_options import LiveActivityOptions
    from .live_activity_options_alert import LiveActivityOptionsAlert
    from .live_activity_options_dismissal_date import LiveActivityOptionsDismissalDate
    from .live_activity_options_expiration import LiveActivityOptionsExpiration
    from .live_activity_options_priority import LiveActivityOptionsPriority
    from .live_activity_options_priority_zero import LiveActivityOptionsPriorityZero
    from .live_activity_options_stale_date import LiveActivityOptionsStaleDate
    from .live_activity_options_timestamp import LiveActivityOptionsTimestamp
    from .live_activity_scoped_lookup import LiveActivityScopedLookup
    from .live_activity_start_job_request import LiveActivityStartJobRequest
    from .live_activity_start_job_request_action import LiveActivityStartJobRequestAction
    from .live_activity_token import LiveActivityToken
    from .live_activity_token_type import LiveActivityTokenType
    from .live_activity_topic_scope import LiveActivityTopicScope
    from .live_activity_update_job_request import LiveActivityUpdateJobRequest
    from .live_activity_update_job_request_action import LiveActivityUpdateJobRequestAction
    from .live_activity_user_scope import LiveActivityUserScope
    from .live_activity_user_topic_subscription import LiveActivityUserTopicSubscription
    from .notification_payload import NotificationPayload
    from .notification_payload_priority import NotificationPayloadPriority
    from .paginated_publish_jobs import PaginatedPublishJobs
    from .paginated_topic_subscribers import PaginatedTopicSubscribers
    from .paginated_users import PaginatedUsers
    from .platform import Platform
    from .publish_job import PublishJob
    from .publish_job_status import PublishJobStatus
    from .queued_job_response import QueuedJobResponse
    from .send_notification_request import SendNotificationRequest
    from .token import Token
    from .topic import Topic
    from .topic_subscriber import TopicSubscriber
    from .user import User
    from .user_topic_subscription import UserTopicSubscription
_dynamic_imports: typing.Dict[str, str] = {
    "CreateLiveActivityJobRequest": ".create_live_activity_job_request",
    "LiveActivityAction": ".live_activity_action",
    "LiveActivityActivityIdScope": ".live_activity_activity_id_scope",
    "LiveActivityEndJobRequest": ".live_activity_end_job_request",
    "LiveActivityEndJobRequestAction": ".live_activity_end_job_request_action",
    "LiveActivityJobResponse": ".live_activity_job_response",
    "LiveActivityJobResponseStatus": ".live_activity_job_response_status",
    "LiveActivityJobTarget": ".live_activity_job_target",
    "LiveActivityOptions": ".live_activity_options",
    "LiveActivityOptionsAlert": ".live_activity_options_alert",
    "LiveActivityOptionsDismissalDate": ".live_activity_options_dismissal_date",
    "LiveActivityOptionsExpiration": ".live_activity_options_expiration",
    "LiveActivityOptionsPriority": ".live_activity_options_priority",
    "LiveActivityOptionsPriorityZero": ".live_activity_options_priority_zero",
    "LiveActivityOptionsStaleDate": ".live_activity_options_stale_date",
    "LiveActivityOptionsTimestamp": ".live_activity_options_timestamp",
    "LiveActivityScopedLookup": ".live_activity_scoped_lookup",
    "LiveActivityStartJobRequest": ".live_activity_start_job_request",
    "LiveActivityStartJobRequestAction": ".live_activity_start_job_request_action",
    "LiveActivityToken": ".live_activity_token",
    "LiveActivityTokenType": ".live_activity_token_type",
    "LiveActivityTopicScope": ".live_activity_topic_scope",
    "LiveActivityUpdateJobRequest": ".live_activity_update_job_request",
    "LiveActivityUpdateJobRequestAction": ".live_activity_update_job_request_action",
    "LiveActivityUserScope": ".live_activity_user_scope",
    "LiveActivityUserTopicSubscription": ".live_activity_user_topic_subscription",
    "NotificationPayload": ".notification_payload",
    "NotificationPayloadPriority": ".notification_payload_priority",
    "PaginatedPublishJobs": ".paginated_publish_jobs",
    "PaginatedTopicSubscribers": ".paginated_topic_subscribers",
    "PaginatedUsers": ".paginated_users",
    "Platform": ".platform",
    "PublishJob": ".publish_job",
    "PublishJobStatus": ".publish_job_status",
    "QueuedJobResponse": ".queued_job_response",
    "SendNotificationRequest": ".send_notification_request",
    "Token": ".token",
    "Topic": ".topic",
    "TopicSubscriber": ".topic_subscriber",
    "User": ".user",
    "UserTopicSubscription": ".user_topic_subscription",
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
    "CreateLiveActivityJobRequest",
    "LiveActivityAction",
    "LiveActivityActivityIdScope",
    "LiveActivityEndJobRequest",
    "LiveActivityEndJobRequestAction",
    "LiveActivityJobResponse",
    "LiveActivityJobResponseStatus",
    "LiveActivityJobTarget",
    "LiveActivityOptions",
    "LiveActivityOptionsAlert",
    "LiveActivityOptionsDismissalDate",
    "LiveActivityOptionsExpiration",
    "LiveActivityOptionsPriority",
    "LiveActivityOptionsPriorityZero",
    "LiveActivityOptionsStaleDate",
    "LiveActivityOptionsTimestamp",
    "LiveActivityScopedLookup",
    "LiveActivityStartJobRequest",
    "LiveActivityStartJobRequestAction",
    "LiveActivityToken",
    "LiveActivityTokenType",
    "LiveActivityTopicScope",
    "LiveActivityUpdateJobRequest",
    "LiveActivityUpdateJobRequestAction",
    "LiveActivityUserScope",
    "LiveActivityUserTopicSubscription",
    "NotificationPayload",
    "NotificationPayloadPriority",
    "PaginatedPublishJobs",
    "PaginatedTopicSubscribers",
    "PaginatedUsers",
    "Platform",
    "PublishJob",
    "PublishJobStatus",
    "QueuedJobResponse",
    "SendNotificationRequest",
    "Token",
    "Topic",
    "TopicSubscriber",
    "User",
    "UserTopicSubscription",
]
