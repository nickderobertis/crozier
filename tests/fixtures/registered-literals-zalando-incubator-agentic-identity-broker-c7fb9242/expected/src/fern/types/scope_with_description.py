

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ScopeWithDescription(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Scope name (e.g., "user.email", "repo.read")
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable description of scope permissions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
