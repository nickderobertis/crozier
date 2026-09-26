

import typing

from .config_lsp_one_value_command import ConfigLspOneValueCommand
from .config_lsp_one_value_zero import ConfigLspOneValueZero

ConfigLspOneValue = typing.Union[ConfigLspOneValueZero, ConfigLspOneValueCommand]
