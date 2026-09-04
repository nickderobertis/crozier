

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCollectionsByReleaseIdRequestSortField(enum.StrEnum):
    VERSION = "version"

    def visit(self, version: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCollectionsByReleaseIdRequestSortField.VERSION:
            return version()
