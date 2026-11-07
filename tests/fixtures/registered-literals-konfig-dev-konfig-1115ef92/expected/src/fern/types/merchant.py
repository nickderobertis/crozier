

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Merchant(UniversalBaseModel):
    raw_descriptor: str = pydantic.Field()
    """
    Merchant descriptor, it can be the merchant name.
    """

    mcc: str = pydantic.Field()
    """
    A four-digit number listed in ISO 18245 for retail financial services, e.g. 4121 for Taxicabs and Rideshares. Please refer to https://en.wikipedia.org/wiki/Merchant_category_code for more details.
    """

    country: str = pydantic.Field()
    """
    Merchant's country, in ISO 3166-1 alpha-3 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
