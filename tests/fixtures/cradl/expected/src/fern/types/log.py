

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Log(UniversalBaseModel):
    resource_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resourceId"), pydantic.Field(alias="resourceId")
    ] = None
    log_id: typing_extensions.Annotated[str, FieldMetadata(alias="logId"), pydantic.Field(alias="logId")]
    workflow_execution_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="workflowExecutionId"), pydantic.Field(alias="workflowExecutionId")
    ] = None
    start_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="startTime"), pydantic.Field(alias="startTime")
    ] = None
    workflow_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="workflowId"), pydantic.Field(alias="workflowId")
    ] = None
    events: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
