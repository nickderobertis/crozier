

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SkuCapacity(UniversalBaseModel):
    """
    Capacity of the sku.
    """

    maximum: typing.Optional[str] = pydantic.Field(default=None)
    """
    Maximum capacity in TB.
    """

    usable: typing.Optional[str] = pydantic.Field(default=None)
    """
    Usable capacity in TB.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
