

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssetKind(enum.StrEnum):
    PAGE_IMAGE = "page_image"
    FIGURE = "figure"
    EMBEDDED_IMAGE = "embedded_image"
    OTHER = "other"

    def visit(
        self,
        page_image: typing.Callable[[], T_Result],
        figure: typing.Callable[[], T_Result],
        embedded_image: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssetKind.PAGE_IMAGE:
            return page_image()
        if self is AssetKind.FIGURE:
            return figure()
        if self is AssetKind.EMBEDDED_IMAGE:
            return embedded_image()
        if self is AssetKind.OTHER:
            return other()
