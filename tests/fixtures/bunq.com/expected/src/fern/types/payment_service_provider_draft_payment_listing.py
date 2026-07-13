

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount


class PaymentServiceProviderDraftPaymentListing(UniversalBaseModel):
    amount: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount of the draft payment
    """

    receiver_iban: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sender IBAN.
    """

    sender_iban: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sender IBAN.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the draft payment
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
