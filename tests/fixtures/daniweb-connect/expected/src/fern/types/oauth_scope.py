

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    BASIC = "basic"
    """
    *Originally missing*
    """

    CONVERSATIONS_READ = "conversations_read"
    """
    Access your DaniWeb conversations
    """

    CONVERSATIONS_WRITE = "conversations_write"
    """
    Manage your DaniWeb conversations
    """

    GROUPS_READ = "groups_read"
    """
    Access your DaniWeb groups
    """

    GROUPS_WRITE = "groups_write"
    """
    Manage your DaniWeb groups
    """

    PROFILE_READ = "profile_read"
    """
    Access your DaniWeb user profile
    """

    PROFILE_WRITE = "profile_write"
    """
    Manage your DaniWeb user profile
    """

    def visit(
        self,
        basic: typing.Callable[[], T_Result],
        conversations_read: typing.Callable[[], T_Result],
        conversations_write: typing.Callable[[], T_Result],
        groups_read: typing.Callable[[], T_Result],
        groups_write: typing.Callable[[], T_Result],
        profile_read: typing.Callable[[], T_Result],
        profile_write: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OauthScope.BASIC:
            return basic()
        if self is OauthScope.CONVERSATIONS_READ:
            return conversations_read()
        if self is OauthScope.CONVERSATIONS_WRITE:
            return conversations_write()
        if self is OauthScope.GROUPS_READ:
            return groups_read()
        if self is OauthScope.GROUPS_WRITE:
            return groups_write()
        if self is OauthScope.PROFILE_READ:
            return profile_read()
        if self is OauthScope.PROFILE_WRITE:
            return profile_write()
