

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GenerateStreamingTokenStreamingApiResponse(UniversalBaseModel):
    token: str = pydantic.Field()
    """
    The temporary authentication token
    """

    expires_in_seconds: int = pydantic.Field()
    """
    The actual expiration time of the token in seconds.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
