

import typing

from ...types.mcp_server_name import McpServerName
from .strata_add_servers_request_servers_one import StrataAddServersRequestServersOne

StrataAddServersRequestServers = typing.Union[typing.List[McpServerName], StrataAddServersRequestServersOne]
