

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_sku_products_response_skus_item import CreateSkuProductsResponseSkusItem


class CreateSkuProductsResponse(UniversalBaseModel):
    skus: typing.List[CreateSkuProductsResponseSkusItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
