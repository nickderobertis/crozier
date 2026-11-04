

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .error_code import ErrorCode


class Error(UniversalBaseModel):
    """
    Error content as defined in the Microsoft REST guidelines
    (https://github.com/microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses).
    """

    code: ErrorCode
    message: str = pydantic.Field()
    """
    The message of this error.
    """

    target: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location where the error happened if available.
    """

    details: typing.Optional[typing.List["Error"]] = pydantic.Field(default=None)
    """
    The error details if available.
    """

    innererror: typing.Optional["InnerError"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .inner_error import InnerError

update_forward_refs(Error, InnerError=InnerError)
