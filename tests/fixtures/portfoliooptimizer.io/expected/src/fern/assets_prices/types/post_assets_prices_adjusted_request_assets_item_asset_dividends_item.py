

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostAssetsPricesAdjustedRequestAssetsItemAssetDividendsItem(UniversalBaseModel):
    amount: float = pydantic.Field()
    """
    The dividend amount distributed by the asset at the date t
    """

    date: str = pydantic.Field()
    """
    The date corresponding to the date t in format YYYY-MM-DD, which is usually the ex-distribution date
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
