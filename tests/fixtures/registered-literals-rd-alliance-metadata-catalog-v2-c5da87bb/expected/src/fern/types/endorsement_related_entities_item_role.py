

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EndorsementRelatedEntitiesItemRole(enum.StrEnum):
    """
    The manner of the relationship between the entity and the endorsement.
    """

    ENDORSED_SCHEME = "endorsed scheme"
    ORIGINATOR = "originator"

    def visit(
        self, endorsed_scheme: typing.Callable[[], T_Result], originator: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is EndorsementRelatedEntitiesItemRole.ENDORSED_SCHEME:
            return endorsed_scheme()
        if self is EndorsementRelatedEntitiesItemRole.ORIGINATOR:
            return originator()
