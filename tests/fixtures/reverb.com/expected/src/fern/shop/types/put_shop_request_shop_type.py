

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutShopRequestShopType(enum.StrEnum):
    INDIVIDUAL = "individual"
    BUSINESS = "business"

    def visit(self, individual: typing.Callable[[], T_Result], business: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutShopRequestShopType.INDIVIDUAL:
            return individual()
        if self is PutShopRequestShopType.BUSINESS:
            return business()
