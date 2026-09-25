

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .hook_run_status import HookRunStatus


class HookRun(UniversalBaseModel):
    updated_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedTime"), pydantic.Field(alias="updatedTime")
    ] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    updated_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")
    ] = None
    warnings: typing.Optional[typing.List[str]] = None
    description: typing.Optional[str] = None
    history: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    agent_run_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="agentRunId"), pydantic.Field(alias="agentRunId")
    ] = None
    output: typing.Optional[typing.Dict[str, typing.Any]] = None
    input: typing.Optional[typing.Dict[str, typing.Any]] = None
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    hook_id: typing_extensions.Annotated[str, FieldMetadata(alias="hookId"), pydantic.Field(alias="hookId")]
    name: typing.Optional[str] = None
    action_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="actionId"), pydantic.Field(alias="actionId")
    ] = None
    created_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="createdTime"), pydantic.Field(alias="createdTime")
    ]
    log_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="logId"), pydantic.Field(alias="logId")
    ] = None
    id: typing.Optional[str] = None
    run_id: typing_extensions.Annotated[str, FieldMetadata(alias="runId"), pydantic.Field(alias="runId")]
    errors: typing.Optional[typing.List[str]] = None
    status: typing.Optional[HookRunStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
