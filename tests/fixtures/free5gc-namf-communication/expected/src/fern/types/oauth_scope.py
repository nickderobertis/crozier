

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    NAMF_COMM = "namf-comm"
    """
    Access to the Namf_Communication API
    """

    def visit(self, namf_comm: typing.Callable[[], T_Result]) -> T_Result:
        if self is OauthScope.NAMF_COMM:
            return namf_comm()
