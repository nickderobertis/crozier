

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlignAt(enum.StrEnum):
    """
    Possible values for `align.at`.

    * 'grid' Align to a fixed grid (possibly using timezone information)
    * 'from' Align a the `from` boundary
    * 'until' Align a the `until` boundary
    * 'boundary' Align a the `from` boundary if specified,
       otherwise the `until` boundary.

    When not specified, 'grid' is used.
    """

    GRID = "grid"
    BOUNDARY = "boundary"
    FROM = "from"
    UNTIL = "until"

    def visit(
        self,
        grid: typing.Callable[[], T_Result],
        boundary: typing.Callable[[], T_Result],
        from_: typing.Callable[[], T_Result],
        until: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AlignAt.GRID:
            return grid()
        if self is AlignAt.BOUNDARY:
            return boundary()
        if self is AlignAt.FROM:
            return from_()
        if self is AlignAt.UNTIL:
            return until()
