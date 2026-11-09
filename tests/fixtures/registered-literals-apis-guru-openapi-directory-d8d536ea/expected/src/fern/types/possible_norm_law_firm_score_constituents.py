

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .possible_norm_law_firm_score_constituents_address import PossibleNormLawFirmScoreConstituentsAddress
from .possible_norm_law_firm_score_constituents_email import PossibleNormLawFirmScoreConstituentsEmail
from .possible_norm_law_firm_score_constituents_phone import PossibleNormLawFirmScoreConstituentsPhone
from .possible_norm_law_firm_score_constituents_secretary_of_state_id import (
    PossibleNormLawFirmScoreConstituentsSecretaryOfStateId,
)


class PossibleNormLawFirmScoreConstituents(UniversalBaseModel):
    address: PossibleNormLawFirmScoreConstituentsAddress
    email: PossibleNormLawFirmScoreConstituentsEmail
    name_similarity_score: typing_extensions.Annotated[
        float, FieldMetadata(alias="nameSimilarityScore"), pydantic.Field(alias="nameSimilarityScore")
    ]
    other_potential_norm_law_firms: typing_extensions.Annotated[
        int, FieldMetadata(alias="otherPotentialNormLawFirms"), pydantic.Field(alias="otherPotentialNormLawFirms")
    ]
    phone: PossibleNormLawFirmScoreConstituentsPhone
    secretary_of_state_id: typing_extensions.Annotated[
        PossibleNormLawFirmScoreConstituentsSecretaryOfStateId,
        FieldMetadata(alias="secretaryOfStateId"),
        pydantic.Field(alias="secretaryOfStateId"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
