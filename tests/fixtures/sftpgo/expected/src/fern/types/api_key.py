

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_key_scope import ApiKeyScope


class ApiKey(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    unique key identifier
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    User friendly key name
    """

    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    We store the hash of the key. This is just like a password. For security reasons this field is omitted when you search/get API keys
    """

    scope: typing.Optional[ApiKeyScope] = None
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
    last use time as unix timestamp in milliseconds. It is saved at most once every 10 minutes
    """

    expires_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    expiration time as unix timestamp in milliseconds
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional description
    """

    user: typing.Optional[str] = pydantic.Field(default=None)
    """
    username associated with this API key. If empty and the scope is "user scope" the key can impersonate any user
    """

    admin: typing.Optional[str] = pydantic.Field(default=None)
    """
    admin associated with this API key. If empty and the scope is "admin scope" the key can impersonate any admin
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
