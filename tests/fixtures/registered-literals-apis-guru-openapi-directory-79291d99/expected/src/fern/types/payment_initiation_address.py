

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PaymentInitiationAddress(UniversalBaseModel):
    """
    The optional address of the payment recipient. Required by most institutions outside of the UK.
    """

    city: str = pydantic.Field()
    """
    The city where the recipient is located. Maximum of 35 characters.
    """

    country: str = pydantic.Field()
    """
    The ISO 3166-1 alpha-2 country code where the recipient is located.
    """

    postal_code: str = pydantic.Field()
    """
    The postal code where the recipient is located. Maximum of 16 characters.
    """

    street: typing.List[str] = pydantic.Field()
    """
    An array of length 1-2 representing the street address where the recipient is located. Maximum of 70 characters.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
