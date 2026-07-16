

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BadResponse(UniversalBaseModel):
    """
    An HTTP response that is not supposed to be returned by a service
    """

    body: str = pydantic.Field()
    """
    The body of the HTTP response
    """

    headers: typing.Dict[str, str] = pydantic.Field()
    """
    The HTTP headers of the response
    """

    status: int = pydantic.Field()
    """
    The HTTP status for the response
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
