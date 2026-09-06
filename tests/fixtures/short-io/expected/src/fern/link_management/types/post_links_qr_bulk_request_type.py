

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostLinksQrBulkRequestType(enum.StrEnum):
    PNG = "png"
    SVG = "svg"

    def visit(self, png: typing.Callable[[], T_Result], svg: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostLinksQrBulkRequestType.PNG:
            return png()
        if self is PostLinksQrBulkRequestType.SVG:
            return svg()
