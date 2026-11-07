

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CompactAuditRequestCompactionType(enum.StrEnum):
    AUDIT_COMPACTION = "audit_compaction"

    def visit(self, audit_compaction: typing.Callable[[], T_Result]) -> T_Result:
        if self is CompactAuditRequestCompactionType.AUDIT_COMPACTION:
            return audit_compaction()
