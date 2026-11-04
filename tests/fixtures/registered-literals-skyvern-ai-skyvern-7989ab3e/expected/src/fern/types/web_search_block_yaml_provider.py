

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebSearchBlockYamlProvider(enum.StrEnum):
    AUTO = "auto"
    GOOGLE = "google"
    EXA = "exa"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        google: typing.Callable[[], T_Result],
        exa: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebSearchBlockYamlProvider.AUTO:
            return auto()
        if self is WebSearchBlockYamlProvider.GOOGLE:
            return google()
        if self is WebSearchBlockYamlProvider.EXA:
            return exa()
