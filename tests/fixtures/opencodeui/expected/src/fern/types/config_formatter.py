

import typing

from .config_formatter_one_value import ConfigFormatterOneValue

ConfigFormatter = typing.Union[bool, typing.Dict[str, ConfigFormatterOneValue]]
