

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GiftCardGanSource(str, enum.Enum):
    """
    Indicates the source that generated the gift card
    account number (GAN).
    """

    SQUARE = "SQUARE"
    OTHER = "OTHER"

    def visit(self, square: typing.Callable[[], T_Result], other: typing.Callable[[], T_Result]) -> T_Result:
        if self is GiftCardGanSource.SQUARE:
            return square()
        if self is GiftCardGanSource.OTHER:
            return other()
