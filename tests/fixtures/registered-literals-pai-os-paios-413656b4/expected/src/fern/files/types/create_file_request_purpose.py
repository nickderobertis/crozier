

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateFileRequestPurpose(enum.StrEnum):
    """
    The intended purpose of the uploaded file.

    Use "fine-tune" for [Fine-tuning](/docs/api-reference/fine-tuning) and "assistants" for [Assistants](/docs/api-reference/assistants) and [Messages](/docs/api-reference/messages). This allows us to validate the format of the uploaded file is correct for fine-tuning.
    """

    FINE_TUNE = "fine-tune"
    ASSISTANTS = "assistants"

    def visit(self, fine_tune: typing.Callable[[], T_Result], assistants: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateFileRequestPurpose.FINE_TUNE:
            return fine_tune()
        if self is CreateFileRequestPurpose.ASSISTANTS:
            return assistants()
