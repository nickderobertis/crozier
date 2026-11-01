



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .active_invite_link_state import ActiveInviteLinkState
    from .already_member_problem import AlreadyMemberProblem
    from .code import Code
    from .code_delivery import CodeDelivery
    from .email import Email
    from .expired_invite_link_state import ExpiredInviteLinkState
    from .introduced_user_state import IntroducedUserState
    from .invalid_code_problem import InvalidCodeProblem
    from .invite_link import InviteLink
    from .invite_link_list import InviteLinkList
    from .invite_link_state import (
        InviteLinkState,
        InviteLinkState_Active,
        InviteLinkState_Expired,
        InviteLinkState_Revoked,
    )
    from .pass_ import Pass
    from .problem import Problem
    from .revoked_invite_link_state import RevokedInviteLinkState
    from .team import Team
    from .team_list import TeamList
    from .team_name import TeamName
    from .unintroduced_user_state import UnintroducedUserState
    from .user import User
    from .user_state import UserState, UserState_Introduced, UserState_Unintroduced
    from .username import Username
_dynamic_imports: typing.Dict[str, str] = {
    "ActiveInviteLinkState": ".active_invite_link_state",
    "AlreadyMemberProblem": ".already_member_problem",
    "Code": ".code",
    "CodeDelivery": ".code_delivery",
    "Email": ".email",
    "ExpiredInviteLinkState": ".expired_invite_link_state",
    "IntroducedUserState": ".introduced_user_state",
    "InvalidCodeProblem": ".invalid_code_problem",
    "InviteLink": ".invite_link",
    "InviteLinkList": ".invite_link_list",
    "InviteLinkState": ".invite_link_state",
    "InviteLinkState_Active": ".invite_link_state",
    "InviteLinkState_Expired": ".invite_link_state",
    "InviteLinkState_Revoked": ".invite_link_state",
    "Pass": ".pass_",
    "Problem": ".problem",
    "RevokedInviteLinkState": ".revoked_invite_link_state",
    "Team": ".team",
    "TeamList": ".team_list",
    "TeamName": ".team_name",
    "UnintroducedUserState": ".unintroduced_user_state",
    "User": ".user",
    "UserState": ".user_state",
    "UserState_Introduced": ".user_state",
    "UserState_Unintroduced": ".user_state",
    "Username": ".username",
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
    "Code",
    "CodeDelivery",
    "Email",
    "ExpiredInviteLinkState",
    "IntroducedUserState",
    "InvalidCodeProblem",
    "InviteLink",
    "InviteLinkList",
    "InviteLinkState",
    "InviteLinkState_Active",
    "InviteLinkState_Expired",
    "InviteLinkState_Revoked",
    "Pass",
    "Problem",
    "RevokedInviteLinkState",
    "Team",
    "TeamList",
    "TeamName",
    "UnintroducedUserState",
    "User",
    "UserState",
    "UserState_Introduced",
    "UserState_Unintroduced",
    "Username",
]
