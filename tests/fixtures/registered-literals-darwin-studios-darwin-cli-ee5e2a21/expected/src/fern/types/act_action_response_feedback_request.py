

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .act_action_response_feedback_request_role import ActActionResponseFeedbackRequestRole
from .act_action_response_feedback_request_state import ActActionResponseFeedbackRequestState


class ActActionResponseFeedbackRequest(UniversalBaseModel):
    interaction_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="interactionId"), pydantic.Field(alias="interactionId")
    ]
    state: ActActionResponseFeedbackRequestState
    role: ActActionResponseFeedbackRequestRole
    closes_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="closesAt"), pydantic.Field(alias="closesAt")
    ] = None
    revision: int
    web_link: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="webLink"), pydantic.Field(alias="webLink")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
