

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostMyFollowsSearchRequestListingType(str, enum.Enum):
    """
    Type of listing: auctions,offers
    """

    AUCTIONS = "auctions"
    OFFERS = "offers"

    def visit(self, auctions: typing.Callable[[], T_Result], offers: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostMyFollowsSearchRequestListingType.AUCTIONS:
            return auctions()
        if self is PostMyFollowsSearchRequestListingType.OFFERS:
            return offers()
