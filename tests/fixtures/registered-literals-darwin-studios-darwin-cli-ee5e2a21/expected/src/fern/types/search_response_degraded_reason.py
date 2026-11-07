

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchResponseDegradedReason(enum.StrEnum):
    CANONICAL_CACHE = "CANONICAL_CACHE"
    POSTGRES_COMPATIBILITY = "POSTGRES_COMPATIBILITY"

    def visit(
        self, canonical_cache: typing.Callable[[], T_Result], postgres_compatibility: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is SearchResponseDegradedReason.CANONICAL_CACHE:
            return canonical_cache()
        if self is SearchResponseDegradedReason.POSTGRES_COMPATIBILITY:
            return postgres_compatibility()
