

import typing

from .header_conf_from_env import HeaderConfFromEnv
from .header_conf_value import HeaderConfValue

OtelExporterConfigHeadersItem = typing.Union[HeaderConfValue, HeaderConfFromEnv]
