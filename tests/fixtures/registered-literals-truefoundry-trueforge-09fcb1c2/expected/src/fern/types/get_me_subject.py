

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetMeSubject(UniversalBaseModel):
    display_name: str = pydantic.Field()
    """
    Human-readable name for the caller.
    """

    id: str = pydantic.Field()
    """
    Stable subject identifier for the caller.
    """

    type: str = pydantic.Field()
    """
    Subject kind as returned by the identity provider (stored as-is).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
