

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OpenAiFilePurpose(enum.StrEnum):
    """
    The intended purpose of the file. Supported values are `fine-tune`, `fine-tune-results`, `assistants`, and `assistants_output`.
    """

    FINE_TUNE = "fine-tune"
    FINE_TUNE_RESULTS = "fine-tune-results"
    ASSISTANTS = "assistants"
    ASSISTANTS_OUTPUT = "assistants_output"

    def visit(
        self,
        fine_tune: typing.Callable[[], T_Result],
        fine_tune_results: typing.Callable[[], T_Result],
        assistants: typing.Callable[[], T_Result],
        assistants_output: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OpenAiFilePurpose.FINE_TUNE:
            return fine_tune()
        if self is OpenAiFilePurpose.FINE_TUNE_RESULTS:
            return fine_tune_results()
        if self is OpenAiFilePurpose.ASSISTANTS:
            return assistants()
        if self is OpenAiFilePurpose.ASSISTANTS_OUTPUT:
            return assistants_output()
