

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .monitor_get_response_notifications_item import MonitorGetResponseNotificationsItem


class MonitorGetResponse(UniversalBaseModel):
    id: str
    workspace_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]
    name: str
    type: str
    active: bool
    interval: int
    max_retries: typing_extensions.Annotated[int, FieldMetadata(alias="maxRetries"), pydantic.Field(alias="maxRetries")]
    payload: typing.Dict[str, typing.Any]
    trending_mode: typing_extensions.Annotated[
        bool, FieldMetadata(alias="trendingMode"), pydantic.Field(alias="trendingMode")
    ]
    recent_error: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="recentError"), pydantic.Field(alias="recentError")
    ] = None
    up_message_template: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="upMessageTemplate"), pydantic.Field(alias="upMessageTemplate")
    ] = None
    down_message_template: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="downMessageTemplate"), pydantic.Field(alias="downMessageTemplate")
    ] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]
    notifications: typing.List[MonitorGetResponseNotificationsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
