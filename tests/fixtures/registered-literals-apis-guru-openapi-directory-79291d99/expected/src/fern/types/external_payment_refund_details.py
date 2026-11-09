

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .recipient_bacs_nullable import RecipientBacsNullable


class ExternalPaymentRefundDetails(UniversalBaseModel):
    """
    Details about external payment refund
    """

    bacs: typing.Optional[RecipientBacsNullable] = None
    iban: typing.Optional[str] = pydantic.Field(default=None)
    """
    The International Bank Account Number (IBAN) for the account.
    """

    name: str = pydantic.Field()
    """
    The name of the account holder.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
