

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ErrorResponse(UniversalBaseModel):
    """
    Human-readable API error. The server currently sends no stable machine
    error code. In particular, clients must not parse `message` to
    distinguish IP-allow-list, scope, ownership, plan, self-lockout,
    suppression-duplicate, or other errors that share an HTTP status.
    """

    message: str = pydantic.Field()
    """
    Error description
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
