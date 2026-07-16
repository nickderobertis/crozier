

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsCorrelationMatrixEffectiveRankResponse(UniversalBaseModel):
    assets_correlation_matrix_effective_rank: typing_extensions.Annotated[
        typing.List[typing.List[float]], FieldMetadata(alias="assetsCorrelationMatrixEffectiveRank")
    ] = pydantic.Field()
    """
    The effective rank of the asset correlation matrix
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
