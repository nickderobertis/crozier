

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetFamilyBalancesV3RequestGroupBy(enum.StrEnum):
    SCHOOL_ID = "school_id"
    FAMILY_ID = "family_id"
    FAMILY_NAME = "family_name"

    def visit(
        self,
        school_id: typing.Callable[[], T_Result],
        family_id: typing.Callable[[], T_Result],
        family_name: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetFamilyBalancesV3RequestGroupBy.SCHOOL_ID:
            return school_id()
        if self is GetFamilyBalancesV3RequestGroupBy.FAMILY_ID:
            return family_id()
        if self is GetFamilyBalancesV3RequestGroupBy.FAMILY_NAME:
            return family_name()
