

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PartnerEndCustomerAddress(UniversalBaseModel):
    """
    The end customer's address.
    """

    city: typing.Optional[str] = None
    country_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO-3166-1 alpha-2 country code standard.
    """

    postal_code: typing.Optional[str] = None
    region: typing.Optional[str] = None
    street: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
