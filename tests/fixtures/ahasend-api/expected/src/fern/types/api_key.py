

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_key_object import ApiKeyObject
from .api_key_scope import ApiKeyScope


class ApiKey(UniversalBaseModel):
    object: ApiKeyObject = pydantic.Field()
    """
    Object type identifier
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the API key
    """

    created_at: dt.datetime = pydantic.Field()
    """
    When the API key was created
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    When the API key was last updated
    """

    last_used_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the API key was last used (updates every 5-10 minutes)
    """

    account_id: str = pydantic.Field()
    """
    Account ID this API key belongs to
    """

    label: str = pydantic.Field()
    """
    Human-readable label for the API key
    """

    public_key: str = pydantic.Field()
    """
    Public portion of the API key
    """

    scopes: typing.List[ApiKeyScope] = pydantic.Field()
    """
    Scopes granted to this API key
    """

    ip_allow_list: typing.List[str] = pydantic.Field()
    """
    Source IPs allowed to authenticate with this API key, as canonical CIDR blocks (a bare address is stored as a `/32` for IPv4 or `/128` for IPv6). Always present; an empty array means the key may be used from any source IP. When non-empty, an authenticated request whose client IP is not covered by an entry is rejected with HTTP 403 on every v2 endpoint, regardless of the key's scopes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
