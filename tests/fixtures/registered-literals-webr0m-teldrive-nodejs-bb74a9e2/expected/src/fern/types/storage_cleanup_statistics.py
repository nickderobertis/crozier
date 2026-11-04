

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StorageCleanupStatistics(UniversalBaseModel):
    trash_bytes: typing_extensions.Annotated[int, FieldMetadata(alias="trashBytes"), pydantic.Field(alias="trashBytes")]
    stale_upload_bytes: typing_extensions.Annotated[
        int, FieldMetadata(alias="staleUploadBytes"), pydantic.Field(alias="staleUploadBytes")
    ]
    stale_uploads: typing_extensions.Annotated[
        int, FieldMetadata(alias="staleUploads"), pydantic.Field(alias="staleUploads")
    ]
    total_reclaimable_bytes: typing_extensions.Annotated[
        int, FieldMetadata(alias="totalReclaimableBytes"), pydantic.Field(alias="totalReclaimableBytes")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
