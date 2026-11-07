

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UnauthorizedErrorBody(UniversalBaseModel):
    """
    Returned when the API key is missing, malformed, or lacks current API access.
    """

    error: str = pydantic.Field()
    """
    Human-readable error message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
