



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_error_body import BadRequestErrorBody
    from .bad_request_error_body_errcode import BadRequestErrorBodyErrcode
    from .bridge_name import BridgeName
    from .bridge_state import BridgeState
    from .bridge_state_state_event import BridgeStateStateEvent
    from .created_group import CreatedGroup
    from .internal_server_error_body import InternalServerErrorBody
    from .internal_server_error_body_errcode import InternalServerErrorBodyErrcode
    from .login_flow import LoginFlow
    from .login_step import (
        LoginStep,
        LoginStep_Complete,
        LoginStep_Cookies,
        LoginStep_DisplayAndWait,
        LoginStep_UserInput,
    )
    from .login_step_complete import LoginStepComplete
    from .login_step_complete_complete import LoginStepCompleteComplete
    from .login_step_cookies import LoginStepCookies
    from .login_step_cookies_cookies import LoginStepCookiesCookies
    from .login_step_cookies_cookies_fields_item import LoginStepCookiesCookiesFieldsItem
    from .login_step_cookies_cookies_fields_item_type import LoginStepCookiesCookiesFieldsItemType
    from .login_step_display_and_wait import LoginStepDisplayAndWait
    from .login_step_display_and_wait_display_and_wait import LoginStepDisplayAndWaitDisplayAndWait
    from .login_step_display_and_wait_display_and_wait_type import LoginStepDisplayAndWaitDisplayAndWaitType
    from .login_step_user_input import LoginStepUserInput
    from .login_step_user_input_user_input import LoginStepUserInputUserInput
    from .login_step_user_input_user_input_fields_item import LoginStepUserInputUserInputFieldsItem
    from .login_step_user_input_user_input_fields_item_type import LoginStepUserInputUserInputFieldsItemType
    from .not_found_error_body import NotFoundErrorBody
    from .not_found_error_body_errcode import NotFoundErrorBodyErrcode
    from .not_implemented_error_body import NotImplementedErrorBody
    from .not_implemented_error_body_errcode import NotImplementedErrorBodyErrcode
    from .remote_profile import RemoteProfile
    from .resolved_identifier import ResolvedIdentifier
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .unauthorized_error_body_errcode import UnauthorizedErrorBodyErrcode
    from .user_login_id import UserLoginId
    from .whoami import Whoami
    from .whoami_login import WhoamiLogin
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestErrorBody": ".bad_request_error_body",
    "BadRequestErrorBodyErrcode": ".bad_request_error_body_errcode",
    "BridgeName": ".bridge_name",
    "BridgeState": ".bridge_state",
    "BridgeStateStateEvent": ".bridge_state_state_event",
    "CreatedGroup": ".created_group",
    "InternalServerErrorBody": ".internal_server_error_body",
    "InternalServerErrorBodyErrcode": ".internal_server_error_body_errcode",
    "LoginFlow": ".login_flow",
    "LoginStep": ".login_step",
    "LoginStepComplete": ".login_step_complete",
    "LoginStepCompleteComplete": ".login_step_complete_complete",
    "LoginStepCookies": ".login_step_cookies",
    "LoginStepCookiesCookies": ".login_step_cookies_cookies",
    "LoginStepCookiesCookiesFieldsItem": ".login_step_cookies_cookies_fields_item",
    "LoginStepCookiesCookiesFieldsItemType": ".login_step_cookies_cookies_fields_item_type",
    "LoginStepDisplayAndWait": ".login_step_display_and_wait",
    "LoginStepDisplayAndWaitDisplayAndWait": ".login_step_display_and_wait_display_and_wait",
    "LoginStepDisplayAndWaitDisplayAndWaitType": ".login_step_display_and_wait_display_and_wait_type",
    "LoginStepUserInput": ".login_step_user_input",
    "LoginStepUserInputUserInput": ".login_step_user_input_user_input",
    "LoginStepUserInputUserInputFieldsItem": ".login_step_user_input_user_input_fields_item",
    "LoginStepUserInputUserInputFieldsItemType": ".login_step_user_input_user_input_fields_item_type",
    "LoginStep_Complete": ".login_step",
    "LoginStep_Cookies": ".login_step",
    "LoginStep_DisplayAndWait": ".login_step",
    "LoginStep_UserInput": ".login_step",
    "NotFoundErrorBody": ".not_found_error_body",
    "NotFoundErrorBodyErrcode": ".not_found_error_body_errcode",
    "NotImplementedErrorBody": ".not_implemented_error_body",
    "NotImplementedErrorBodyErrcode": ".not_implemented_error_body_errcode",
    "RemoteProfile": ".remote_profile",
    "ResolvedIdentifier": ".resolved_identifier",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "UnauthorizedErrorBodyErrcode": ".unauthorized_error_body_errcode",
    "UserLoginId": ".user_login_id",
    "Whoami": ".whoami",
    "WhoamiLogin": ".whoami_login",
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
    "BadRequestErrorBody",
    "BadRequestErrorBodyErrcode",
    "BridgeName",
    "BridgeState",
    "BridgeStateStateEvent",
    "CreatedGroup",
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
    "NotFoundErrorBody",
    "NotFoundErrorBodyErrcode",
    "NotImplementedErrorBody",
    "NotImplementedErrorBodyErrcode",
    "RemoteProfile",
    "ResolvedIdentifier",
    "UnauthorizedErrorBody",
    "UnauthorizedErrorBodyErrcode",
    "UserLoginId",
    "Whoami",
    "WhoamiLogin",
]
