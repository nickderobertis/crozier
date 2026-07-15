

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EcommerceOrderLineItemOptionsItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the option.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the option.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value of the option.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
