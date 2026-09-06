

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class LibraryCreationDtoScanInterval(enum.StrEnum):
    DISABLED = "DISABLED"
    HOURLY = "HOURLY"
    EVERY6H = "EVERY_6H"
    EVERY12H = "EVERY_12H"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"

    def visit(
        self,
        disabled: typing.Callable[[], T_Result],
        hourly: typing.Callable[[], T_Result],
        every6h: typing.Callable[[], T_Result],
        every12h: typing.Callable[[], T_Result],
        daily: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LibraryCreationDtoScanInterval.DISABLED:
            return disabled()
        if self is LibraryCreationDtoScanInterval.HOURLY:
            return hourly()
        if self is LibraryCreationDtoScanInterval.EVERY6H:
            return every6h()
        if self is LibraryCreationDtoScanInterval.EVERY12H:
            return every12h()
        if self is LibraryCreationDtoScanInterval.DAILY:
            return daily()
        if self is LibraryCreationDtoScanInterval.WEEKLY:
            return weekly()
