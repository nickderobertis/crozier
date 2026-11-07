

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebSearchBlockProvider(enum.StrEnum):
    AUTO = "auto"
    GOOGLE = "google"
    EXA = "exa"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        google: typing.Callable[[], T_Result],
        exa: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebSearchBlockProvider.AUTO:
            return auto()
        if self is WebSearchBlockProvider.GOOGLE:
            return google()
        if self is WebSearchBlockProvider.EXA:
            return exa()
