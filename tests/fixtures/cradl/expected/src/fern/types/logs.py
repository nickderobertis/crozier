

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .logs_logs_item import LogsLogsItem
from .logs_order import LogsOrder


class Logs(UniversalBaseModel):
    resource_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resourceId"), pydantic.Field(alias="resourceId")
    ] = None
    next_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nextToken"), pydantic.Field(alias="nextToken")
    ] = None
    workflow_execution_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="workflowExecutionId"), pydantic.Field(alias="workflowExecutionId")
    ] = None
    logs: typing.List[LogsLogsItem]
    workflow_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="workflowId"), pydantic.Field(alias="workflowId")
    ] = None
    order: typing.Optional[LogsOrder] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
