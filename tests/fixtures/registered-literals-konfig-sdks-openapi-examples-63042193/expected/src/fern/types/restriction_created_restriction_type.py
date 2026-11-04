

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RestrictionCreatedRestrictionType(enum.StrEnum):
    """
    Type of the restriction
    """

    PROJECT = "project"
    EXPRESSION = "expression"

    def visit(self, project: typing.Callable[[], T_Result], expression: typing.Callable[[], T_Result]) -> T_Result:
        if self is RestrictionCreatedRestrictionType.PROJECT:
            return project()
        if self is RestrictionCreatedRestrictionType.EXPRESSION:
            return expression()
