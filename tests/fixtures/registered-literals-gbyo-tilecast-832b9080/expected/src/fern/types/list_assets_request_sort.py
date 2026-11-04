

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListAssetsRequestSort(enum.StrEnum):
    NEWEST = "newest"
    OLDEST = "oldest"
    UPDATED = "updated"
    NAME = "name"

    def visit(
        self,
        newest: typing.Callable[[], T_Result],
        oldest: typing.Callable[[], T_Result],
        updated: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListAssetsRequestSort.NEWEST:
            return newest()
        if self is ListAssetsRequestSort.OLDEST:
            return oldest()
        if self is ListAssetsRequestSort.UPDATED:
            return updated()
        if self is ListAssetsRequestSort.NAME:
            return name()
