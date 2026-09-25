

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ApiKeyResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    api_key: str = pydantic.Field()
    """
    The API key that can be used to authenticate as the requested user.
    """

    email: str = pydantic.Field()
    """
    The email address of the user who owns the API key.
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique ID of the user who owns the API key.
    
    **Changes**: New in Zulip 7.0 (feature level 171).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
