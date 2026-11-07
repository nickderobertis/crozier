

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .error_details import ErrorDetails
from .node_validation_error_type import NodeValidationErrorType


class NodeValidationError(UniversalBaseModel):
    typ: str
    message: str
    description: str
    field_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fieldName"), pydantic.Field(alias="fieldName")
    ] = None
    error_type: typing_extensions.Annotated[
        NodeValidationErrorType, FieldMetadata(alias="errorType"), pydantic.Field(alias="errorType")
    ]
    details: typing.Optional[ErrorDetails] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
