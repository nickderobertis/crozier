

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCustomersRequestSortItem(enum.StrEnum):
    EMAIL = "email"
    ORGANIZATION_NAME = "organization_name"
    ORGANIZATION_NAME = "-organization_name"

    def visit(self, email: typing.Callable[[], T_Result], organization_name: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCustomersRequestSortItem.EMAIL:
            return email()
        if self is GetCustomersRequestSortItem.ORGANIZATION_NAME:
            return organization_name()
        if self is GetCustomersRequestSortItem.ORGANIZATION_NAME:
            return organization_name()
