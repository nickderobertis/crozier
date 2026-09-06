

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .content_submission_shared_business_entities_content_definition_attribute import (
    ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute,
)


class ContentSubmissionSharedBusinessEntitiesContentDefinition(UniversalBaseModel):
    """
    The definition of the content for submission
    """

    attributes: typing_extensions.Annotated[
        typing.Optional[typing.List[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]],
        FieldMetadata(alias="Attributes"),
        pydantic.Field(alias="Attributes", description="Attributes of this ContentDefinition"),
    ] = None
    """
    Attributes of this ContentDefinition
    """

    content_definition_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ContentDefinitionID"),
        pydantic.Field(alias="ContentDefinitionID", description="The ID of this content definition."),
    ] = None
    """
    The ID of this content definition.
    """

    description: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Description"),
        pydantic.Field(
            alias="Description", description="The description used on the package type in the AGCO Update System"
        ),
    ]
    """
    The description used on the package type in the AGCO Update System
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(
            alias="Name", description="The name of this content. Name must be valid for Attribute on PackageType."
        ),
    ] = None
    """
    The name of this content. Name must be valid for Attribute on PackageType.
    """

    package_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PackageTypeID"),
        pydantic.Field(
            alias="PackageTypeID", description="Read Only. The ID of the package type used for this content."
        ),
    ] = None
    """
    Read Only. The ID of the package type used for this content.
    """

    type_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="TypeID"),
        pydantic.Field(alias="TypeID", description="The type of content."),
    ] = None
    """
    The type of content.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
