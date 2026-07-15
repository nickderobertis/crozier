

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address


class LinkedSupplier(UniversalBaseModel):
    """
    The supplier this entity is linked to.
    """

    address: typing.Optional[Address] = None
    company_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company name of the supplier.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The display name of the supplier.
    """

    id: str = pydantic.Field()
    """
    The ID of the supplier this entity is linked to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
