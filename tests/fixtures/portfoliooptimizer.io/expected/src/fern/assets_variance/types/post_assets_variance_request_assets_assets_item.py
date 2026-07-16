

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsVarianceRequestAssetsAssetsItem(UniversalBaseModel):
    asset_volatility: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="assetVolatility"),
        pydantic.Field(alias="assetVolatility", description="The asset volatility"),
    ]
    """
    The asset volatility
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
