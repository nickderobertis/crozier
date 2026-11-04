

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .api_error_code import ApiErrorCode


class ApiError(UniversalBaseModel):
    code: ApiErrorCode
    error_id: typing_extensions.Annotated[str, FieldMetadata(alias="errorId"), pydantic.Field(alias="errorId")]
    error_list: typing_extensions.Annotated[
        typing.List["ApiError"], FieldMetadata(alias="errorList"), pydantic.Field(alias="errorList")
    ]
    message: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ApiError)
