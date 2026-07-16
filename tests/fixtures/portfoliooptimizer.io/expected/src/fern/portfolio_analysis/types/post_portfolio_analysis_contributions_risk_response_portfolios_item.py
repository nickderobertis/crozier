

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisContributionsRiskResponsePortfoliosItem(UniversalBaseModel):
    assets_groups_risk_contributions: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="assetsGroupsRiskContributions")
    ] = pydantic.Field(default=None)
    """
    assetsGroupsRiskContributions[k] is the risk contribution of the group of assets k to the risk of the portfolio
    """

    assets_risk_contributions: typing_extensions.Annotated[
        typing.List[float], FieldMetadata(alias="assetsRiskContributions")
    ] = pydantic.Field()
    """
    assetsRiskContributions[i] is the risk contribution of the asset i to the risk of the portfolio
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
