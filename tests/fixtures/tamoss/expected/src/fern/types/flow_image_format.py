

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FlowImageFormat(enum.StrEnum):
    """
    The primary content type URN for the Flow.
    """

    URN_X_TAM_FORMAT_IMAGE = "urn:x-tam:format:image"

    def visit(self, urn_x_tam_format_image: typing.Callable[[], T_Result]) -> T_Result:
        if self is FlowImageFormat.URN_X_TAM_FORMAT_IMAGE:
            return urn_x_tam_format_image()
