

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from .schema import Schema
SchemaAdditionalProperties = typing.Union["Schema", bool]
