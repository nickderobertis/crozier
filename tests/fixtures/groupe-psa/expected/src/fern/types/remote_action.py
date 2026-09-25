

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .remote import Remote
from .remote_action_id import RemoteActionId
from .remote_action_links import RemoteActionLinks
from .remote_action_status import RemoteActionStatus
from .remote_event_feedback_detail import RemoteEventFeedbackDetail
from .remote_failed_event_status import RemoteFailedEventStatus
from .remote_type import RemoteType


class RemoteAction(UniversalBaseModel):
    links: typing_extensions.Annotated[RemoteActionLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]
    remote_action_id: typing_extensions.Annotated[
        typing.Optional[RemoteActionId], FieldMetadata(alias="remoteActionId"), pydantic.Field(alias="remoteActionId")
    ] = None
    remote: typing.Optional[Remote] = None
    status: typing.Optional[RemoteActionStatus] = None
    failure_cause: typing_extensions.Annotated[
        typing.Optional[RemoteFailedEventStatus],
        FieldMetadata(alias="failureCause"),
        pydantic.Field(alias="failureCause"),
    ] = None
    feedback_detail: typing_extensions.Annotated[
        typing.Optional[RemoteEventFeedbackDetail],
        FieldMetadata(alias="feedbackDetail"),
        pydantic.Field(alias="feedbackDetail"),
    ] = None
    type: typing.Optional[RemoteType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
