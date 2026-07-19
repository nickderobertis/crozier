

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FlowVideoFormat(enum.StrEnum):
    """
    The primary content type URN for the Flow.
    """

    URN_X_NMOS_FORMAT_VIDEO = "urn:x-nmos:format:video"

    def visit(self, urn_x_nmos_format_video: typing.Callable[[], T_Result]) -> T_Result:
        if self is FlowVideoFormat.URN_X_NMOS_FORMAT_VIDEO:
            return urn_x_nmos_format_video()
