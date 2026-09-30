

import typing

from .header_conf_from_env import HeaderConfFromEnv
from .header_conf_value import HeaderConfValue

ValidateInputHttpDefinitionHeadersItem = typing.Union[HeaderConfValue, HeaderConfFromEnv]
