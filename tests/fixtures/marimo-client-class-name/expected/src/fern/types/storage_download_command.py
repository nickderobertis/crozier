

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .storage_download_command_type import StorageDownloadCommandType


class StorageDownloadCommand(UniversalBaseModel):
    """
    Download a storage entry.

        Obtains a pre-signed URL or downloads the file locally and returns a virtual file URL
        so the frontend can fetch the contents.

        Attributes:
            request_id: Unique identifier for this request.
            namespace: Variable name identifying the storage backend.
            path: Full path of the entry to download.
            preview: If true, a local preview of the file is returned.
                This is useful if you need to bypass CORS.
    """

    namespace: str
    path: str
    preview: typing.Optional[bool] = None
    request_id: typing_extensions.Annotated[str, FieldMetadata(alias="requestId"), pydantic.Field(alias="requestId")]
    type: StorageDownloadCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
