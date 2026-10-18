

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrganizationProjectsResponseOutputProjectsItemDatabasesItemDiskType(enum.StrEnum):
    GP3 = "gp3"
    IO2 = "io2"

    def visit(self, gp3: typing.Callable[[], T_Result], io2: typing.Callable[[], T_Result]) -> T_Result:
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemDiskType.GP3:
            return gp3()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemDiskType.IO2:
            return io2()
