

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .related_norm_party_relationship_type import RelatedNormPartyRelationshipType


class RelatedNormParty(UniversalBaseModel):
    norm_party_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normPartyId"), pydantic.Field(alias="normPartyId")
    ]
    object: str
    relationship_type: typing_extensions.Annotated[
        RelatedNormPartyRelationshipType,
        FieldMetadata(alias="relationshipType"),
        pydantic.Field(alias="relationshipType"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
