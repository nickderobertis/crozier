

import typing

from .config_mcp_value_enabled import ConfigMcpValueEnabled
from .config_mcp_value_zero import ConfigMcpValueZero

ConfigMcpValue = typing.Union[ConfigMcpValueZero, ConfigMcpValueEnabled]
