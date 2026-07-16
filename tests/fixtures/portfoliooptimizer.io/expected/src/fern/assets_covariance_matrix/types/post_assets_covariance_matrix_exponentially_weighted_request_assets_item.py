

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem(UniversalBaseModel):
    asset_returns: typing_extensions.Annotated[typing.List[float], FieldMetadata(alias="assetReturns")] = (
        pydantic.Field()
    )
    """
    assetReturns[t] is the return of the asset at the time t; all the assetReturns arrays must have the same length
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
