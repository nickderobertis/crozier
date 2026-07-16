

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OrderSource(UniversalBaseModel):
    """
    Represents the origination details of an order.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name used to identify the place (physical or digital) that an order originates.
    If unset, the name defaults to the name of the application that created the order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
