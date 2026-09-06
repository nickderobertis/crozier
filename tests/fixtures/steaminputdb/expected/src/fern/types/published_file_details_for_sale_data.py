

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PublishedFileDetailsForSaleData(UniversalBaseModel):
    discount_percentage: typing.Optional[int] = None
    estatus: typing.Optional[int] = None
    is_for_sale: typing.Optional[bool] = None
    price_category: typing.Optional[int] = None
    price_category_floor: typing.Optional[int] = None
    price_is_pay_what_you_want: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
