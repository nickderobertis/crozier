

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeliveryPartnersSortingOptions(enum.StrEnum):
    """
    Sort records being returned.
    """

    NAME = "name"
    CREATED_AT = "created_at"
    CREATED_AT = "-created_at"
    UPDATED_AT = "updated_at"
    UPDATED_AT = "-updated_at"

    def visit(
        self,
        name: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeliveryPartnersSortingOptions.NAME:
            return name()
        if self is DeliveryPartnersSortingOptions.CREATED_AT:
            return created_at()
        if self is DeliveryPartnersSortingOptions.CREATED_AT:
            return created_at()
        if self is DeliveryPartnersSortingOptions.UPDATED_AT:
            return updated_at()
        if self is DeliveryPartnersSortingOptions.UPDATED_AT:
            return updated_at()
