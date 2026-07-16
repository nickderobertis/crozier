

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WritableUser(UniversalBaseModel):
    date_joined: typing.Optional[dt.datetime] = None
    display: typing.Optional[str] = None
    email: typing.Optional[str] = None
    first_name: typing.Optional[str] = None
    groups: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The groups this user belongs to. A user will get all permissions granted to each of their groups.
    """

    id: typing.Optional[int] = None
    is_active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Designates whether this user should be treated as active. Unselect this instead of deleting accounts.
    """

    is_staff: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Designates whether the user can log into this admin site.
    """

    last_name: typing.Optional[str] = None
    password: str
    url: typing.Optional[str] = None
    username: str = pydantic.Field()
    """
    Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
