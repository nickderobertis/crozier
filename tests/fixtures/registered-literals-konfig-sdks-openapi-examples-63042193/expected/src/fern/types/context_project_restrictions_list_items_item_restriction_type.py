

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContextProjectRestrictionsListItemsItemRestrictionType(enum.StrEnum):
    """
    Type of the restriction
    """

    PROJECT = "project"
    EXPRESSION = "expression"

    def visit(self, project: typing.Callable[[], T_Result], expression: typing.Callable[[], T_Result]) -> T_Result:
        if self is ContextProjectRestrictionsListItemsItemRestrictionType.PROJECT:
            return project()
        if self is ContextProjectRestrictionsListItemsItemRestrictionType.EXPRESSION:
            return expression()
