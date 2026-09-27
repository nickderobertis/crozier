

from __future__ import annotations

import typing

from .string_array import StringArray

if typing.TYPE_CHECKING:
    from .schema import Schema
SchemaDependenciesValue = typing.Union["Schema", StringArray]
