

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .share_scope import ShareScope


class Share(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    auto-generated unique share identifier
    """

    name: typing.Optional[str] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional description
    """

    scope: typing.Optional[ShareScope] = None
    paths: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    paths to files or directories, for share scope write this array must contain exactly one directory. Paths will not be validated on save so you can also create them after creating the share
    """

    username: typing.Optional[str] = None
    created_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    creation time as unix timestamp in milliseconds
    """

    updated_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    last update time as unix timestamp in milliseconds
    """

    last_use_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    last use time as unix timestamp in milliseconds
    """

    expires_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    optional share expiration, as unix timestamp in milliseconds. 0 means no expiration
    """

    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional password to protect the share. The special value "[**redacted**]" means that a password has been set, you can use this value if you want to preserve the current password when you update a share
    """

    max_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    maximum allowed access tokens. 0 means no limit
    """

    used_tokens: typing.Optional[int] = None
    allow_from: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Limit the share availability to these IP/Mask. IP/Mask must be in CIDR notation as defined in RFC 4632 and RFC 4291, for example "192.0.2.0/24" or "2001:db8::/32". An empty list means no restrictions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
