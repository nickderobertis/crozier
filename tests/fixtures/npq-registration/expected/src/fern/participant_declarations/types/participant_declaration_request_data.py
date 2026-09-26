

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_declaration_request_data_attributes import ParticipantDeclarationRequestDataAttributes
from .participant_declaration_request_data_type import ParticipantDeclarationRequestDataType


class ParticipantDeclarationRequestData(UniversalBaseModel):
    """
    A participant declaration data request
    """

    type: ParticipantDeclarationRequestDataType
    attributes: ParticipantDeclarationRequestDataAttributes

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
