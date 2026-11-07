



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BadRequestErrorBody,
        BadRequestErrorBodyErrcode,
        BridgeName,
        BridgeState,
        BridgeStateStateEvent,
        CreatedGroup,
        InternalServerErrorBody,
        InternalServerErrorBodyErrcode,
        LoginFlow,
        LoginStep,
        LoginStepComplete,
        LoginStepCompleteComplete,
        LoginStepCookies,
        LoginStepCookiesCookies,
        LoginStepCookiesCookiesFieldsItem,
        LoginStepCookiesCookiesFieldsItemType,
        LoginStepDisplayAndWait,
        LoginStepDisplayAndWaitDisplayAndWait,
        LoginStepDisplayAndWaitDisplayAndWaitType,
        LoginStepUserInput,
        LoginStepUserInputUserInput,
        LoginStepUserInputUserInputFieldsItem,
        LoginStepUserInputUserInputFieldsItemType,
        LoginStep_Complete,
        LoginStep_Cookies,
        LoginStep_DisplayAndWait,
        LoginStep_UserInput,
        NotFoundErrorBody,
        NotFoundErrorBodyErrcode,
        NotImplementedErrorBody,
        NotImplementedErrorBodyErrcode,
        RemoteProfile,
        ResolvedIdentifier,
        UnauthorizedErrorBody,
        UnauthorizedErrorBodyErrcode,
        UserLoginId,
        Whoami,
        WhoamiLogin,
    )
    from .errors import BadRequestError, InternalServerError, NotFoundError, NotImplementedError, UnauthorizedError
    from . import auth, snc
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .auth import GetLoginFlowsResponse, GetLoginIDsResponse, LogoutRequestLoginId, LogoutRequestLoginIdOne
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .snc import (
        CreateDmResponse,
        GetContactsResponse,
        GroupCreateParamsAvatar,
        GroupCreateParamsDisappear,
        GroupCreateParamsName,
        GroupCreateParamsTopic,
        SearchUsersResponse,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BadRequestErrorBody": ".types",
    "BadRequestErrorBodyErrcode": ".types",
    "BridgeName": ".types",
    "BridgeState": ".types",
    "BridgeStateStateEvent": ".types",
    "CreateDmResponse": ".snc",
    "CreatedGroup": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetContactsResponse": ".snc",
    "GetLoginFlowsResponse": ".auth",
    "GetLoginIDsResponse": ".auth",
    "GroupCreateParamsAvatar": ".snc",
    "GroupCreateParamsDisappear": ".snc",
    "GroupCreateParamsName": ".snc",
    "GroupCreateParamsTopic": ".snc",
    "InternalServerError": ".errors",
    "InternalServerErrorBody": ".types",
    "InternalServerErrorBodyErrcode": ".types",
    "LoginFlow": ".types",
    "LoginStep": ".types",
    "LoginStepComplete": ".types",
    "LoginStepCompleteComplete": ".types",
    "LoginStepCookies": ".types",
    "LoginStepCookiesCookies": ".types",
    "LoginStepCookiesCookiesFieldsItem": ".types",
    "LoginStepCookiesCookiesFieldsItemType": ".types",
    "LoginStepDisplayAndWait": ".types",
    "LoginStepDisplayAndWaitDisplayAndWait": ".types",
    "LoginStepDisplayAndWaitDisplayAndWaitType": ".types",
    "LoginStepUserInput": ".types",
    "LoginStepUserInputUserInput": ".types",
    "LoginStepUserInputUserInputFieldsItem": ".types",
    "LoginStepUserInputUserInputFieldsItemType": ".types",
    "LoginStep_Complete": ".types",
    "LoginStep_Cookies": ".types",
    "LoginStep_DisplayAndWait": ".types",
    "LoginStep_UserInput": ".types",
    "LogoutRequestLoginId": ".auth",
    "LogoutRequestLoginIdOne": ".auth",
    "NotFoundError": ".errors",
    "NotFoundErrorBody": ".types",
    "NotFoundErrorBodyErrcode": ".types",
    "NotImplementedError": ".errors",
    "NotImplementedErrorBody": ".types",
    "NotImplementedErrorBodyErrcode": ".types",
    "RemoteProfile": ".types",
    "ResolvedIdentifier": ".types",
    "SearchUsersResponse": ".snc",
    "UnauthorizedError": ".errors",
    "UnauthorizedErrorBody": ".types",
    "UnauthorizedErrorBodyErrcode": ".types",
    "UserLoginId": ".types",
    "Whoami": ".types",
    "WhoamiLogin": ".types",
    "__version__": ".version",
    "auth": ".auth",
    "snc": ".snc",
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
    "AsyncFernApi",
    "BadRequestError",
    "BadRequestErrorBody",
    "BadRequestErrorBodyErrcode",
    "BridgeName",
    "BridgeState",
    "BridgeStateStateEvent",
    "CreateDmResponse",
    "CreatedGroup",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "GetContactsResponse",
    "GetLoginFlowsResponse",
    "GetLoginIDsResponse",
    "GroupCreateParamsAvatar",
    "GroupCreateParamsDisappear",
    "GroupCreateParamsName",
    "GroupCreateParamsTopic",
    "InternalServerError",
    "InternalServerErrorBody",
    "InternalServerErrorBodyErrcode",
    "LoginFlow",
    "LoginStep",
    "LoginStepComplete",
    "LoginStepCompleteComplete",
    "LoginStepCookies",
    "LoginStepCookiesCookies",
    "LoginStepCookiesCookiesFieldsItem",
    "LoginStepCookiesCookiesFieldsItemType",
    "LoginStepDisplayAndWait",
    "LoginStepDisplayAndWaitDisplayAndWait",
    "LoginStepDisplayAndWaitDisplayAndWaitType",
    "LoginStepUserInput",
    "LoginStepUserInputUserInput",
    "LoginStepUserInputUserInputFieldsItem",
    "LoginStepUserInputUserInputFieldsItemType",
    "LoginStep_Complete",
    "LoginStep_Cookies",
    "LoginStep_DisplayAndWait",
    "LoginStep_UserInput",
    "LogoutRequestLoginId",
    "LogoutRequestLoginIdOne",
    "NotFoundError",
    "NotFoundErrorBody",
    "NotFoundErrorBodyErrcode",
    "NotImplementedError",
    "NotImplementedErrorBody",
    "NotImplementedErrorBodyErrcode",
    "RemoteProfile",
    "ResolvedIdentifier",
    "SearchUsersResponse",
    "UnauthorizedError",
    "UnauthorizedErrorBody",
    "UnauthorizedErrorBodyErrcode",
    "UserLoginId",
    "Whoami",
    "WhoamiLogin",
    "__version__",
    "auth",
    "snc",
]
