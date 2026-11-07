

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UploadDailyStatistics(UniversalBaseModel):
    date: dt.date
    uploaded_bytes: typing_extensions.Annotated[
        int, FieldMetadata(alias="uploadedBytes"), pydantic.Field(alias="uploadedBytes")
    ]
    completed_files: typing_extensions.Annotated[
        int, FieldMetadata(alias="completedFiles"), pydantic.Field(alias="completedFiles")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
