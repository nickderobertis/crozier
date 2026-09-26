

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProductProfileIn(UniversalBaseModel):
    brand: typing.Optional[str] = None
    brand_color_hex: typing.Optional[str] = None
    category: typing.Optional[str] = None
    name: typing.Optional[str] = None
    price: typing.Optional[float] = None
    product_type: typing.Optional[str] = None
    selling_points: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
