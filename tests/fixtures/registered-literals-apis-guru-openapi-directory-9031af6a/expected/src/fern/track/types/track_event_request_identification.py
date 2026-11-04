

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .track_event_request_identification_account import TrackEventRequestIdentificationAccount
from .track_event_request_identification_user import TrackEventRequestIdentificationUser


class TrackEventRequestIdentification(UniversalBaseModel):
    """
    Event identification requires a user, account or both
    """

    account: typing.Optional[TrackEventRequestIdentificationAccount] = pydantic.Field(default=None)
    """
    Account identification requires an accountId, domain or both
    """

    user: typing.Optional[TrackEventRequestIdentificationUser] = pydantic.Field(default=None)
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
