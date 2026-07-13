

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_api_key_anchored_user import UserApiKeyAnchoredUser


class UserApiKey(UniversalBaseModel):
    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the user object's creation.
    """

    granted_by_user: typing.Optional[UserApiKeyAnchoredUser] = pydantic.Field(default=None)
    """
    The user who granted access.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the user.
    """

    requested_by_user: typing.Optional[UserApiKeyAnchoredUser] = pydantic.Field(default=None)
    """
    The user who requested access.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the user object's last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
