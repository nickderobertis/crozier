

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sku import Sku
from .sku_properties import SkuProperties


class SkuInformation(UniversalBaseModel):
    """
    Information of the sku.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The sku is enabled or not.
    """

    properties: typing.Optional[SkuProperties] = pydantic.Field(default=None)
    """
    Properties of the sku.
    """

    sku: typing.Optional[Sku] = pydantic.Field(default=None)
    """
    The Sku.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
