

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Address(UniversalBaseModel):
    """
    Physical address
    """

    country: typing.Optional[str] = None
    city: typing.Optional[str] = None
    postcode: typing.Optional[str] = None
    street: typing.Optional[str] = None
    housenumber: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
