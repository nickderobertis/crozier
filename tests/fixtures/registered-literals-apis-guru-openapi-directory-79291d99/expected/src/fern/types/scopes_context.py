

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScopesContext(enum.StrEnum):
    """
    An indicator for when scopes are being updated. When scopes are updated via enrollment (i.e. OAuth), the partner must send `ENROLLMENT`. When scopes are updated in a post-enrollment view, the partner must send `PORTAL`.
    """

    ENROLLMENT = "ENROLLMENT"
    PORTAL = "PORTAL"

    def visit(self, enrollment: typing.Callable[[], T_Result], portal: typing.Callable[[], T_Result]) -> T_Result:
        if self is ScopesContext.ENROLLMENT:
            return enrollment()
        if self is ScopesContext.PORTAL:
            return portal()
