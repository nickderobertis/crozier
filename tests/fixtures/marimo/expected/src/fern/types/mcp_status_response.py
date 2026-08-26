

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_status_response_servers_value import McpStatusResponseServersValue
from .mcp_status_response_status import McpStatusResponseStatus


class McpStatusResponse(UniversalBaseModel):
    error: typing.Optional[str] = None
    servers: typing.Optional[typing.Dict[str, McpStatusResponseServersValue]] = None
    status: McpStatusResponseStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
