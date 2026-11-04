

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PipelineSetupRequestOnly(enum.StrEnum):
    """
    Run only the source or destination side. Useful for optimistic destination setup or isolating a connector when debugging.
    """

    SOURCE = "source"
    DESTINATION = "destination"

    def visit(self, source: typing.Callable[[], T_Result], destination: typing.Callable[[], T_Result]) -> T_Result:
        if self is PipelineSetupRequestOnly.SOURCE:
            return source()
        if self is PipelineSetupRequestOnly.DESTINATION:
            return destination()
