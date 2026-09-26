

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sku_meta_in_product_type import SkuMetaInProductType


class SkuMetaIn(UniversalBaseModel):
    brand: str
    category: str
    name: typing.Optional[str] = None
    price: float
    product_type: SkuMetaInProductType
    sku: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
