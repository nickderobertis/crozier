

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .card_country_permission import CardCountryPermission
from .card_pin_assignment import CardPinAssignment
from .card_primary_account_number import CardPrimaryAccountNumber


class Card(UniversalBaseModel):
    activation_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    DEPRECATED: Activate a card by setting status to ACTIVE when the order_status is ACCEPTED_FOR_PRODUCTION.
    """

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

    monetary_account_id_fallback: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID of the MA to be used as fallback for this card if insufficient balance. Fallback account is removed if not supplied.
    """

    order_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order status to set for the card. Set to CARD_REQUEST_PENDING to get a virtual card produced.
    """

    pin_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The plaintext pin code. Requests require encryption to be enabled.
    """

    pin_code_assignment: typing.Optional[typing.List[CardPinAssignment]] = pydantic.Field(default=None)
    """
    Array of Types, PINs, account IDs assigned to the card.
    """

    primary_account_numbers: typing.Optional[typing.List[CardPrimaryAccountNumber]] = pydantic.Field(default=None)
    """
    Array of PANs and their attributes.
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
