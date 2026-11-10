

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_state import ActionState
from .activity_type import ActivityType
from .application_id import ApplicationId
from .scopes_nullable import ScopesNullable


class Activity(UniversalBaseModel):
    """
    Describes a consent activity.
    """

    activity: ActivityType
    id: str = pydantic.Field()
    """
    A unique identifier for the activity
    """

    initiated_date: str = pydantic.Field()
    """
    The date and time this activity was initiated [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC.
    """

    initiator: str = pydantic.Field()
    """
    Application ID of the client who initiated the activity.
    """

    scopes: typing.Optional[ScopesNullable] = None
    state: ActionState
    target_application_id: typing.Optional[ApplicationId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
