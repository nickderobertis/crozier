

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .live_activity_action import LiveActivityAction
from .live_activity_options import LiveActivityOptions


class LiveActivityJobTarget(UniversalBaseModel):
    action: typing.Optional[LiveActivityAction] = None
    activity_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="activityId"), pydantic.Field(alias="activityId")
    ] = None
    activity_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="activityType"), pydantic.Field(alias="activityType")
    ] = None
    user_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userId"), pydantic.Field(alias="userId")
    ] = None
    topic_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="topicId"), pydantic.Field(alias="topicId")
    ] = None
    payload: typing.Optional[typing.Dict[str, typing.Any]] = None
    options: typing.Optional[LiveActivityOptions] = None
    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
