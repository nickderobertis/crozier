

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrganizationProjectsResponseOutputProjectsItemDatabasesItemType(enum.StrEnum):
    PRIMARY = "PRIMARY"
    READ_REPLICA = "READ_REPLICA"

    def visit(self, primary: typing.Callable[[], T_Result], read_replica: typing.Callable[[], T_Result]) -> T_Result:
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemType.PRIMARY:
            return primary()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemType.READ_REPLICA:
            return read_replica()
