

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IngestResponseModel(enum.StrEnum):
    PRIVATE_GPT = "private-gpt"

    def visit(self, private_gpt: typing.Callable[[], T_Result]) -> T_Result:
        if self is IngestResponseModel.PRIVATE_GPT:
            return private_gpt()
