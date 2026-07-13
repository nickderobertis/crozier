

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .card_country_permission import CardCountryPermission
from .card_pin_assignment import CardPinAssignment
from .card_primary_account_number import CardPrimaryAccountNumber
from .label_monetary_account import LabelMonetaryAccount


class CardListing(UniversalBaseModel):
    card_limit: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The spending limit for the card.
    """

    card_limit_atm: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The ATM spending limit for the card.
    """

    card_shipment_tracking_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    A tracking link provided by our shipment provider.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country that is domestic to the card. Defaults to country of residence of user.
    """

    country_permission: typing.Optional[typing.List[CardCountryPermission]] = pydantic.Field(default=None)
    """
    The countries for which to grant (temporary) permissions to use the card.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the card's creation.
    """

    expiry_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    Expiry date of the card.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the card.
    """

    label_monetary_account_current: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The monetary account that this card is currently linked to and the label user viewing it.
    """

    label_monetary_account_ordered: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The monetary account this card was ordered on and the label user that owns the card.
    """

    monetary_account_id_fallback: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID of the MA to be used as fallback for this card if insufficient balance. Fallback account is removed if not supplied.
    """

    name_on_card: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's name on the card.
    """

    order_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order status of the card. Can be NEW_CARD_REQUEST_RECEIVED, CARD_REQUEST_PENDING, SENT_FOR_PRODUCTION, ACCEPTED_FOR_PRODUCTION, DELIVERED_TO_CUSTOMER, CARD_UPDATE_REQUESTED, CARD_UPDATE_PENDING, CARD_UPDATE_SENT, CARD_UPDATE_ACCEPTED, VIRTUAL_DELIVERY, NEW_CARD_REQUEST_PENDING_USER_APPROVAL, SENT_FOR_DELIVERY or NEW_CARD_REQUEST_CANCELLED.
    """

    payment_account_reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    The payment account reference number associated with the card.
    """

    pin_code_assignment: typing.Optional[typing.List[CardPinAssignment]] = pydantic.Field(default=None)
    """
    Array of Types, PINs, account IDs assigned to the card.
    """

    primary_account_numbers: typing.Optional[typing.List[CardPrimaryAccountNumber]] = pydantic.Field(default=None)
    """
    Array of PANs and their attributes.
    """

    public_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The public UUID of the card.
    """

    second_line: typing.Optional[str] = pydantic.Field(default=None)
    """
    The second line of text on the card
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status to set for the card. Can be ACTIVE, DEACTIVATED, LOST, STOLEN, CANCELLED, EXPIRED or PIN_TRIES_EXCEEDED.
    """

    sub_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sub-status of the card. Can be NONE or REPLACED.
    """

    sub_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sub-type of the card.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the card. Can be MAESTRO, MASTERCARD.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the card's last update.
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID of the user who is owner of the card.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
