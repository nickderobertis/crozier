



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .admin_stats import AdminStats
    from .agent_binding_info import AgentBindingInfo
    from .app_setting_spec import AppSettingSpec
    from .app_settings_info import AppSettingsInfo
    from .artifact_info import ArtifactInfo
    from .component_health import ComponentHealth
    from .component_health_status import ComponentHealthStatus
    from .error_response import ErrorResponse
    from .health_status import HealthStatus
    from .health_status_status import HealthStatusStatus
    from .http_validation_error import HttpValidationError
    from .llm_options import LlmOptions
    from .me_response import MeResponse
    from .me_response_role import MeResponseRole
    from .message_response import MessageResponse
    from .model_config_info import ModelConfigInfo
    from .page_model_config_info import PageModelConfigInfo
    from .page_provider_info import PageProviderInfo
    from .page_task_list_item import PageTaskListItem
    from .page_token_info import PageTokenInfo
    from .page_user_info import PageUserInfo
    from .progress_event import ProgressEvent
    from .progress_event_status import ProgressEventStatus
    from .provider_info import ProviderInfo
    from .provider_kinds_response import ProviderKindsResponse
    from .task_cancel_accepted import TaskCancelAccepted
    from .task_cancel_accepted_status import TaskCancelAcceptedStatus
    from .task_compile_result import TaskCompileResult
    from .task_created import TaskCreated
    from .task_list_item import TaskListItem
    from .task_progress import TaskProgress
    from .task_result import TaskResult
    from .task_status import TaskStatus
    from .task_status_status import TaskStatusStatus
    from .token_created import TokenCreated
    from .token_info import TokenInfo
    from .user_detail import UserDetail
    from .user_info import UserInfo
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
    from .version_info import VersionInfo
_dynamic_imports: typing.Dict[str, str] = {
    "AdminStats": ".admin_stats",
    "AgentBindingInfo": ".agent_binding_info",
    "AppSettingSpec": ".app_setting_spec",
    "AppSettingsInfo": ".app_settings_info",
    "ArtifactInfo": ".artifact_info",
    "ComponentHealth": ".component_health",
    "ComponentHealthStatus": ".component_health_status",
    "ErrorResponse": ".error_response",
    "HealthStatus": ".health_status",
    "HealthStatusStatus": ".health_status_status",
    "HttpValidationError": ".http_validation_error",
    "LlmOptions": ".llm_options",
    "MeResponse": ".me_response",
    "MeResponseRole": ".me_response_role",
    "MessageResponse": ".message_response",
    "ModelConfigInfo": ".model_config_info",
    "PageModelConfigInfo": ".page_model_config_info",
    "PageProviderInfo": ".page_provider_info",
    "PageTaskListItem": ".page_task_list_item",
    "PageTokenInfo": ".page_token_info",
    "PageUserInfo": ".page_user_info",
    "ProgressEvent": ".progress_event",
    "ProgressEventStatus": ".progress_event_status",
    "ProviderInfo": ".provider_info",
    "ProviderKindsResponse": ".provider_kinds_response",
    "TaskCancelAccepted": ".task_cancel_accepted",
    "TaskCancelAcceptedStatus": ".task_cancel_accepted_status",
    "TaskCompileResult": ".task_compile_result",
    "TaskCreated": ".task_created",
    "TaskListItem": ".task_list_item",
    "TaskProgress": ".task_progress",
    "TaskResult": ".task_result",
    "TaskStatus": ".task_status",
    "TaskStatusStatus": ".task_status_status",
    "TokenCreated": ".token_created",
    "TokenInfo": ".token_info",
    "UserDetail": ".user_detail",
    "UserInfo": ".user_info",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
    "VersionInfo": ".version_info",
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
    "AdminStats",
    "AgentBindingInfo",
    "AppSettingSpec",
    "AppSettingsInfo",
    "ArtifactInfo",
    "ComponentHealth",
    "ComponentHealthStatus",
    "ErrorResponse",
    "HealthStatus",
    "HealthStatusStatus",
    "HttpValidationError",
    "LlmOptions",
    "MeResponse",
    "MeResponseRole",
    "MessageResponse",
    "ModelConfigInfo",
    "PageModelConfigInfo",
    "PageProviderInfo",
    "PageTaskListItem",
    "PageTokenInfo",
    "PageUserInfo",
    "ProgressEvent",
    "ProgressEventStatus",
    "ProviderInfo",
    "ProviderKindsResponse",
    "TaskCancelAccepted",
    "TaskCancelAcceptedStatus",
    "TaskCompileResult",
    "TaskCreated",
    "TaskListItem",
    "TaskProgress",
    "TaskResult",
    "TaskStatus",
    "TaskStatusStatus",
    "TokenCreated",
    "TokenInfo",
    "UserDetail",
    "UserInfo",
    "ValidationError",
    "ValidationErrorLocItem",
    "VersionInfo",
]
