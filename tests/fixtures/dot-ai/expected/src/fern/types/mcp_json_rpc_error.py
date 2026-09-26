

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_json_rpc_error_error import McpJsonRpcErrorError
from .mcp_json_rpc_error_id import McpJsonRpcErrorId
from .mcp_json_rpc_error_jsonrpc import McpJsonRpcErrorJsonrpc


class McpJsonRpcError(UniversalBaseModel):
    """
    JSON-RPC 2.0 error response
    """

    jsonrpc: McpJsonRpcErrorJsonrpc = pydantic.Field()
    """
    JSON-RPC version
    """

    id: typing.Optional[McpJsonRpcErrorId] = pydantic.Field(default=None)
    """
    Request identifier
    """

    error: McpJsonRpcErrorError

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
