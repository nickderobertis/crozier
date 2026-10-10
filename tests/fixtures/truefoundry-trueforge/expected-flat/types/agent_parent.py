

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AgentParent(UniversalBaseModel):
    thread_id: str = pydantic.Field()
    """
    Parent thread that spawned the child agent.
    """

    tool_call_id: str = pydantic.Field()
    """
    Tool call on the parent thread that created the child.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
