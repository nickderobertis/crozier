

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .custom_fields import CustomFields
from .fields import Fields
from .naming_strategy import NamingStrategy


class OligoCreate(UniversalBaseModel):
    aliases: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Aliases to add to the Oligo
    """

    author_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="authorIds"),
        pydantic.Field(alias="authorIds", description="IDs of users to set as the Oligo's authors."),
    ] = None
    """
    IDs of users to set as the Oligo's authors.
    """

    bases: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base pairs of the oligo.
    """

    custom_fields: typing_extensions.Annotated[
        typing.Optional[CustomFields],
        FieldMetadata(alias="customFields"),
        pydantic.Field(
            alias="customFields",
            description="Custom fields to add to the Oligo. Every field should have its name as a key, mapping to an object with information about the value of the field.",
        ),
    ] = None
    """
    Custom fields to add to the Oligo. Every field should have its name as a key, mapping to an object with information about the value of the field.
    """

    fields: typing.Optional[Fields] = pydantic.Field(default=None)
    """
    Fields to set on the Oligo. Must correspond with the schema's field definitions. Every field should have its name as a key, mapping to an object with information about the value of the field.
    """

    folder_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="folderId"),
        pydantic.Field(alias="folderId", description="ID of the folder containing the Oligo."),
    ] = None
    """
    ID of the folder containing the Oligo.
    """

    name: str = pydantic.Field()
    """
    Name of the Oligo.
    """

    schema_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="schemaId"),
        pydantic.Field(alias="schemaId", description="ID of the oligo's schema."),
    ] = None
    """
    ID of the oligo's schema.
    """

    entity_registry_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="entityRegistryId"),
        pydantic.Field(
            alias="entityRegistryId",
            description="Entity registry ID to set for the registered entity. Cannot specify both entityRegistryId and namingStrategy at the same time.",
        ),
    ] = None
    """
    Entity registry ID to set for the registered entity. Cannot specify both entityRegistryId and namingStrategy at the same time.
    """

    naming_strategy: typing_extensions.Annotated[
        typing.Optional[NamingStrategy], FieldMetadata(alias="namingStrategy"), pydantic.Field(alias="namingStrategy")
    ] = None
    registry_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="registryId"),
        pydantic.Field(
            alias="registryId",
            description="Registry ID into which entity should be registered. this is the ID of the registry which was configured for a particular organization\nTo get available registryIds, use the [/registries endpoint](#/Registry/listRegistries)\n\nRequired in order for entities to be created directly in the registry.",
        ),
    ] = None
    """
    Registry ID into which entity should be registered. this is the ID of the registry which was configured for a particular organization
    To get available registryIds, use the [/registries endpoint](#/Registry/listRegistries)
    
    Required in order for entities to be created directly in the registry.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
