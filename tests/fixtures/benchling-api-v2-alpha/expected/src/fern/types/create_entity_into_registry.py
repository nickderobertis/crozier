

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .naming_strategy import NamingStrategy


class CreateEntityIntoRegistry(UniversalBaseModel):
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

    folder_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="folderId"),
        pydantic.Field(
            alias="folderId",
            description="ID of the folder containing the entity. Can be left empty when registryId is present.",
        ),
    ] = None
    """
    ID of the folder containing the entity. Can be left empty when registryId is present.
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
