

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsReturnsResponseAssetsItem(UniversalBaseModel):
    asset_returns: typing_extensions.Annotated[typing.List[float], FieldMetadata(alias="assetReturns")] = (
        pydantic.Field()
    )
    """
    assetReturns[t] is the arithmetic return of the asset from the time t-1 to the time t, in percentage
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
