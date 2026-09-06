

from __future__ import annotations

import typing

from .inner_errors import InnerErrors

ErrorDetails = typing.Union[typing.Dict[str, "ErrorDetails"], InnerErrors]
