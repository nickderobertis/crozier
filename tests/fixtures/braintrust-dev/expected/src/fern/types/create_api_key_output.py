

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateApiKeyOutput(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the api key
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of api key creation
    """

    name: str = pydantic.Field()
    """
    Name of the api key
    """

    preview_name: str
    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the user
    """

    user_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's email
    """

    user_given_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Given name of the user
    """

    user_family_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Family name of the user
    """

    org_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the organization
    """

    key: str = pydantic.Field()
    """
    The raw API key. It will only be exposed this one time
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
