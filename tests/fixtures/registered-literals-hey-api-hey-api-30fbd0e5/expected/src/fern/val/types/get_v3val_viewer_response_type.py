

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetV3ValViewerResponseType(enum.StrEnum):
    """
    Whether the viewer is a user or an organization
    """

    USER = "user"
    ORG = "org"

    def visit(self, user: typing.Callable[[], T_Result], org: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetV3ValViewerResponseType.USER:
            return user()
        if self is GetV3ValViewerResponseType.ORG:
            return org()
