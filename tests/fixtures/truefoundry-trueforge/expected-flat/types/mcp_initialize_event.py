

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_server_init_info import McpServerInitInfo


class McpInitializeEvent(UniversalBaseModel):
    created_at: str = pydantic.Field()
    """
    ISO 8601 event timestamp.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the event (monotonic ULID).
    """

    mcp_servers: typing.List[McpServerInitInfo] = pydantic.Field()
    """
    Servers that were initialized.
    """

    thread_id: str = pydantic.Field()
    """
    Thread that triggered initialization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
