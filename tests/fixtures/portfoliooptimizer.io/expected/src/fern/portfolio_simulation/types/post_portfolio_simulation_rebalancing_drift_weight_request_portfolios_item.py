

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem(UniversalBaseModel):
    assets_weights: typing_extensions.Annotated[typing.List[float], FieldMetadata(alias="assetsWeights")] = (
        pydantic.Field()
    )
    """
    assetsWeights[i] is the weight of the asset i in the portfolio, in percentage
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
