

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostParResponse(UniversalBaseModel):
    request_uri: str = pydantic.Field()
    """
    RFC 9126 §2.2 — use as the `request_uri` authorization parameter
    """

    expires_in: int = pydantic.Field()
    """
    Seconds until the request URI expires
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
