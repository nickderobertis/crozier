

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptsSourcesPostResponseDataStatus(enum.StrEnum):
    """
    Ingestion status: "ingested" (decoded and cached) or "unchanged" (content-hash dedup short-circuit)
    """

    INGESTED = "ingested"
    UNCHANGED = "unchanged"

    def visit(self, ingested: typing.Callable[[], T_Result], unchanged: typing.Callable[[], T_Result]) -> T_Result:
        if self is PromptsSourcesPostResponseDataStatus.INGESTED:
            return ingested()
        if self is PromptsSourcesPostResponseDataStatus.UNCHANGED:
            return unchanged()
