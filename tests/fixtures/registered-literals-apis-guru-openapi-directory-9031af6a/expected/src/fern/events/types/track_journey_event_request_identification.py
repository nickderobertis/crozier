

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .track_journey_event_request_identification_account import TrackJourneyEventRequestIdentificationAccount
from .track_journey_event_request_identification_user import TrackJourneyEventRequestIdentificationUser


class TrackJourneyEventRequestIdentification(UniversalBaseModel):
    """
    Event identification requires a user, account or both
    """

    account: typing.Optional[TrackJourneyEventRequestIdentificationAccount] = pydantic.Field(default=None)
    """
    Account identification requires an accountId, domain or both
    """

    user: typing.Optional[TrackJourneyEventRequestIdentificationUser] = pydantic.Field(default=None)
    """
    User identification requires a userId, email or both
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
