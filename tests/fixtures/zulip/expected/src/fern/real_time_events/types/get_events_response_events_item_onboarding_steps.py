

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from ...types.onboarding_step import OnboardingStep
from .get_events_response_events_item_onboarding_steps_type import GetEventsResponseEventsItemOnboardingStepsType


class GetEventsResponseEventsItemOnboardingSteps(UniversalBaseModel):
    """
    Event sent when the set of onboarding steps to show for the current user
    has changed (e.g. because the user dismissed one).

    Clients that feature a similar tutorial experience to the Zulip web app
    may want to handle these events.

    **Changes**: Before Zulip 8.0 (feature level 233), this event was named
    `hotspots`. Prior to this feature level, one-time notice onboarding
    steps were not supported.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemOnboardingStepsType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    onboarding_steps: typing.Optional[typing.List[OnboardingStep]] = pydantic.Field(default=None)
    """
    An array of dictionaries where each dictionary contains details about a
    single onboarding step.
    
    **Changes**: Before Zulip 8.0 (feature level 233), this array was named
    `hotspots`. Prior to this feature level, one-time notice onboarding
    steps were not supported, and the `type` field in these objects did not
    exist as all onboarding steps were implicitly hotspots.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
