

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...types.checkout import Checkout
from .process_checkout_response_payment_instrument import ProcessCheckoutResponsePaymentInstrument


class ProcessCheckoutResponse(Checkout):
    """
    Checkout resource returned after a synchronous processing attempt. In addition to the base checkout fields, it can include the resulting transaction identifiers and any newly created payment instrument token.
    """

    transaction_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Transaction code of the successful transaction with which the payment for the checkout is completed.
    """

    transaction_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of the successful transaction that completed payment for the checkout.
    """

    merchant_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the merchant.
    """

    redirect_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL where the payer is redirected after a redirect-based payment or SCA flow completes.
    """

    payment_instrument: typing.Optional[ProcessCheckoutResponsePaymentInstrument] = pydantic.Field(default=None)
    """
    Details of the saved payment instrument created or reused during checkout processing.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
