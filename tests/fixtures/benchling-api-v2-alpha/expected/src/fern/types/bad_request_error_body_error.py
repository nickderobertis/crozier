

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bad_request_error_body_error_type import BadRequestErrorBodyErrorType


class BadRequestErrorBodyError(UniversalBaseModel):
    type: typing.Optional[BadRequestErrorBodyErrorType] = None
    message: typing.Optional[str] = None
    user_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userMessage"), pydantic.Field(alias="userMessage")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
