

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NodeAgentConfig(UniversalBaseModel):
    """
    Desired control-plane node-agent configuration.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Exact agent release version. An empty value disables agent convergence.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
