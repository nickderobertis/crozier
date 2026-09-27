

from __future__ import annotations

import typing

from .http_request import HttpRequest
from .open_api_definition import OpenApiDefinition

if typing.TYPE_CHECKING:
    from .conditional_request_definition import ConditionalRequestDefinition
RequestDefinition = typing.Union[HttpRequest, OpenApiDefinition, "ConditionalRequestDefinition"]
