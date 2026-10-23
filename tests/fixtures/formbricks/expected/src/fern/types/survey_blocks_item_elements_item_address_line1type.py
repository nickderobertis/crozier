

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemAddressLine1Type(enum.StrEnum):
    ADDRESS = "address"

    def visit(self, address: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyBlocksItemElementsItemAddressLine1Type.ADDRESS:
            return address()
