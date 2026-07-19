

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class User(UniversalBaseModel):
    """
    Representation of a user.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-friendly ID of the User
    """

    name: str = pydantic.Field()
    """
    The name of the user.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The creation date of the user.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The update date of the user.
    """

    is_deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this user is deleted or not.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
