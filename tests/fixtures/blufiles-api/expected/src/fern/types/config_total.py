

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ConfigTotal(UniversalBaseModel):
    max_files: typing_extensions.Annotated[float, FieldMetadata(alias="maxFiles"), pydantic.Field(alias="maxFiles")]
    max_folders: typing_extensions.Annotated[
        float, FieldMetadata(alias="maxFolders"), pydantic.Field(alias="maxFolders")
    ]
    max_pastes: typing_extensions.Annotated[float, FieldMetadata(alias="maxPastes"), pydantic.Field(alias="maxPastes")]
    max_collections: typing_extensions.Annotated[
        float, FieldMetadata(alias="maxCollections"), pydantic.Field(alias="maxCollections")
    ]
    max_shares: typing_extensions.Annotated[float, FieldMetadata(alias="maxShares"), pydantic.Field(alias="maxShares")]
    max_storage: typing_extensions.Annotated[
        float, FieldMetadata(alias="maxStorage"), pydantic.Field(alias="maxStorage")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
