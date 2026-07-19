

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FlowDataFormat(enum.StrEnum):
    """
    The primary content type URN for the Flow.
    """

    URN_X_NMOS_FORMAT_DATA = "urn:x-nmos:format:data"

    def visit(self, urn_x_nmos_format_data: typing.Callable[[], T_Result]) -> T_Result:
        if self is FlowDataFormat.URN_X_NMOS_FORMAT_DATA:
            return urn_x_nmos_format_data()
