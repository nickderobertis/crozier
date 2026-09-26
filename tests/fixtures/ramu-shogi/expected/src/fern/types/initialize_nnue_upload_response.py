

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nnue_file_summary import NnueFileSummary


class InitializeNnueUploadResponse(UniversalBaseModel):
    file: NnueFileSummary
    upload_id: typing_extensions.Annotated[str, FieldMetadata(alias="uploadId"), pydantic.Field(alias="uploadId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
