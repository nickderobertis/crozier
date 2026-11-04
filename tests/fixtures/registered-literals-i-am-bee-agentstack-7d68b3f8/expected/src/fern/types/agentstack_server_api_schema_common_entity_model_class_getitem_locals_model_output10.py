

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extracted_file_info import ExtractedFileInfo
from .extraction_metadata import ExtractionMetadata
from .extraction_status import ExtractionStatus


class AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10(UniversalBaseModel):
    id: str
    file_id: str
    extracted_files: typing.Optional[typing.List[ExtractedFileInfo]] = None
    status: typing.Optional[ExtractionStatus] = None
    job_id: typing.Optional[str] = None
    error_message: typing.Optional[str] = None
    extraction_metadata: typing.Optional[ExtractionMetadata] = None
    started_at: typing.Optional[dt.datetime] = None
    finished_at: typing.Optional[dt.datetime] = None
    created_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
