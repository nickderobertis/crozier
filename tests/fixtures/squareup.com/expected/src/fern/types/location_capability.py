

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LocationCapability(enum.StrEnum):
    """
    The capabilities a location may have.
    """

    CREDIT_CARD_PROCESSING = "CREDIT_CARD_PROCESSING"
    AUTOMATIC_TRANSFERS = "AUTOMATIC_TRANSFERS"

    def visit(
        self, credit_card_processing: typing.Callable[[], T_Result], automatic_transfers: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is LocationCapability.CREDIT_CARD_PROCESSING:
            return credit_card_processing()
        if self is LocationCapability.AUTOMATIC_TRANSFERS:
            return automatic_transfers()
