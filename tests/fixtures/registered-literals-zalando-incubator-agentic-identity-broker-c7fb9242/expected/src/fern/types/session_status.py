

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SessionStatus(UniversalBaseModel):
    session_id: str = pydantic.Field()
    """
    Session identifier
    """

    initiated_at: dt.datetime = pydantic.Field()
    """
    When the OAuth2 flow was completed
    """

    access_token_expires_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the access token expires (null if unknown)
    """

    refresh_token_expires_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the refresh token expires (null if never or unknown)
    """

    is_expired: bool = pydantic.Field()
    """
    True if the refresh token has expired. Session is only marked expired
    when refresh token expires, not access token (access tokens can be refreshed).
    """

    has_refresh_token: bool = pydantic.Field()
    """
    Whether a refresh token is stored for this session
    """

    scope: typing.List[str] = pydantic.Field()
    """
    OAuth2 scopes granted in this session
    """

    dependent_agent_count: int = pydantic.Field()
    """
    Number of distinct agents with grants owned by the authenticated session principal that reference this service
    """

    tokens_encrypted: bool = pydantic.Field()
    """
    Indicates tokens are stored encrypted (always true)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
