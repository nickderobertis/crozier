

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListDnaOligosHelmRequestSort(enum.StrEnum):
    """
    Method by which to order search results. Valid sorts are modifiedAt (modified time, most recent first) and name (entity name, alphabetical). Optionally add :asc or :desc to specify ascending or descending order.
    """

    MODIFIED_AT = "modifiedAt"
    MODIFIED_AT_ASC = "modifiedAt:asc"
    MODIFIED_AT_DESC = "modifiedAt:desc"
    NAME = "name"
    NAME_ASC = "name:asc"
    NAME_DESC = "name:desc"

    def visit(
        self,
        modified_at: typing.Callable[[], T_Result],
        modified_at_asc: typing.Callable[[], T_Result],
        modified_at_desc: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        name_asc: typing.Callable[[], T_Result],
        name_desc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListDnaOligosHelmRequestSort.MODIFIED_AT:
            return modified_at()
        if self is ListDnaOligosHelmRequestSort.MODIFIED_AT_ASC:
            return modified_at_asc()
        if self is ListDnaOligosHelmRequestSort.MODIFIED_AT_DESC:
            return modified_at_desc()
        if self is ListDnaOligosHelmRequestSort.NAME:
            return name()
        if self is ListDnaOligosHelmRequestSort.NAME_ASC:
            return name_asc()
        if self is ListDnaOligosHelmRequestSort.NAME_DESC:
            return name_desc()
