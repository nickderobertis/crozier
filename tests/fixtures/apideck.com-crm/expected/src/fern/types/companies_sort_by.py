

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CompaniesSortBy(enum.StrEnum):
    """
    The field on which to sort the Companies
    """

    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    NAME = "name"

    def visit(
        self,
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CompaniesSortBy.CREATED_AT:
            return created_at()
        if self is CompaniesSortBy.UPDATED_AT:
            return updated_at()
        if self is CompaniesSortBy.NAME:
            return name()
