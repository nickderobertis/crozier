

from __future__ import annotations

import typing

from .import_node_body import ImportNodeBody

if typing.TYPE_CHECKING:
    from .import_node_children import ImportNodeChildren
ImportNode = typing.Union["ImportNodeChildren", ImportNodeBody]
