

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from .schema import Schema
SchemaAdditionalItems = typing.Union[bool, "Schema"]
