

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nnue_upload_status import NnueUploadStatus


class NnueFileSummary(UniversalBaseModel):
    id: str
    original_filename: typing_extensions.Annotated[
        str, FieldMetadata(alias="originalFilename"), pydantic.Field(alias="originalFilename")
    ]
    size_bytes: typing_extensions.Annotated[int, FieldMetadata(alias="sizeBytes"), pydantic.Field(alias="sizeBytes")]
    sha256hex: typing_extensions.Annotated[str, FieldMetadata(alias="sha256Hex"), pydantic.Field(alias="sha256Hex")]
    upload_status: typing_extensions.Annotated[
        NnueUploadStatus, FieldMetadata(alias="uploadStatus"), pydantic.Field(alias="uploadStatus")
    ]
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    completed_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="completedAt"), pydantic.Field(alias="completedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
