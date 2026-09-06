

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AzureBlobFsConfigAccessTier(enum.StrEnum):
    EMPTY = ""
    ARCHIVE = "Archive"
    HOT = "Hot"
    COOL = "Cool"

    def visit(
        self,
        empty: typing.Callable[[], T_Result],
        archive: typing.Callable[[], T_Result],
        hot: typing.Callable[[], T_Result],
        cool: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AzureBlobFsConfigAccessTier.EMPTY:
            return empty()
        if self is AzureBlobFsConfigAccessTier.ARCHIVE:
            return archive()
        if self is AzureBlobFsConfigAccessTier.HOT:
            return hot()
        if self is AzureBlobFsConfigAccessTier.COOL:
            return cool()
