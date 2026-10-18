

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1GetAllProjectsForOrganizationRequestSort(enum.StrEnum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    CREATED_ASC = "created_asc"
    CREATED_DESC = "created_desc"

    def visit(
        self,
        name_asc: typing.Callable[[], T_Result],
        name_desc: typing.Callable[[], T_Result],
        created_asc: typing.Callable[[], T_Result],
        created_desc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1GetAllProjectsForOrganizationRequestSort.NAME_ASC:
            return name_asc()
        if self is V1GetAllProjectsForOrganizationRequestSort.NAME_DESC:
            return name_desc()
        if self is V1GetAllProjectsForOrganizationRequestSort.CREATED_ASC:
            return created_asc()
        if self is V1GetAllProjectsForOrganizationRequestSort.CREATED_DESC:
            return created_desc()
