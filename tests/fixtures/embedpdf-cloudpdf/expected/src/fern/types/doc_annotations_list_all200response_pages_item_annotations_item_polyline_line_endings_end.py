

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineLineEndingsEnd(enum.StrEnum):
    NONE = "none"
    SQUARE = "square"
    CIRCLE = "circle"
    DIAMOND = "diamond"
    OPEN_ARROW = "open-arrow"
    CLOSED_ARROW = "closed-arrow"
    BUTT = "butt"
    R_OPEN_ARROW = "r-open-arrow"
    R_CLOSED_ARROW = "r-closed-arrow"
    SLASH = "slash"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        square: typing.Callable[[], T_Result],
        circle: typing.Callable[[], T_Result],
        diamond: typing.Callable[[], T_Result],
        open_arrow: typing.Callable[[], T_Result],
        closed_arrow: typing.Callable[[], T_Result],
        butt: typing.Callable[[], T_Result],
        r_open_arrow: typing.Callable[[], T_Result],
        r_closed_arrow: typing.Callable[[], T_Result],
        slash: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineLineEndingsEnd.NONE:
            return none()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineLineEndingsEnd.SQUARE:
            return square()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineLineEndingsEnd.CIRCLE:
            return circle()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineLineEndingsEnd.DIAMOND:
            return diamond()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineLineEndingsEnd.OPEN_ARROW:
            return open_arrow()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineLineEndingsEnd.CLOSED_ARROW:
            return closed_arrow()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineLineEndingsEnd.BUTT:
            return butt()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineLineEndingsEnd.R_OPEN_ARROW:
            return r_open_arrow()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineLineEndingsEnd.R_CLOSED_ARROW:
            return r_closed_arrow()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineLineEndingsEnd.SLASH:
            return slash()
