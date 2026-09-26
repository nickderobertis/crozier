

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_json_rpc_response_error import McpJsonRpcResponseError
from .mcp_json_rpc_response_id import McpJsonRpcResponseId
from .mcp_json_rpc_response_jsonrpc import McpJsonRpcResponseJsonrpc


class McpJsonRpcResponse(UniversalBaseModel):
    """
    JSON-RPC 2.0 response message
    """

    jsonrpc: McpJsonRpcResponseJsonrpc = pydantic.Field()
    """
    JSON-RPC version
    """

    id: typing.Optional[McpJsonRpcResponseId] = pydantic.Field(default=None)
    """
    Request identifier
    """

    result: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Method result
    """

    error: typing.Optional[McpJsonRpcResponseError] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
