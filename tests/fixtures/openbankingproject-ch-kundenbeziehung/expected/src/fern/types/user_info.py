

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UserInfo(UniversalBaseModel):
    sub: str = pydantic.Field()
    """
    Subject identifier
    """

    preferred_username: typing.Optional[str] = pydantic.Field(default=None)
    """
    Preferred username
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full name
    """

    given_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Given name
    """

    family_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Family name
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address
    """

    email_verified: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether email is verified
    """

    institution_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Associated institution identifier
    """

    updated_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time of last update (Unix timestamp)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
