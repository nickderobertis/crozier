

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .possible_norm_attorney_score_constituents_address import PossibleNormAttorneyScoreConstituentsAddress
from .possible_norm_attorney_score_constituents_bar_id import PossibleNormAttorneyScoreConstituentsBarId
from .possible_norm_attorney_score_constituents_email import PossibleNormAttorneyScoreConstituentsEmail
from .possible_norm_attorney_score_constituents_law_firm import PossibleNormAttorneyScoreConstituentsLawFirm
from .possible_norm_attorney_score_constituents_phone import PossibleNormAttorneyScoreConstituentsPhone


class PossibleNormAttorneyScoreConstituents(UniversalBaseModel):
    address: PossibleNormAttorneyScoreConstituentsAddress
    bar_id: typing_extensions.Annotated[
        PossibleNormAttorneyScoreConstituentsBarId, FieldMetadata(alias="barId"), pydantic.Field(alias="barId")
    ]
    email: PossibleNormAttorneyScoreConstituentsEmail
    law_firm: typing_extensions.Annotated[
        PossibleNormAttorneyScoreConstituentsLawFirm, FieldMetadata(alias="lawFirm"), pydantic.Field(alias="lawFirm")
    ]
    name_similarity_score: typing_extensions.Annotated[
        float, FieldMetadata(alias="nameSimilarityScore"), pydantic.Field(alias="nameSimilarityScore")
    ]
    other_potential_norm_attorneys: typing_extensions.Annotated[
        int, FieldMetadata(alias="otherPotentialNormAttorneys"), pydantic.Field(alias="otherPotentialNormAttorneys")
    ]
    phone: PossibleNormAttorneyScoreConstituentsPhone

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
