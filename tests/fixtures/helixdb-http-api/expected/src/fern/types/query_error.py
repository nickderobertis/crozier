

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class QueryError(UniversalBaseModel):
    """
    Stable error envelope returned by local servers and Helix Cloud gateways.
    """

    error: str = pydantic.Field()
    """
    Stable snake_case error code.
    """

    msg: str = pydantic.Field()
    """
    Human-readable diagnostic message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
