

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .card_pin_assignment import CardPinAssignment
from .pointer import Pointer


class CardDebit(UniversalBaseModel):
    alias: typing.Optional[Pointer] = pydantic.Field(default=None)
    """
    The pointer to the monetary account that will be connected at first with the card. Its IBAN code is also the one that will be printed on the card itself. The pointer must be of type IBAN.
    """

    monetary_account_id_fallback: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID of the MA to be used as fallback for this card if insufficient balance. Fallback account is removed if not supplied.
    """

    name_on_card: str = pydantic.Field()
    """
    The user's name as it will be on the card. Check 'card-name' for the available card names for a user.
    """

    order_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order status of this card. Can be CARD_REQUEST_PENDING or VIRTUAL_DELIVERY.
    """

    pin_code_assignment: typing.Optional[typing.List[CardPinAssignment]] = pydantic.Field(default=None)
    """
    Array of Types, PINs, account IDs assigned to the card.
    """

    preferred_name_on_card: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's preferred name that can be put on the card.
    """

    product_type: str = pydantic.Field()
    """
    The product type of the card to order.
    """

    second_line: str = pydantic.Field()
    """
    The second line of text on the card, used as name/description for it. It can contain at most 17 characters and it can be empty.
    """

    type: str = pydantic.Field()
    """
    The type of card to order. Can be MAESTRO or MASTERCARD.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
