

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_parent import AgentParent


class BaseThreadDoneEvent(UniversalBaseModel):
    parent: typing.Optional[AgentParent] = None
    thread_id: str = pydantic.Field()
    """
    Thread that finished.
    """

    title: str = pydantic.Field()
    """
    Human-readable thread title.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
