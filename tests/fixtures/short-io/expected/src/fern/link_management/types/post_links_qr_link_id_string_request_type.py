

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostLinksQrLinkIdStringRequestType(enum.StrEnum):
    PNG = "png"
    SVG = "svg"

    def visit(self, png: typing.Callable[[], T_Result], svg: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostLinksQrLinkIdStringRequestType.PNG:
            return png()
        if self is PostLinksQrLinkIdStringRequestType.SVG:
            return svg()
