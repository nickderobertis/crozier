

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CleSupportDefinition(UniversalBaseModel):
    """
    A support policy definition from CLE
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the support policy
    """

    description: str = pydantic.Field()
    """
    Human-readable description of the policy
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to detailed documentation about this support policy
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
