

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsSkewnessResponseAssetsItem(UniversalBaseModel):
    asset_skewness: typing_extensions.Annotated[float, FieldMetadata(alias="assetSkewness")] = pydantic.Field()
    """
    The skewness of the asset
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
