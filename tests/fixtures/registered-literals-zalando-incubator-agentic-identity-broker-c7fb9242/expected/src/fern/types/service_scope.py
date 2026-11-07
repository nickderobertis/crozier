

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ServiceScope(UniversalBaseModel):
    value: str = pydantic.Field()
    """
    OAuth2 scope value (machine-readable identifier).
    Follows OAuth 2.0 scope syntax conventions.
    """

    description: str = pydantic.Field()
    """
    Human-readable description of what this scope allows.
    Should be clear and understandable to end users.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
