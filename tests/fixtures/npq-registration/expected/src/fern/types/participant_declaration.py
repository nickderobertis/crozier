

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .id_attribute import IdAttribute
from .participant_declaration_attributes import ParticipantDeclarationAttributes
from .participant_declaration_type import ParticipantDeclarationType


class ParticipantDeclaration(UniversalBaseModel):
    """
    The details of a participant declaration
    """

    id: IdAttribute
    type: ParticipantDeclarationType
    attributes: ParticipantDeclarationAttributes

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
