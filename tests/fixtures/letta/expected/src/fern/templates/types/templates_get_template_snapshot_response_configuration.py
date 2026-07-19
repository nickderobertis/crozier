

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class TemplatesGetTemplateSnapshotResponseConfiguration(UniversalBaseModel):
    manager_agent_entity_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="managerAgentEntityId"), pydantic.Field(alias="managerAgentEntityId")
    ] = None
    manager_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="managerType"), pydantic.Field(alias="managerType")
    ] = None
    termination_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="terminationToken"), pydantic.Field(alias="terminationToken")
    ] = None
    max_turns: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maxTurns"), pydantic.Field(alias="maxTurns")
    ] = None
    sleeptime_agent_frequency: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="sleeptimeAgentFrequency"),
        pydantic.Field(alias="sleeptimeAgentFrequency"),
    ] = None
    max_message_buffer_length: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="maxMessageBufferLength"),
        pydantic.Field(alias="maxMessageBufferLength"),
    ] = None
    min_message_buffer_length: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="minMessageBufferLength"),
        pydantic.Field(alias="minMessageBufferLength"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
