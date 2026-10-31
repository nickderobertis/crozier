

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .validation_input_request import ValidationInputRequest
from .validation_request_validation_category import ValidationRequestValidationCategory


class ValidationRequest(UniversalBaseModel):
    """
    Input request for all pre job creation validation.
    """

    individual_request_details: typing_extensions.Annotated[
        typing.List[ValidationInputRequest],
        FieldMetadata(alias="individualRequestDetails"),
        pydantic.Field(
            alias="individualRequestDetails",
            description="List of request details contain validationType and its request as key and value respectively.",
        ),
    ]
    """
    List of request details contain validationType and its request as key and value respectively.
    """

    validation_category: typing_extensions.Annotated[
        ValidationRequestValidationCategory,
        FieldMetadata(alias="validationCategory"),
        pydantic.Field(alias="validationCategory", description="Identify the nature of validation."),
    ]
    """
    Identify the nature of validation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
