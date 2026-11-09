

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .possible_norm_judge_score_constituents_address import PossibleNormJudgeScoreConstituentsAddress
from .possible_norm_judge_score_constituents_email import PossibleNormJudgeScoreConstituentsEmail
from .possible_norm_judge_score_constituents_phone import PossibleNormJudgeScoreConstituentsPhone


class PossibleNormJudgeScoreConstituents(UniversalBaseModel):
    address: PossibleNormJudgeScoreConstituentsAddress
    email: PossibleNormJudgeScoreConstituentsEmail
    name_similarity_score: typing_extensions.Annotated[
        float, FieldMetadata(alias="nameSimilarityScore"), pydantic.Field(alias="nameSimilarityScore")
    ]
    other_potential_norm_judges: typing_extensions.Annotated[
        int, FieldMetadata(alias="otherPotentialNormJudges"), pydantic.Field(alias="otherPotentialNormJudges")
    ]
    phone: PossibleNormJudgeScoreConstituentsPhone

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
