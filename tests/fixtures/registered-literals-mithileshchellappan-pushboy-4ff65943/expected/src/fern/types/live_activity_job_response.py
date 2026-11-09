

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .live_activity_job_response_status import LiveActivityJobResponseStatus


class LiveActivityJobResponse(UniversalBaseModel):
    activity_id: typing_extensions.Annotated[str, FieldMetadata(alias="activityId"), pydantic.Field(alias="activityId")]
    status: LiveActivityJobResponseStatus
    dispatch_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dispatchId"), pydantic.Field(alias="dispatchId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
