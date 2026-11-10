

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_initiation_optional_restriction_bacs import PaymentInitiationOptionalRestrictionBacs
from .payment_scheme import PaymentScheme


class ExternalPaymentOptions(UniversalBaseModel):
    """
    Additional payment options
    """

    bacs: typing.Optional[PaymentInitiationOptionalRestrictionBacs] = None
    iban: typing.Optional[str] = pydantic.Field(default=None)
    """
    The International Bank Account Number (IBAN) for the payer's account. Where possible, the end user will be able to send payments only from the specified bank account if provided.
    """

    request_refund_details: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When `true`, Plaid will attempt to request refund details from the payee's financial institution.  Support varies between financial institutions and will not always be available.  If refund details could be retrieved, they will be available in the `/payment_initiation/payment/get` response.
    """

    scheme: typing.Optional[PaymentScheme] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
