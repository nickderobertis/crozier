

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mandate_response import MandateResponse
from .payment_instrument_response_card import PaymentInstrumentResponseCard
from .payment_instrument_response_type import PaymentInstrumentResponseType


class PaymentInstrumentResponse(UniversalBaseModel):
    """
    Details of a saved payment instrument.
    """

    token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique token identifying the saved payment card for a customer.
    """

    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the payment instrument is active and can be used for payments. To deactivate it, send a `DELETE` request to the resource endpoint.
    """

    type: typing.Optional[PaymentInstrumentResponseType] = pydantic.Field(default=None)
    """
    Type of the payment instrument.
    """

    card: typing.Optional[PaymentInstrumentResponseCard] = pydantic.Field(default=None)
    """
    Details of the payment card.
    """

    mandate: typing.Optional[MandateResponse] = None
    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp of when the payment instrument was created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
