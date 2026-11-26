

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RegistryTarget(UniversalBaseModel):
    folder_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="folderId"),
        pydantic.Field(alias="folderId", description="ID of the folder containing the entity."),
    ] = None
    """
    ID of the folder containing the entity.
    """

    registry_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="registryId"),
        pydantic.Field(alias="registryId", description="Registry the entity is registered into."),
    ] = None
    """
    Registry the entity is registered into.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
