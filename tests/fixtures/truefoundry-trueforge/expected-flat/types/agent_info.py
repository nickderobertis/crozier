

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_info_type import AgentInfoType


class AgentInfo(UniversalBaseModel):
    input: str = pydantic.Field()
    """
    Input prompt passed to the subagent.
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional model override for the subagent.
    """

    name: str = pydantic.Field()
    """
    Display name of the dynamic subagent.
    """

    type: AgentInfoType = pydantic.Field()
    """
    Subagent kind.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
