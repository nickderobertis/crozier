

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsVolatilityResponseAssetsItem(UniversalBaseModel):
    asset_volatility: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="assetVolatility"),
        pydantic.Field(alias="assetVolatility", description="The volatility of the asset"),
    ]
    """
    The volatility of the asset
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
