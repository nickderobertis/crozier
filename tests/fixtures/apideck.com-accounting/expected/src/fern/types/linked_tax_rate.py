

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LinkedTaxRate(UniversalBaseModel):
    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tax rate code
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the object.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the tax rate
    """

    rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    Rate of the tax rate
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
