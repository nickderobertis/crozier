

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FilesUploadRequestPurpose(enum.StrEnum):
    """
    The intended purpose of the uploaded documents. Use "fine-tune" for fine-tuning. This allows us to validate the format of the uploaded file.
    """

    FINE_TUNE = "fine-tune"
    FINE_TUNE_RESULTS = "fine-tune-results"

    def visit(
        self, fine_tune: typing.Callable[[], T_Result], fine_tune_results: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is FilesUploadRequestPurpose.FINE_TUNE:
            return fine_tune()
        if self is FilesUploadRequestPurpose.FINE_TUNE_RESULTS:
            return fine_tune_results()
