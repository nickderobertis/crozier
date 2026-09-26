

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelPermissionResolveRequestContactType(enum.StrEnum):
    GUARDIAN = "guardian"
    TRUSTED_CONTACT = "trusted_contact"
    UNVERIFIED_CONTACT = "unverified_contact"
    UNKNOWN = "unknown"

    def visit(
        self,
        guardian: typing.Callable[[], T_Result],
        trusted_contact: typing.Callable[[], T_Result],
        unverified_contact: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChannelPermissionResolveRequestContactType.GUARDIAN:
            return guardian()
        if self is ChannelPermissionResolveRequestContactType.TRUSTED_CONTACT:
            return trusted_contact()
        if self is ChannelPermissionResolveRequestContactType.UNVERIFIED_CONTACT:
            return unverified_contact()
        if self is ChannelPermissionResolveRequestContactType.UNKNOWN:
            return unknown()
