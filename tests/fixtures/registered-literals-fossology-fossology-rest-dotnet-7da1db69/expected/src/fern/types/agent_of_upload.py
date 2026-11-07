

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .agent_of_upload_successful_agents_item import AgentOfUploadSuccessfulAgentsItem


class AgentOfUpload(UniversalBaseModel):
    successful_agents: typing_extensions.Annotated[
        typing.Optional[typing.List[AgentOfUploadSuccessfulAgentsItem]],
        FieldMetadata(alias="successfulAgents"),
        pydantic.Field(alias="successfulAgents"),
    ] = None
    upload_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="uploadId"), pydantic.Field(alias="uploadId")
    ] = None
    agent_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="agentName"), pydantic.Field(alias="agentName")
    ] = None
    current_agent_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="currentAgentId"), pydantic.Field(alias="currentAgentId")
    ] = None
    current_agent_rev: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="currentAgentRev"), pydantic.Field(alias="currentAgentRev")
    ] = None
    is_agent_running: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isAgentRunning"), pydantic.Field(alias="isAgentRunning")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
