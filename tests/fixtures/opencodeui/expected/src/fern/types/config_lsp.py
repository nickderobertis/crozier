

import typing

from .config_lsp_one_value import ConfigLspOneValue

ConfigLsp = typing.Union[bool, typing.Dict[str, ConfigLspOneValue]]
