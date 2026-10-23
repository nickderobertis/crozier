

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .dataset_register_body_openzgy_v1data_dataset_properties_file_source_infos_item import (
    DatasetRegisterBodyOpenzgyV1DataDatasetPropertiesFileSourceInfosItem,
)


class DatasetRegisterBodyOpenzgyV1DataDatasetProperties(UniversalBaseModel):
    """
    The dataset properties for a file collection.
    """

    file_collection_path: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="FileCollectionPath"),
        pydantic.Field(
            alias="FileCollectionPath",
            description="The mandatory path to the file collection. A FileCollectionPath should represent folder level access to a set of files.",
        ),
    ]
    """
    The mandatory path to the file collection. A FileCollectionPath should represent folder level access to a set of files.
    """

    index_file_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="IndexFilePath"),
        pydantic.Field(alias="IndexFilePath", description="An optional path to an index file."),
    ] = None
    """
    An optional path to an index file.
    """

    file_source_infos: typing_extensions.Annotated[
        typing.Optional[typing.List[DatasetRegisterBodyOpenzgyV1DataDatasetPropertiesFileSourceInfosItem]],
        FieldMetadata(alias="FileSourceInfos"),
        pydantic.Field(alias="FileSourceInfos", description="Array of file collection members as FileSourceInfo."),
    ] = None
    """
    Array of file collection members as FileSourceInfo.
    """

    checksum: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Checksum"),
        pydantic.Field(alias="Checksum", description="MD5 checksum of file bytes - a 32 byte hexadecimal number."),
    ] = None
    """
    MD5 checksum of file bytes - a 32 byte hexadecimal number.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
