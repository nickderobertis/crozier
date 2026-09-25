

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .agent_run_status import AgentRunStatus


class AgentRun(UniversalBaseModel):
    updated_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedTime"), pydantic.Field(alias="updatedTime")
    ] = None
    agent_id: typing_extensions.Annotated[str, FieldMetadata(alias="agentId"), pydantic.Field(alias="agentId")]
    updated_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")
    ] = None
    created_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ] = None
    created_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createdTime"), pydantic.Field(alias="createdTime")
    ] = None
    id: typing.Optional[str] = None
    run_id: typing_extensions.Annotated[str, FieldMetadata(alias="runId"), pydantic.Field(alias="runId")]
    variables_file_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="variablesFileUrl"), pydantic.Field(alias="variablesFileUrl")
    ] = None
    events: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    resource_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="resourceIds"), pydantic.Field(alias="resourceIds")
    ] = None
    status: typing.Optional[AgentRunStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
