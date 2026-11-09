

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .authentication_result_outcome_details_electronic_commerce_indicator import (
    AuthenticationResultOutcomeDetailsElectronicCommerceIndicator,
)


class AuthenticationResultOutcomeDetails(UniversalBaseModel):
    """
    Detailed authentication data. This field is required when the outcome is 'authenticated', 'informational', or 'attempt_acknowledged'.
    """

    three_ds_cryptogram: str = pydantic.Field()
    """
    The 3DS cryptogram (authentication value / AAV/CAVV/AEVV). This value is 20 bytes, base64-encoded into a 28-character string.
    """

    electronic_commerce_indicator: AuthenticationResultOutcomeDetailsElectronicCommerceIndicator = pydantic.Field()
    """
    Electronic Commerce Indicator (ECI) returned by the 3D Secure provider. Indicates the degree/type of authentication performed.
    """

    transaction_id: str = pydantic.Field()
    """
    Transaction identifier returned by the 3DS system: - For 3DS1: the XID - For 3DS2: the Directory Server Transaction ID (dsTransID)
    """

    version: str = pydantic.Field()
    """
    The 3D Secure version used for this authentication (for example "1.0.2" or "2.2.0").
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
