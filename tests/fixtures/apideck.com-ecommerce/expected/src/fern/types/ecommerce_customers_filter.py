

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EcommerceCustomersFilter(UniversalBaseModel):
    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Customer email address to filter on
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Customer phone number to filter on
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
