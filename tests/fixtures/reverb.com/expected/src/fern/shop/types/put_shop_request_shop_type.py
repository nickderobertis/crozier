

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PutShopRequestShopType(str, enum.Enum):
    INDIVIDUAL = "individual"
    BUSINESS = "business"

    def visit(self, individual: typing.Callable[[], T_Result], business: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutShopRequestShopType.INDIVIDUAL:
            return individual()
        if self is PutShopRequestShopType.BUSINESS:
            return business()
