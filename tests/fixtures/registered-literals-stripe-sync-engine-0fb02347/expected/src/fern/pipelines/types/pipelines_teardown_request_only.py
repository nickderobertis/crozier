

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PipelinesTeardownRequestOnly(enum.StrEnum):
    """
    Run only the source or destination side
    """

    SOURCE = "source"
    DESTINATION = "destination"

    def visit(self, source: typing.Callable[[], T_Result], destination: typing.Callable[[], T_Result]) -> T_Result:
        if self is PipelinesTeardownRequestOnly.SOURCE:
            return source()
        if self is PipelinesTeardownRequestOnly.DESTINATION:
            return destination()
