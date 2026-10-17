

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assistant_config import AssistantConfig


class Assistant(UniversalBaseModel):
    assistant_id: str = pydantic.Field()
    """
    The ID of the assistant.
    """

    graph_id: str = pydantic.Field()
    """
    The ID of the graph.
    """

    config: AssistantConfig = pydantic.Field()
    """
    The assistant config.
    """

    context: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Static context added to the assistant.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The time the assistant was created.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    The last time the assistant was updated.
    """

    metadata: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The assistant metadata.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version of the assistant
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the assistant
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the assistant
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
