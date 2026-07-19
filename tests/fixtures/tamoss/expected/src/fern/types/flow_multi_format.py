

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FlowMultiFormat(enum.StrEnum):
    """
    The primary content type URN for the Flow.
    """

    URN_X_NMOS_FORMAT_MULTI = "urn:x-nmos:format:multi"

    def visit(self, urn_x_nmos_format_multi: typing.Callable[[], T_Result]) -> T_Result:
        if self is FlowMultiFormat.URN_X_NMOS_FORMAT_MULTI:
            return urn_x_nmos_format_multi()
