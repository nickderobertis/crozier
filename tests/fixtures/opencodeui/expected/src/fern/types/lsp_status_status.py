

import typing

from .lsp_status_status_one import LspStatusStatusOne
from .lsp_status_status_zero import LspStatusStatusZero

LspStatusStatus = typing.Union[LspStatusStatusZero, LspStatusStatusOne]
