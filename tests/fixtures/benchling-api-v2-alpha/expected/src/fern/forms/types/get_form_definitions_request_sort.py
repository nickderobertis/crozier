

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetFormDefinitionsRequestSort(enum.StrEnum):
    """
    Sets the sort-order of the response. Valid sorts are modifiedAt (modified time, most recent first). Optionally add :asc or :desc to specify ascending or descending order.
    """

    MODIFIED_AT = "modifiedAt"
    MODIFIED_AT_ASC = "modifiedAt:asc"
    MODIFIED_AT_DESC = "modifiedAt:desc"

    def visit(
        self,
        modified_at: typing.Callable[[], T_Result],
        modified_at_asc: typing.Callable[[], T_Result],
        modified_at_desc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetFormDefinitionsRequestSort.MODIFIED_AT:
            return modified_at()
        if self is GetFormDefinitionsRequestSort.MODIFIED_AT_ASC:
            return modified_at_asc()
        if self is GetFormDefinitionsRequestSort.MODIFIED_AT_DESC:
            return modified_at_desc()
