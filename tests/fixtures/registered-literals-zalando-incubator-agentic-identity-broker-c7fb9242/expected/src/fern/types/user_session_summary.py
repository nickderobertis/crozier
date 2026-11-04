

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UserSessionSummary(UniversalBaseModel):
    """
    Flat session summary as returned by the session endpoints. Mirrors the
    storage.UserSessionSummary domain read model.
    """

    id: str
    service_id: str
    service_display_name: str
    token_type: str
    scope: typing.List[str]
    initiated_at: dt.datetime
    is_expired: bool
    access_token_expired: bool
    has_refresh_token: bool
    refresh_token_expires_at: typing.Optional[dt.datetime] = None
    dependent_agent_count: int = pydantic.Field()
    """
    Number of distinct agents with grants owned by the authenticated session principal that reference this service
    """

    is_encrypted: bool = pydantic.Field()
    """
    Indicates tokens are stored encrypted
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
