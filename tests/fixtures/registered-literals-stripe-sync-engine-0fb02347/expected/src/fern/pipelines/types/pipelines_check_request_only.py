

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PipelinesCheckRequestOnly(enum.StrEnum):
    """
    Run only the source or destination side
    """

    SOURCE = "source"
    DESTINATION = "destination"

    def visit(self, source: typing.Callable[[], T_Result], destination: typing.Callable[[], T_Result]) -> T_Result:
        if self is PipelinesCheckRequestOnly.SOURCE:
            return source()
        if self is PipelinesCheckRequestOnly.DESTINATION:
            return destination()
