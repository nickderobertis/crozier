



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ActiveInviteLinkState,
        AlreadyMemberProblem,
        Code,
        CodeDelivery,
        Email,
        ExpiredInviteLinkState,
        IntroducedUserState,
        InvalidCodeProblem,
        InviteLink,
        InviteLinkList,
        InviteLinkState,
        InviteLinkState_Active,
        InviteLinkState_Expired,
        InviteLinkState_Revoked,
        Pass,
        Problem,
        RevokedInviteLinkState,
        Team,
        TeamList,
        TeamName,
        UnintroducedUserState,
        User,
        UserState,
        UserState_Introduced,
        UserState_Unintroduced,
        Username,
    )
    from .errors import (
        BadRequestError,
        ConflictError,
        ForbiddenError,
        GoneError,
        InternalServerError,
        NotFoundError,
        TooManyRequestsError,
        UnauthorizedError,
    )
    from . import auth, invite_links, teams, users
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .invite_links import ListInviteLinksRequestStatus
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "ActiveInviteLinkState": ".types",
    "AlreadyMemberProblem": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "Code": ".types",
    "CodeDelivery": ".types",
    "ConflictError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Email": ".types",
    "ExpiredInviteLinkState": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "GoneError": ".errors",
    "InternalServerError": ".errors",
    "IntroducedUserState": ".types",
    "InvalidCodeProblem": ".types",
    "InviteLink": ".types",
    "InviteLinkList": ".types",
    "InviteLinkState": ".types",
    "InviteLinkState_Active": ".types",
    "InviteLinkState_Expired": ".types",
    "InviteLinkState_Revoked": ".types",
    "ListInviteLinksRequestStatus": ".invite_links",
    "NotFoundError": ".errors",
    "Pass": ".types",
    "Problem": ".types",
    "RevokedInviteLinkState": ".types",
    "Team": ".types",
    "TeamList": ".types",
    "TeamName": ".types",
    "TooManyRequestsError": ".errors",
    "UnauthorizedError": ".errors",
    "UnintroducedUserState": ".types",
    "User": ".types",
    "UserState": ".types",
    "UserState_Introduced": ".types",
    "UserState_Unintroduced": ".types",
    "Username": ".types",
    "__version__": ".version",
    "auth": ".auth",
    "invite_links": ".invite_links",
    "teams": ".teams",
    "users": ".users",
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
    "ActiveInviteLinkState",
    "AlreadyMemberProblem",
    "AsyncFernApi",
    "BadRequestError",
    "Code",
    "CodeDelivery",
    "ConflictError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Email",
    "ExpiredInviteLinkState",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "GoneError",
    "InternalServerError",
    "IntroducedUserState",
    "InvalidCodeProblem",
    "InviteLink",
    "InviteLinkList",
    "InviteLinkState",
    "InviteLinkState_Active",
    "InviteLinkState_Expired",
    "InviteLinkState_Revoked",
    "ListInviteLinksRequestStatus",
    "NotFoundError",
    "Pass",
    "Problem",
    "RevokedInviteLinkState",
    "Team",
    "TeamList",
    "TeamName",
    "TooManyRequestsError",
    "UnauthorizedError",
    "UnintroducedUserState",
    "User",
    "UserState",
    "UserState_Introduced",
    "UserState_Unintroduced",
    "Username",
    "__version__",
    "auth",
    "invite_links",
    "teams",
    "users",
]
