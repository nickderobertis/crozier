

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinkTokenCreateRequestAuthFlowType(enum.StrEnum):
    """
    This field has been deprecated in favor of `auth_type_select_enabled`.
    """

    FLEXIBLE_AUTH = "FLEXIBLE_AUTH"

    def visit(self, flexible_auth: typing.Callable[[], T_Result]) -> T_Result:
        if self is LinkTokenCreateRequestAuthFlowType.FLEXIBLE_AUTH:
            return flexible_auth()
