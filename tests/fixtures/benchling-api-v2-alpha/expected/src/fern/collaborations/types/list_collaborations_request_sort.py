

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListCollaborationsRequestSort(enum.StrEnum):
    MODIFIED_AT = "modifiedAt"
    MODIFIED_AT_ASC = "modifiedAt:asc"
    MODIFIED_AT_DESC = "modifiedAt:desc"

    def visit(
        self,
        modified_at: typing.Callable[[], T_Result],
        modified_at_asc: typing.Callable[[], T_Result],
        modified_at_desc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListCollaborationsRequestSort.MODIFIED_AT:
            return modified_at()
        if self is ListCollaborationsRequestSort.MODIFIED_AT_ASC:
            return modified_at_asc()
        if self is ListCollaborationsRequestSort.MODIFIED_AT_DESC:
            return modified_at_desc()
