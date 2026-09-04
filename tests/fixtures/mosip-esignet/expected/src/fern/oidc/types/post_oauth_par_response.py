

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostOauthParResponse(UniversalBaseModel):
    request_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    The request URI corresponding to the authorization request posted. This URI is a single-use reference to the respective request data in the subsequent authorization request.
    """

    expires_in: typing.Optional[float] = pydantic.Field(default=None)
    """
    A JSON number that represents the lifetime of the request URI in seconds as a positive integer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
