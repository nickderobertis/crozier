

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyComponentsSocialDestinySocialCommendationsComponent(UniversalBaseModel):
    commendation_node_scores_by_hash: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, int]], FieldMetadata(alias="commendationNodeScoresByHash")
    ] = None
    commendation_scores_by_hash: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, int]], FieldMetadata(alias="commendationScoresByHash")
    ] = None
    score_detail_values: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="scoreDetailValues")
    ] = None
    total_score: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="totalScore")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
