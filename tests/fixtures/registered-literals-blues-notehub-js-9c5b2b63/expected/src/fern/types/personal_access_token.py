

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .personal_access_token_created_by import PersonalAccessTokenCreatedBy


class PersonalAccessToken(UniversalBaseModel):
    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the key was created
    """

    created_by: typing.Optional[PersonalAccessTokenCreatedBy] = pydantic.Field(default=None)
    """
    The user that created this key
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional description for this API Key
    """

    expires_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the key expires
    """

    last_used: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When it was last used, if ever
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name for this API Key
    """

    suspended: typing.Optional[bool] = pydantic.Field(default=None)
    """
    if true, this token cannot be used
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique and public identifier
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
