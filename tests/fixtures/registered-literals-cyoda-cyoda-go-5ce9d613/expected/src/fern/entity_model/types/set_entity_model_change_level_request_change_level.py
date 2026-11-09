

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SetEntityModelChangeLevelRequestChangeLevel(enum.StrEnum):
    ARRAY_LENGTH = "ARRAY_LENGTH"
    ARRAY_ELEMENTS = "ARRAY_ELEMENTS"
    TYPE = "TYPE"
    STRUCTURAL = "STRUCTURAL"

    def visit(
        self,
        array_length: typing.Callable[[], T_Result],
        array_elements: typing.Callable[[], T_Result],
        type: typing.Callable[[], T_Result],
        structural: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SetEntityModelChangeLevelRequestChangeLevel.ARRAY_LENGTH:
            return array_length()
        if self is SetEntityModelChangeLevelRequestChangeLevel.ARRAY_ELEMENTS:
            return array_elements()
        if self is SetEntityModelChangeLevelRequestChangeLevel.TYPE:
            return type()
        if self is SetEntityModelChangeLevelRequestChangeLevel.STRUCTURAL:
            return structural()
