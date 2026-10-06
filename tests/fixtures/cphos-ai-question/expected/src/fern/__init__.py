



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AdminStats,
        AgentBindingInfo,
        AppSettingSpec,
        AppSettingsInfo,
        ArtifactInfo,
        ComponentHealth,
        ComponentHealthStatus,
        ErrorResponse,
        HealthStatus,
        HealthStatusStatus,
        HttpValidationError,
        LlmOptions,
        MeResponse,
        MeResponseRole,
        MessageResponse,
        ModelConfigInfo,
        PageModelConfigInfo,
        PageProviderInfo,
        PageTaskListItem,
        PageTokenInfo,
        PageUserInfo,
        ProgressEvent,
        ProgressEventStatus,
        ProviderInfo,
        ProviderKindsResponse,
        TaskCancelAccepted,
        TaskCancelAcceptedStatus,
        TaskCompileResult,
        TaskCreated,
        TaskListItem,
        TaskProgress,
        TaskResult,
        TaskStatus,
        TaskStatusStatus,
        TokenCreated,
        TokenInfo,
        UserDetail,
        UserInfo,
        ValidationError,
        ValidationErrorLocItem,
        VersionInfo,
    )
    from .errors import ConflictError, ForbiddenError, NotFoundError, UnauthorizedError, UnprocessableEntityError
    from . import admin, llm_settings, system, tasks
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .admin import CreateTokenRequestRole
    from .client import AsyncFernApi, FernApi
    from .llm_settings import AppSettingsUpdateLatexCompilerBackend
    from .tasks import GenerateRequestMode
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AdminStats": ".types",
    "AgentBindingInfo": ".types",
    "AppSettingSpec": ".types",
    "AppSettingsInfo": ".types",
    "AppSettingsUpdateLatexCompilerBackend": ".llm_settings",
    "ArtifactInfo": ".types",
    "AsyncFernApi": ".client",
    "ComponentHealth": ".types",
    "ComponentHealthStatus": ".types",
    "ConflictError": ".errors",
    "CreateTokenRequestRole": ".admin",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "ErrorResponse": ".types",
    "FernApi": ".client",
    "ForbiddenError": ".errors",
    "GenerateRequestMode": ".tasks",
    "HealthStatus": ".types",
    "HealthStatusStatus": ".types",
    "HttpValidationError": ".types",
    "LlmOptions": ".types",
    "MeResponse": ".types",
    "MeResponseRole": ".types",
    "MessageResponse": ".types",
    "ModelConfigInfo": ".types",
    "NotFoundError": ".errors",
    "PageModelConfigInfo": ".types",
    "PageProviderInfo": ".types",
    "PageTaskListItem": ".types",
    "PageTokenInfo": ".types",
    "PageUserInfo": ".types",
    "ProgressEvent": ".types",
    "ProgressEventStatus": ".types",
    "ProviderInfo": ".types",
    "ProviderKindsResponse": ".types",
    "TaskCancelAccepted": ".types",
    "TaskCancelAcceptedStatus": ".types",
    "TaskCompileResult": ".types",
    "TaskCreated": ".types",
    "TaskListItem": ".types",
    "TaskProgress": ".types",
    "TaskResult": ".types",
    "TaskStatus": ".types",
    "TaskStatusStatus": ".types",
    "TokenCreated": ".types",
    "TokenInfo": ".types",
    "UnauthorizedError": ".errors",
    "UnprocessableEntityError": ".errors",
    "UserDetail": ".types",
    "UserInfo": ".types",
    "ValidationError": ".types",
    "ValidationErrorLocItem": ".types",
    "VersionInfo": ".types",
    "__version__": ".version",
    "admin": ".admin",
    "llm_settings": ".llm_settings",
    "system": ".system",
    "tasks": ".tasks",
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
    "AppSettingsUpdateLatexCompilerBackend",
    "ArtifactInfo",
    "AsyncFernApi",
    "ComponentHealth",
    "ComponentHealthStatus",
    "ConflictError",
    "CreateTokenRequestRole",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "ErrorResponse",
    "FernApi",
    "ForbiddenError",
    "GenerateRequestMode",
    "HealthStatus",
    "HealthStatusStatus",
    "HttpValidationError",
    "LlmOptions",
    "MeResponse",
    "MeResponseRole",
    "MessageResponse",
    "ModelConfigInfo",
    "NotFoundError",
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
    "UnauthorizedError",
    "UnprocessableEntityError",
    "UserDetail",
    "UserInfo",
    "ValidationError",
    "ValidationErrorLocItem",
    "VersionInfo",
    "__version__",
    "admin",
    "llm_settings",
    "system",
    "tasks",
]
