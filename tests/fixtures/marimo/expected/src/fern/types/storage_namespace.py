

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .storage_entry import StorageEntry
from .storage_namespace_backend_type import StorageNamespaceBackendType
from .variable_name import VariableName


class StorageNamespace(UniversalBaseModel):
    """
    Represents external storage systems (filesystems and object storage)

        Attributes:
            name: The variable name of the storage namespace.
            display_name: The display name of the storage namespace.
            protocol: The protocol of the storage namespace. E.g. s3, gcs, azure, http, file, in-memory.
            root_path: The root path of the storage namespace.
            backend_type: The type of the storage backend (fsspec or obstore)
            storage_entries: The storage entries in the storage namespace.
    """

    backend_type: typing_extensions.Annotated[
        StorageNamespaceBackendType, FieldMetadata(alias="backendType"), pydantic.Field(alias="backendType")
    ]
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    name: VariableName
    protocol: str
    root_path: typing_extensions.Annotated[str, FieldMetadata(alias="rootPath"), pydantic.Field(alias="rootPath")]
    storage_entries: typing_extensions.Annotated[
        typing.List[StorageEntry], FieldMetadata(alias="storageEntries"), pydantic.Field(alias="storageEntries")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
