

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cloud_federation_api_validation_error_all_of_validation_errors import (
    CloudFederationApiValidationErrorAllOfValidationErrors,
)


class CloudFederationApiValidationErrorAllOf(UniversalBaseModel):
    validation_errors: typing_extensions.Annotated[
        typing.List[CloudFederationApiValidationErrorAllOfValidationErrors],
        FieldMetadata(alias="validationErrors"),
        pydantic.Field(alias="validationErrors"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
