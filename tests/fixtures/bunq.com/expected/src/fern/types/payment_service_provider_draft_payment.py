

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount


class PaymentServiceProviderDraftPayment(UniversalBaseModel):
    amount: Amount = pydantic.Field()
    """
    The Amount to transfer with the Payment. Must be bigger than 0.
    """

    counterparty_iban: str = pydantic.Field()
    """
    The IBAN of the counterparty.
    """

    counterparty_name: str = pydantic.Field()
    """
    The name of the counterparty.
    """

    description: str = pydantic.Field()
    """
    Description of the payment.
    """

    sender_iban: str = pydantic.Field()
    """
    The IBAN of the sender.
    """

    sender_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the sender.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new status of the Draft Payment. Can only be set to REJECTED or CANCELLED by update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
