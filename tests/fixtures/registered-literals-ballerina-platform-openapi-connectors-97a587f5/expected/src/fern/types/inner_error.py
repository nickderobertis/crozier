

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .inner_error_code import InnerErrorCode


class InnerError(UniversalBaseModel):
    """
    Inner error as defined in the Microsoft REST guidelines
    (https://github.com/microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses).
    """

    code: typing.Optional[InnerErrorCode] = None
    innererror: typing.Optional["InnerError"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(InnerError)
