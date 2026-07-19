

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .not_found_error_body_error_code import NotFoundErrorBodyErrorCode


class NotFoundErrorBody(UniversalBaseModel):
    message: str
    error_code: typing_extensions.Annotated[
        NotFoundErrorBodyErrorCode, FieldMetadata(alias="errorCode"), pydantic.Field(alias="errorCode")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
