

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_declaration_started_request_course_identifier import (
    ParticipantDeclarationStartedRequestCourseIdentifier,
)
from .participant_declaration_started_request_declaration_type import (
    ParticipantDeclarationStartedRequestDeclarationType,
)


class ParticipantDeclarationStartedRequest(UniversalBaseModel):
    """
    An NPQ started participant declaration
    """

    participant_id: str = pydantic.Field()
    """
    The unique id of the participant
    """

    declaration_type: ParticipantDeclarationStartedRequestDeclarationType = pydantic.Field()
    """
    The event declaration type
    """

    declaration_date: dt.datetime = pydantic.Field()
    """
    The event declaration date
    """

    course_identifier: ParticipantDeclarationStartedRequestCourseIdentifier = pydantic.Field()
    """
    The type of course the participant is enrolled in
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
