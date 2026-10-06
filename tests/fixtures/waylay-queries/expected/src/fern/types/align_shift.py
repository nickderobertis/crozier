

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlignShift(enum.StrEnum):
    """
    Possible values for `align.shift`.

    * 'backward': keep the window size of the original interval specification,
       shifting back.
    * 'forward': keep the window size of the original interval specification,
       shifting forward.
    * 'wrap': enlarge the window size to include all of the original interval.

    When not specified, 'backward' is used.
    """

    BACKWARD = "backward"
    FORWARD = "forward"
    WRAP = "wrap"

    def visit(
        self,
        backward: typing.Callable[[], T_Result],
        forward: typing.Callable[[], T_Result],
        wrap: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AlignShift.BACKWARD:
            return backward()
        if self is AlignShift.FORWARD:
            return forward()
        if self is AlignShift.WRAP:
            return wrap()
