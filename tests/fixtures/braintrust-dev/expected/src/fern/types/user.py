

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class User(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the user
    """

    given_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Given name of the user
    """

    family_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Family name of the user
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's email
    """

    avatar_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the user's Avatar image
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of user creation
    """

    last_active_at: typing.Optional[float] = pydantic.Field(default=None)
    """
    Unix timestamp in milliseconds of the user's last activity, when available
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
