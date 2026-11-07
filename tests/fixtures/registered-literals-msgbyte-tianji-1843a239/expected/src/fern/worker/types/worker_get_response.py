

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .worker_get_response_visibility import WorkerGetResponseVisibility


class WorkerGetResponse(UniversalBaseModel):
    id: str
    workspace_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]
    name: str
    description: typing.Optional[str] = None
    code: str
    revision: int
    active: bool
    enable_cron: typing_extensions.Annotated[
        bool, FieldMetadata(alias="enableCron"), pydantic.Field(alias="enableCron")
    ]
    cron_expression: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cronExpression"), pydantic.Field(alias="cronExpression")
    ] = None
    visibility: WorkerGetResponseVisibility
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
