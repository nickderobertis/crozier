

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCollectionsByProductReleaseIdRequestSortField(enum.StrEnum):
    VERSION = "version"

    def visit(self, version: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCollectionsByProductReleaseIdRequestSortField.VERSION:
            return version()
