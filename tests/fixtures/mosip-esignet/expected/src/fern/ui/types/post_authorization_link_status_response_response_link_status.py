

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostAuthorizationLinkStatusResponseResponseLinkStatus(enum.StrEnum):
    """
    Link status of the linkCode passed in the request.
    """

    LINKED = "LINKED"

    def visit(self, linked: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostAuthorizationLinkStatusResponseResponseLinkStatus.LINKED:
            return linked()
