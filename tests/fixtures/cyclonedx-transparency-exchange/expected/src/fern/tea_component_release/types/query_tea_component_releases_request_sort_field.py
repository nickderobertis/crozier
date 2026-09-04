

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class QueryTeaComponentReleasesRequestSortField(enum.StrEnum):
    CREATED_DATE = "createdDate"
    RELEASE_DATE = "releaseDate"
    VERSION = "version"

    def visit(
        self,
        created_date: typing.Callable[[], T_Result],
        release_date: typing.Callable[[], T_Result],
        version: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is QueryTeaComponentReleasesRequestSortField.CREATED_DATE:
            return created_date()
        if self is QueryTeaComponentReleasesRequestSortField.RELEASE_DATE:
            return release_date()
        if self is QueryTeaComponentReleasesRequestSortField.VERSION:
            return version()
