

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleDataModelsCodeYesNoType(enum.StrEnum):
    """
    A choice between a positive (yes) or a negative (no) applicability,
    represented as a string with a list of enumerated values.
    """

    YES = "YES"
    NO = "NO"

    def visit(self, yes: typing.Callable[[], T_Result], no: typing.Callable[[], T_Result]) -> T_Result:
        if self is SimpleDataModelsCodeYesNoType.YES:
            return yes()
        if self is SimpleDataModelsCodeYesNoType.NO:
            return no()
