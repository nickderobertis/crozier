

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .error import Error


class ErrorResponse(Error):
    """
    Errors object returned by the Discord API
    """

    errors: typing.Optional["ErrorDetails"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .error_details import ErrorDetails

update_forward_refs(ErrorResponse, ErrorDetails=ErrorDetails)
