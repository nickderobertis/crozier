

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsReturnsSimulationBootstrapResponseSimulationsItemAssetsItem(UniversalBaseModel):
    asset_returns: typing_extensions.Annotated[typing.List[float], FieldMetadata(alias="assetReturns")] = (
        pydantic.Field()
    )
    """
    assetReturns[t] is the simulated return of the i-th asset for the t-th time period, in percentage
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
