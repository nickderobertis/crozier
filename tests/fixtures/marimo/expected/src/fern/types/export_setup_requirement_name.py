

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExportSetupRequirementName(enum.StrEnum):
    PLAYWRIGHT_CHROMIUM = "playwright-chromium"

    def visit(self, playwright_chromium: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExportSetupRequirementName.PLAYWRIGHT_CHROMIUM:
            return playwright_chromium()
