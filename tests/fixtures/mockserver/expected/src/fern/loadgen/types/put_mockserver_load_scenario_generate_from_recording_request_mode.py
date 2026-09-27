

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverLoadScenarioGenerateFromRecordingRequestMode(enum.StrEnum):
    """
    VERBATIM = one step per recorded request; TEMPLATIZED = one step per unique (method, templatised-path) route, ordered by descending frequency
    """

    VERBATIM = "VERBATIM"
    TEMPLATIZED = "TEMPLATIZED"

    def visit(self, verbatim: typing.Callable[[], T_Result], templatized: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutMockserverLoadScenarioGenerateFromRecordingRequestMode.VERBATIM:
            return verbatim()
        if self is PutMockserverLoadScenarioGenerateFromRecordingRequestMode.TEMPLATIZED:
            return templatized()
