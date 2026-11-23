

from __future__ import annotations

import typing

from .json_scalar import JsonScalar

if typing.TYPE_CHECKING:
    from .json_array_output import JsonArrayOutput
    from .json_object_output import JsonObjectOutput
JsonValueOutput = typing.Union[typing.Optional[JsonScalar], "JsonArrayOutput", "JsonObjectOutput"]
