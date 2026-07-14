

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_type import UserType


class User(UniversalBaseModel):
    """
    A username for authenticating with one or more types of credentials. User type defines the expected credentials allowed for the user. Native users have passwords, External users have no credential internally. Internal users are service/system users for inter-service communication.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestampt the user record was created
    """

    last_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp of the last update to this record
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    If the user is external, this is the source that the user was initialized from. All other user types have this set to null
    """

    type: typing.Optional[UserType] = pydantic.Field(default=None)
    """
    The user's type
    """

    username: str = pydantic.Field()
    """
    The username to authenticate with
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
