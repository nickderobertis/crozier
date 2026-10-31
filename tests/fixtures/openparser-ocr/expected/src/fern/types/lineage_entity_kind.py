

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LineageEntityKind(enum.StrEnum):
    VALUE = "value"
    ARTIFACT = "artifact"
    EVIDENCE = "evidence"
    DECISION = "decision"
    COLLECTION = "collection"

    def visit(
        self,
        value: typing.Callable[[], T_Result],
        artifact: typing.Callable[[], T_Result],
        evidence: typing.Callable[[], T_Result],
        decision: typing.Callable[[], T_Result],
        collection: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LineageEntityKind.VALUE:
            return value()
        if self is LineageEntityKind.ARTIFACT:
            return artifact()
        if self is LineageEntityKind.EVIDENCE:
            return evidence()
        if self is LineageEntityKind.DECISION:
            return decision()
        if self is LineageEntityKind.COLLECTION:
            return collection()
