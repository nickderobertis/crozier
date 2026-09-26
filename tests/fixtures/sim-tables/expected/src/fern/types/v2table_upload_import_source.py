

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2table_upload_import_source_type import V2TableUploadImportSourceType


class V2TableUploadImportSource(UniversalBaseModel):
    """
    CSV file uploaded through signed transfer instructions.
    """

    type: V2TableUploadImportSourceType = pydantic.Field()
    """
    Upload-backed import discriminator.
    """

    name: str = pydantic.Field()
    """
    CSV filename.
    """

    content_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="contentType"), pydantic.Field(alias="contentType", description="CSV MIME type.")
    ]
    """
    CSV MIME type.
    """

    size: int = pydantic.Field()
    """
    Exact CSV file size in bytes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
