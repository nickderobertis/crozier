

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .possible_norm_party_score_constituents_address import PossibleNormPartyScoreConstituentsAddress
from .possible_norm_party_score_constituents_email import PossibleNormPartyScoreConstituentsEmail
from .possible_norm_party_score_constituents_phone import PossibleNormPartyScoreConstituentsPhone
from .possible_norm_party_score_constituents_secretary_of_state_id import (
    PossibleNormPartyScoreConstituentsSecretaryOfStateId,
)


class PossibleNormPartyScoreConstituents(UniversalBaseModel):
    address: PossibleNormPartyScoreConstituentsAddress
    email: PossibleNormPartyScoreConstituentsEmail
    name_similarity_score: typing_extensions.Annotated[
        float, FieldMetadata(alias="nameSimilarityScore"), pydantic.Field(alias="nameSimilarityScore")
    ]
    other_potential_norm_parties: typing_extensions.Annotated[
        int, FieldMetadata(alias="otherPotentialNormParties"), pydantic.Field(alias="otherPotentialNormParties")
    ]
    phone: PossibleNormPartyScoreConstituentsPhone
    secretary_of_state_id: typing_extensions.Annotated[
        PossibleNormPartyScoreConstituentsSecretaryOfStateId,
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
