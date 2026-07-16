

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Merchant(UniversalBaseModel):
    """
    Represents a Square seller.
    """

    business_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The business name of the merchant.
    """

    country: str = pydantic.Field()
    """
    The country code associated with the merchant account, in ISO 3166 format.
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The currency associated with the merchant account, in ISO 4217 format.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-issued ID of the merchant.
    """

    language_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The language code associated with the merchant account, in BCP 47 format.
    """

    main_location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the main `Location` for this merchant.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The merchant status, active or inactive.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
