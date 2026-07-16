

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InvoiceAcceptedPaymentMethods(UniversalBaseModel):
    """
    The payment methods that customers can use to pay an invoice on the Square-hosted invoice page.
    """

    bank_account: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether bank transfer payments are accepted. The default value is `false`.
    
    This option is allowed only for invoices that have a single payment request of type `BALANCE`.
    """

    card: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether credit card or debit card payments are accepted. The default value is `false`.
    """

    square_gift_card: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether Square gift card payments are accepted. The default value is `false`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
