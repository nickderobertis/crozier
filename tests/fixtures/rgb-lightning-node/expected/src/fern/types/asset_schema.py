

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssetSchema(enum.StrEnum):
    NIA = "Nia"
    UDA = "Uda"
    CFA = "Cfa"
    IFA = "Ifa"

    def visit(
        self,
        nia: typing.Callable[[], T_Result],
        uda: typing.Callable[[], T_Result],
        cfa: typing.Callable[[], T_Result],
        ifa: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssetSchema.NIA:
            return nia()
        if self is AssetSchema.UDA:
            return uda()
        if self is AssetSchema.CFA:
            return cfa()
        if self is AssetSchema.IFA:
            return ifa()
