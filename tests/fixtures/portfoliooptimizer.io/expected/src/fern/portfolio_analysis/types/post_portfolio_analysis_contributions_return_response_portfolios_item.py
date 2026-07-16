

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisContributionsReturnResponsePortfoliosItem(UniversalBaseModel):
    assets_groups_return_contributions: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="assetsGroupsReturnContributions")
    ] = pydantic.Field(default=None)
    """
    assetsGroupsReturnContributions[k] is the return contribution of the group of assets k to the return of the portfolio
    """

    assets_return_contributions: typing_extensions.Annotated[
        typing.List[float], FieldMetadata(alias="assetsReturnContributions")
    ] = pydantic.Field()
    """
    assetsReturnContributions[i] is the return contribution of the asset i to the return of the portfolio
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
