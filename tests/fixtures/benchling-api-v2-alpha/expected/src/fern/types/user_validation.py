

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_validation_validation_status import UserValidationValidationStatus


class UserValidation(UniversalBaseModel):
    validation_comment: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="validationComment"),
        pydantic.Field(
            alias="validationComment", description="A string explaining the reason for the provided validation status."
        ),
    ] = None
    """
    A string explaining the reason for the provided validation status.
    """

    validation_status: typing_extensions.Annotated[
        typing.Optional[UserValidationValidationStatus],
        FieldMetadata(alias="validationStatus"),
        pydantic.Field(
            alias="validationStatus",
            description="Valid values for this enum depend on whether it is used to set a value (e.g., in a POST request), or is a return value for an existing result.\nAcceptable values for setting a status are 'VALID' or 'INVALID'. Possible return values are 'VALID', 'INVALID', or 'PARTIALLY_VALID' (a result will be partially valid if it has some valid fields and some invalid fields).",
        ),
    ] = None
    """
    Valid values for this enum depend on whether it is used to set a value (e.g., in a POST request), or is a return value for an existing result.
    Acceptable values for setting a status are 'VALID' or 'INVALID'. Possible return values are 'VALID', 'INVALID', or 'PARTIALLY_VALID' (a result will be partially valid if it has some valid fields and some invalid fields).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
