

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AffiliateAttributionSourceType(enum.StrEnum):
    """
    The type of attribution source.
    """

    URL = "url"
    PLATFORM = "platform"
    UNKNOWN = "unknown"

    def visit(
        self,
        url: typing.Callable[[], T_Result],
        platform: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AffiliateAttributionSourceType.URL:
            return url()
        if self is AffiliateAttributionSourceType.PLATFORM:
            return platform()
        if self is AffiliateAttributionSourceType.UNKNOWN:
            return unknown()
