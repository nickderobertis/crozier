

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AtlasTermAssignmentHeaderStatus(enum.StrEnum):
    DISCOVERED = "DISCOVERED"
    PROPOSED = "PROPOSED"
    IMPORTED = "IMPORTED"
    VALIDATED = "VALIDATED"
    DEPRECATED = "DEPRECATED"
    OBSOLETE = "OBSOLETE"
    OTHER = "OTHER"

    def visit(
        self,
        discovered: typing.Callable[[], T_Result],
        proposed: typing.Callable[[], T_Result],
        imported: typing.Callable[[], T_Result],
        validated: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
        obsolete: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AtlasTermAssignmentHeaderStatus.DISCOVERED:
            return discovered()
        if self is AtlasTermAssignmentHeaderStatus.PROPOSED:
            return proposed()
        if self is AtlasTermAssignmentHeaderStatus.IMPORTED:
            return imported()
        if self is AtlasTermAssignmentHeaderStatus.VALIDATED:
            return validated()
        if self is AtlasTermAssignmentHeaderStatus.DEPRECATED:
            return deprecated()
        if self is AtlasTermAssignmentHeaderStatus.OBSOLETE:
            return obsolete()
        if self is AtlasTermAssignmentHeaderStatus.OTHER:
            return other()
