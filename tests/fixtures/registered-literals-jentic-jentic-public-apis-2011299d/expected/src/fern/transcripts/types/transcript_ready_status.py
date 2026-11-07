

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TranscriptReadyStatus(enum.StrEnum):
    """
    The status of the transcript. Either completed or error.
    """

    COMPLETED = "completed"
    """
    The transcript job has been completed successfully.
    """

    ERROR = "error"
    """
    An error occurred while processing the audio file.
    """

    def visit(self, completed: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result:
        if self is TranscriptReadyStatus.COMPLETED:
            return completed()
        if self is TranscriptReadyStatus.ERROR:
            return error()
