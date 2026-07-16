

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PutMyListingsSlugStateEndRequestReason(str, enum.Enum):
    """
    The reason this listing is being ended. Valid reasons: ["not_sold", "reverb_sale"].
    """

    NOT_SOLD = "not_sold"
    REVERB_SALE = "reverb_sale"

    def visit(self, not_sold: typing.Callable[[], T_Result], reverb_sale: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutMyListingsSlugStateEndRequestReason.NOT_SOLD:
            return not_sold()
        if self is PutMyListingsSlugStateEndRequestReason.REVERB_SALE:
            return reverb_sale()
