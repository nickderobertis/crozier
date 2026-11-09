

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InstitutionsSearchPaymentInitiationOptions(UniversalBaseModel):
    """
    Additional options that will be used to filter institutions by various Payment Initiation configurations.
    """

    consent_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID identifying the payment consent
    """

    payment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID identifying the payment
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
