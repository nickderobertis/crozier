

import typing

from .header_conf_from_env import HeaderConfFromEnv
from .header_conf_value import HeaderConfValue

CitusEventTriggerConfEventTriggerConfHeadersItem = typing.Union[HeaderConfValue, HeaderConfFromEnv]
