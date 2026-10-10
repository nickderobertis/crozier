

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UserToolResponseEvent(UniversalBaseModel):
    content: str = pydantic.Field()
    """
    Client-side tool result content.
    """

    thread_id: str = pydantic.Field()
    """
    Thread that owns the pending tool call.
    """

    tool_call_id: str = pydantic.Field()
    """
    Tool call id receiving the client response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
