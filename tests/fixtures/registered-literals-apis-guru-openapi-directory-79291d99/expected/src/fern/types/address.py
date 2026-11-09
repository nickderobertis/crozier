

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address_data import AddressData


class Address(UniversalBaseModel):
    """
    A physical mailing address.
    """

    data: AddressData
    primary: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When `true`, identifies the address as the primary address on an account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
