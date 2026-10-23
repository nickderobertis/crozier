

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from .block import Block
BlockValue = typing.Union[str, typing.Dict[str, typing.Any], typing.List["Block"]]
