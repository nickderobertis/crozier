

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .default_error_data_code import DefaultErrorDataCode


class DefaultErrorData(UniversalBaseModel):
    code: DefaultErrorDataCode
    http_status: typing_extensions.Annotated[
        float, FieldMetadata(alias="httpStatus"), pydantic.Field(alias="httpStatus")
    ]
    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    Path to the procedure that threw the error
    """

    stack: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stack trace of the error (only in development)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
