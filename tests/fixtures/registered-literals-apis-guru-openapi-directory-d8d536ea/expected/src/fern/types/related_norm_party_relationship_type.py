

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RelatedNormPartyRelationshipType(enum.StrEnum):
    PARENT = "Parent"
    CHILD = "Child"
    SAME_CORPORATE_GROUP = "Same_Corporate_Group"

    def visit(
        self,
        parent: typing.Callable[[], T_Result],
        child: typing.Callable[[], T_Result],
        same_corporate_group: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RelatedNormPartyRelationshipType.PARENT:
            return parent()
        if self is RelatedNormPartyRelationshipType.CHILD:
            return child()
        if self is RelatedNormPartyRelationshipType.SAME_CORPORATE_GROUP:
            return same_corporate_group()
