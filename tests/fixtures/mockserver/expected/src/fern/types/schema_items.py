

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from .schema import Schema
    from .schema_array import SchemaArray
SchemaItems = typing.Union["Schema", "SchemaArray"]
