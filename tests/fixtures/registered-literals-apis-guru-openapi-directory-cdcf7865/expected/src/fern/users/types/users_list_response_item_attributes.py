

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UsersListResponseItemAttributes(UniversalBaseModel):
    """
    The properties of the user entity.
    """

    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the user is an active user.
    """

    date_registered: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the user registered their account, as an iso8601 formatted timestamp.
    """

    family_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The family name of the user, used for bibliographic citations.
    """

    full_name: str = pydantic.Field()
    """
    The full name of the user, used for display on the OSF.
    """

    given_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The given name of the user, used for bibliographic citations.
    """

    locale: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's locale, e.g. 'en_US'.
    """

    middle_names: typing.Optional[str] = pydantic.Field(default=None)
    """
    The middle names of the user, used for bibliographic citations.
    """

    suffix: typing.Optional[str] = pydantic.Field(default=None)
    """
    The suffix of the user, used for bibliographic citations.
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's timezone, e.g. 'Etc/UTC'.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
