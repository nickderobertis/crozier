

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_declaration_completed_request_course_identifier import (
    ParticipantDeclarationCompletedRequestCourseIdentifier,
)
from .participant_declaration_completed_request_declaration_type import (
    ParticipantDeclarationCompletedRequestDeclarationType,
)


class ParticipantDeclarationCompletedRequest(UniversalBaseModel):
    """
    An NPQ completed participant declaration
    """

    participant_id: str = pydantic.Field()
    """
    The unique id of the participant
    """

    declaration_type: ParticipantDeclarationCompletedRequestDeclarationType = pydantic.Field()
    """
    The event declaration type
    """

    declaration_date: dt.datetime = pydantic.Field()
    """
    The event declaration date
    """

    course_identifier: ParticipantDeclarationCompletedRequestCourseIdentifier = pydantic.Field()
    """
    The type of course the participant is enrolled in
    """

    has_passed: bool = pydantic.Field()
    """
    Whether the participant has failed or passed
    """

    delivery_partner_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The delivery partner ID
    """

    secondary_delivery_partner_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The secondary delivery partner ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
