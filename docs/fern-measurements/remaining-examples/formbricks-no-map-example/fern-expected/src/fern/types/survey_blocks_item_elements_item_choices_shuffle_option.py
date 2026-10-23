

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemChoicesShuffleOption(enum.StrEnum):
    NONE = "none"
    ALL = "all"
    EXCEPT_LAST = "exceptLast"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
        except_last: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurveyBlocksItemElementsItemChoicesShuffleOption.NONE:
            return none()
        if self is SurveyBlocksItemElementsItemChoicesShuffleOption.ALL:
            return all_()
        if self is SurveyBlocksItemElementsItemChoicesShuffleOption.EXCEPT_LAST:
            return except_last()
