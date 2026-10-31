

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .error import Error
from .validation_input_response_validation_type import ValidationInputResponseValidationType


class ValidationInputResponse(UniversalBaseModel):
    """
    Minimum properties that should be present in each individual validation response.
    """

    error: typing.Optional[Error] = pydantic.Field(default=None)
    """
    Error code and message of validation response.
    """

    validation_type: typing_extensions.Annotated[
        ValidationInputResponseValidationType,
        FieldMetadata(alias="validationType"),
        pydantic.Field(alias="validationType", description="Identifies the type of validation response."),
    ]
    """
    Identifies the type of validation response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
