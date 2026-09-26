

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .validation_tasks_tasks_item_status import ValidationTasksTasksItemStatus


class ValidationTasksTasksItem(UniversalBaseModel):
    updated_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedTime"), pydantic.Field(alias="updatedTime")
    ] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    validation_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="validationId"), pydantic.Field(alias="validationId")
    ]
    updated_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")
    ] = None
    warnings: typing.Optional[typing.List[str]] = None
    description: typing.Optional[str] = None
    history: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    agent_run_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="agentRunId"), pydantic.Field(alias="agentRunId")
    ] = None
    enabled: typing.Optional[bool] = None
    output: typing.Optional[typing.Dict[str, typing.Any]] = None
    input: typing.Dict[str, typing.Any]
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    name: typing.Optional[str] = None
    created_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="createdTime"), pydantic.Field(alias="createdTime")
    ]
    log_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="logId"), pydantic.Field(alias="logId")
    ] = None
    id: typing.Optional[str] = None
    task_id: typing_extensions.Annotated[str, FieldMetadata(alias="taskId"), pydantic.Field(alias="taskId")]
    errors: typing.Optional[typing.List[str]] = None
    status: typing.Optional[ValidationTasksTasksItemStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
