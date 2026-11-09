

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_initiation_address import PaymentInitiationAddress
from .recipient_bacs_nullable import RecipientBacsNullable


class PaymentInitiationRecipient(UniversalBaseModel):
    """
    PaymentInitiationRecipient defines a payment initiation recipient
    """

    address: typing.Optional[PaymentInitiationAddress] = None
    bacs: typing.Optional[RecipientBacsNullable] = None
    iban: typing.Optional[str] = pydantic.Field(default=None)
    """
    The International Bank Account Number (IBAN) for the recipient.
    """

    name: str = pydantic.Field()
    """
    The name of the recipient.
    """

    recipient_id: str = pydantic.Field()
    """
    The ID of the recipient.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
