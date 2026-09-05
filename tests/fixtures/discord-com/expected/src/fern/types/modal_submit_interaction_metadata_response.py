

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modal_submit_interaction_metadata_response_triggering_interaction_metadata import (
    ModalSubmitInteractionMetadataResponseTriggeringInteractionMetadata,
)
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class ModalSubmitInteractionMetadataResponse(UniversalBaseModel):
    id: SnowflakeType
    type: int
    user: typing.Optional[UserResponse] = None
    authorizing_integration_owners: typing.Dict[str, SnowflakeType]
    original_response_message_id: typing.Optional[SnowflakeType] = None
    triggering_interaction_metadata: ModalSubmitInteractionMetadataResponseTriggeringInteractionMetadata

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
