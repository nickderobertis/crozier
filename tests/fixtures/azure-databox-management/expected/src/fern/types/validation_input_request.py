

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .validation_input_request_validation_type import ValidationInputRequestValidationType


class ValidationInputRequest(UniversalBaseModel):
    """
    Minimum fields that must be present in any type of validation request.
    """

    validation_type: typing_extensions.Annotated[
        ValidationInputRequestValidationType,
        FieldMetadata(alias="validationType"),
        pydantic.Field(alias="validationType", description="Identifies the type of validation request."),
    ]
    """
    Identifies the type of validation request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
