

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .card import Card
from .card_payment_timeline import CardPaymentTimeline
from .device_details import DeviceDetails
from .error import Error


class CardPaymentDetails(UniversalBaseModel):
    """
    Reflects the current status of a card payment. Contains only non-confidential information.
    """

    application_cryptogram: typing.Optional[str] = pydantic.Field(default=None)
    """
    For EMV payments, the cryptogram generated for the payment.
    """

    application_identifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    For EMV payments, the application ID identifies the EMV application used for the payment.
    """

    application_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    For EMV payments, the human-readable name of the EMV application used for the payment.
    """

    auth_result_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status code returned by the card issuer that describes the payment's
    authorization status.
    """

    avs_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status code returned from the Address Verification System (AVS) check. The code can be
    `AVS_ACCEPTED`, `AVS_REJECTED`, or `AVS_NOT_CHECKED`.
    """

    card: typing.Optional[Card] = None
    card_payment_timeline: typing.Optional[CardPaymentTimeline] = None
    cvv_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status code returned from the Card Verification Value (CVV) check. The code can be
    `CVV_ACCEPTED`, `CVV_REJECTED`, or `CVV_NOT_CHECKED`.
    """

    device_details: typing.Optional[DeviceDetails] = None
    entry_method: typing.Optional[str] = pydantic.Field(default=None)
    """
    The method used to enter the card's details for the payment. The method can be
    `KEYED`, `SWIPED`, `EMV`, `ON_FILE`, or `CONTACTLESS`.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information about errors encountered during the request.
    """

    refund_requires_card_presence: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the card must be physically present for the payment to
    be refunded.  If set to `true`, the card must be present.
    """

    statement_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The statement description sent to the card networks.
    
    Note: The actual statement description varies and is likely to be truncated and appended with
    additional information on a per issuer basis.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The card payment's current state. The state can be AUTHORIZED, CAPTURED, VOIDED, or
    FAILED.
    """

    verification_method: typing.Optional[str] = pydantic.Field(default=None)
    """
    For EMV payments, the method used to verify the cardholder's identity. The method can be
    `PIN`, `SIGNATURE`, `PIN_AND_SIGNATURE`, `ON_DEVICE`, or `NONE`.
    """

    verification_results: typing.Optional[str] = pydantic.Field(default=None)
    """
    For EMV payments, the results of the cardholder verification. The result can be
    `SUCCESS`, `FAILURE`, or `UNKNOWN`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
