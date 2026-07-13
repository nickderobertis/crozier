

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .card_country_permission import CardCountryPermission


class CardBatchEntry(UniversalBaseModel):
    card_limit: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The spending limit for the card.
    """

    card_limit_atm: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The ATM spending limit for the card.
    """

    country_permission: typing.Optional[typing.List[CardCountryPermission]] = pydantic.Field(default=None)
    """
    The countries for which to grant (temporary) permissions to use the card.
    """

    id: int = pydantic.Field()
    """
    The ID of the card that needs to be updated.
    """

    monetary_account_id_fallback: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID of the MA to be used as fallback for this card if insufficient balance. Fallback account is removed if not supplied.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status to set for the card. Can be ACTIVE, DEACTIVATED, LOST, STOLEN or CANCELLED, and can only be set to LOST/STOLEN/CANCELLED when order status is ACCEPTED_FOR_PRODUCTION/DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED. Can only be set to DEACTIVATED after initial activation, i.e. order_status is DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED. Mind that all the possible choices (apart from ACTIVE and DEACTIVATED) are permanent and cannot be changed after.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
