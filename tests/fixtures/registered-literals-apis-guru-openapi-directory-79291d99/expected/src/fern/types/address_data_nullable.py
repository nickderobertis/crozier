

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .address_data import AddressData


class AddressDataNullable(AddressData):
    """
    Data about the components comprising an address.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
