

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entity_link_form_field_entity_type import EntityLinkFormFieldEntityType
from .entity_link_form_field_type import EntityLinkFormFieldType


class EntityLinkFormField(UniversalBaseModel):
    entity_type: typing_extensions.Annotated[
        typing.Optional[EntityLinkFormFieldEntityType],
        FieldMetadata(alias="entityType"),
        pydantic.Field(
            alias="entityType",
            description="Benchling entity type of this link. Currently only custom_entity is supported",
        ),
    ] = None
    """
    Benchling entity type of this link. Currently only custom_entity is supported
    """

    schema_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="schemaId"),
        pydantic.Field(alias="schemaId", description="Schema ID of the entity in question"),
    ] = None
    """
    Schema ID of the entity in question
    """

    type: typing.Optional[EntityLinkFormFieldType] = pydantic.Field(default=None)
    """
    The type of this form field. Type declares how this field behaves and dictates the additional properties passed along with the required properties like label and key
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
