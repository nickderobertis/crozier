

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TranscriptStatus(enum.StrEnum):
    """
    The status of your transcript. Possible values are queued, processing, completed, or error.
    """

    QUEUED = "queued"
    """
    The audio file is in the queue to be processed by the API.
    """

    PROCESSING = "processing"
    """
    The audio file is being processed by the API.
    """

    COMPLETED = "completed"
    """
    The transcript job has been completed successfully.
    """

    ERROR = "error"
    """
    An error occurred while processing the audio file.
    """

    def visit(
        self,
        queued: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TranscriptStatus.QUEUED:
            return queued()
        if self is TranscriptStatus.PROCESSING:
            return processing()
        if self is TranscriptStatus.COMPLETED:
            return completed()
        if self is TranscriptStatus.ERROR:
            return error()
