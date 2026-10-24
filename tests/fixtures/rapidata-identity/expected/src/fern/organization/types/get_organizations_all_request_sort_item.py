

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetOrganizationsAllRequestSortItem(enum.StrEnum):
    NAME = "name"
    MEMBER_COUNT = "member_count"
    MEMBER_COUNT = "-member_count"
    OWNER_EMAIL = "owner_email"
    OWNER_EMAIL = "-owner_email"

    def visit(
        self,
        name: typing.Callable[[], T_Result],
        member_count: typing.Callable[[], T_Result],
        owner_email: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetOrganizationsAllRequestSortItem.NAME:
            return name()
        if self is GetOrganizationsAllRequestSortItem.MEMBER_COUNT:
            return member_count()
        if self is GetOrganizationsAllRequestSortItem.MEMBER_COUNT:
            return member_count()
        if self is GetOrganizationsAllRequestSortItem.OWNER_EMAIL:
            return owner_email()
        if self is GetOrganizationsAllRequestSortItem.OWNER_EMAIL:
            return owner_email()
