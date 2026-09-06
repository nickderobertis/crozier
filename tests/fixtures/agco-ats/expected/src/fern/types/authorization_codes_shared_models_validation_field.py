

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authorization_codes_shared_models_validation_field_type import AuthorizationCodesSharedModelsValidationFieldType


class AuthorizationCodesSharedModelsValidationField(UniversalBaseModel):
    name: typing_extensions.Annotated[
        str, FieldMetadata(alias="Name"), pydantic.Field(alias="Name", description="The name of the field.")
    ]
    """
    The name of the field.
    """

    type: typing_extensions.Annotated[
        AuthorizationCodesSharedModelsValidationFieldType,
        FieldMetadata(alias="Type"),
        pydantic.Field(alias="Type", description="The type for this validation field."),
    ]
    """
    The type for this validation field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
