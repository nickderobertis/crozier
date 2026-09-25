

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreatePaymentRequestPayment(UniversalBaseModel):
    purchase_amount: int = pydantic.Field()
    """
    Purchase amount in cents
    """

    return_url: str = pydantic.Field()
    """
    URL to redirect after payment
    """

    installments_count: int = pydantic.Field()
    """
    Number of installments
    """

    customer_cancel_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to redirect on cancellation
    """

    ipn_callback_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL for server-to-server payment notifications
    """

    locale: typing.Optional[str] = pydantic.Field(default=None)
    """
    Locale for the payment page (e.g., fr, en)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
