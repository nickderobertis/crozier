

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from .node import Node
Tree = typing.Union[str, typing.List["Tree"], "Node"]
