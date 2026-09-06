

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_collections_response_fields_item_validations_additional_properties import (
    CreateCollectionsResponseFieldsItemValidationsAdditionalProperties,
)


class CreateCollectionsResponseFieldsItemValidations(UniversalBaseModel):
    """
    The validations for the field
    """

    additional_properties: typing_extensions.Annotated[
        typing.Optional[CreateCollectionsResponseFieldsItemValidationsAdditionalProperties],
        FieldMetadata(alias="additionalProperties"),
        pydantic.Field(alias="additionalProperties"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
