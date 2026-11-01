

import typing

from ...types.mcp_server_name import McpServerName
from .strata_create_request_servers_one import StrataCreateRequestServersOne

StrataCreateRequestServers = typing.Union[typing.List[McpServerName], StrataCreateRequestServersOne]
