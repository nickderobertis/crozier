

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ErrorResponse(UniversalBaseModel):
    error: typing.Optional[str] = None
    message: typing.Optional[str] = None
    status_code: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="statusCode"), pydantic.Field(alias="statusCode")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
