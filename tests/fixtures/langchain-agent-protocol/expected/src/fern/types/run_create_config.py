

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunCreateConfig(UniversalBaseModel):
    """
    The configuration for the agent.
    """

    tags: typing.Optional[typing.List[str]] = None
    recursion_limit: typing.Optional[int] = None
    configurable: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
