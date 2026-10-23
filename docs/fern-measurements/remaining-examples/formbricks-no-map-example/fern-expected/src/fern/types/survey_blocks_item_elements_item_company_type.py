

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemCompanyType(enum.StrEnum):
    CONTACT_INFO = "contactInfo"

    def visit(self, contact_info: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyBlocksItemElementsItemCompanyType.CONTACT_INFO:
            return contact_info()
