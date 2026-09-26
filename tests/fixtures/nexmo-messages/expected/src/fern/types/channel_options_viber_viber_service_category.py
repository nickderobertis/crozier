

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelOptionsViberViberServiceCategory(enum.StrEnum):
    """
    The use of different category tags enables the business to send messages for different use cases. For Viber Business Messages the first message sent from a business to a user must be personal, informative & a targeted message - not promotional. By default Vonage sends the `transaction` category to Viber Business Messages.
    """

    TRANSACTION = "transaction"
    PROMOTION = "promotion"

    def visit(self, transaction: typing.Callable[[], T_Result], promotion: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChannelOptionsViberViberServiceCategory.TRANSACTION:
            return transaction()
        if self is ChannelOptionsViberViberServiceCategory.PROMOTION:
            return promotion()
